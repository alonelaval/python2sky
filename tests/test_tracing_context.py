# -*- coding:utf-8 -*-
# author：huawei
import time
from threading import Thread

from skywalking import config
from skywalking.context.context_carrier import ContextCarrier
from skywalking.context.context_manager import ContextManager
from skywalking.util.count_down_latch import CountDownLatch
from skywalking.util.uuid_util import global_id_to_string
from tests.base_test_case import BaseTestCase


class TestTracingContext(BaseTestCase):
    def setUp(self):
        super().setUp()

    def test_ignored_segment(self):
        entry_span = ContextManager.create_entry_span("/operation", None)
        local_span = ContextManager.create_local_span("/local")
        exit_span = ContextManager.create_exit_span("/exit", "172.1.1.1")
        ContextManager.stop_span(exit_span)
        ContextManager.stop_span(local_span)
        ContextManager.stop_span(entry_span)

    def test_tracing_context(self):
        config.SERVICE_ID = 1
        config.SERVICE_INSTANCE_ID = 1
        entry_span = ContextManager.create_entry_span("/operation", None)
        local_span = ContextManager.create_local_span("/local")
        exit_span = ContextManager.create_exit_span("/exit", "172.1.1.1")
        ContextManager.stop_span(exit_span)
        ContextManager.stop_span(local_span)
        ContextManager.stop_span(entry_span)

    def test_tracing_context_extract(self):
        carrier = ContextCarrier()
        carrier.deserialize(self.SW6)
        config.SERVICE_ID = 1
        config.SERVICE_INSTANCE_ID = 1

        entry_span = ContextManager.create_entry_span("/operation", carrier)
        local_span = ContextManager.create_local_span("/local")
        exit_span = ContextManager.create_exit_span("/exit", "172.1.1.1")

        tracing_context = ContextManager.get_tracing_context()

        self.assertEqual(tracing_context.segment.refs[0], carrier)

        ContextManager.stop_span(exit_span)
        ContextManager.stop_span(local_span)
        ContextManager.stop_span(entry_span)

    def test_tracing_context_inject(self):
        carrier = ContextCarrier()
        config.SERVICE_ID = 1
        config.SERVICE_INSTANCE_ID = 1

        entry_span = ContextManager.create_entry_span("/operation", None)
        local_span = ContextManager.create_local_span("/local")
        exit_span = ContextManager.create_inject_exit_span("/exit", "172.1.1.1", carrier)

        tracing_context = ContextManager.get_tracing_context()

        sw6 = carrier.serialize()
        self.assertIsNotNone(sw6)

        ContextManager.stop_span(exit_span)
        ContextManager.stop_span(local_span)
        ContextManager.stop_span(entry_span)

    def test_tracing_context_inject_and_extract(self):
        carrier = ContextCarrier()
        carrier.deserialize(self.SW6)
        config.SERVICE_ID = 1
        config.SERVICE_INSTANCE_ID = 1

        entry_span = ContextManager.create_entry_span("/operation", carrier)
        local_span = ContextManager.create_local_span("/local")
        carrier2 = ContextCarrier()
        exit_span = ContextManager.create_inject_exit_span("/exit", "172.1.1.1", carrier2)

        tracing_context = ContextManager.get_tracing_context()

        sw6 = carrier.serialize()
        self.assertEqual(sw6, carrier.serialize())
        self.assertEqual(ContextManager.get_global_trace_id(), global_id_to_string(["3", "4", "5"]))
        ContextManager.stop_span(exit_span)
        ContextManager.stop_span(local_span)
        ContextManager.stop_span(entry_span)
        self.assertEqual(carrier.trace_id, carrier2.trace_id)

    def local_thread(self, tracing_context, count_down_latch):
        ContextManager.CONTEXT.trace_context = tracing_context
        local_span = ContextManager.create_local_span("/local")
        ContextManager.stop_span(local_span)
        count_down_latch.count_down()

    def exit_thread(self, tracing_context, count_down_latch):
        ContextManager.CONTEXT.trace_context = tracing_context
        exit_span = ContextManager.create_exit_span("/exit", "172.1.1.1")
        ContextManager.stop_span(exit_span)
        count_down_latch.count_down()

    def test_async(self):
        config.SERVICE_ID = 1
        config.SERVICE_INSTANCE_ID = 1
        entry_span = ContextManager.create_entry_span("/operation", None)
        count_down_latch = CountDownLatch(2)
        t1 = Thread(target=self.local_thread, args=(ContextManager.get_tracing_context(), count_down_latch,))
        t2 = Thread(target=self.exit_thread, args=(ContextManager.get_tracing_context(), count_down_latch,))
        t1.start()
        t2.start()
        count_down_latch.wait()
        ContextManager.stop_span(entry_span)

    def test_async2(self):
        config.SERVICE_ID = 1
        config.SERVICE_INSTANCE_ID = 1

        entry_span = ContextManager.create_entry_span("/operation", None)
        context_carrier = ContextManager.capture()
        count_down_latch = CountDownLatch(2)
        trace_id = ContextManager.get_global_trace_id()

        def local_thread():
            local_span = ContextManager.create_local_span("/local")
            ContextManager.continued(context_carrier)
            trace_id1 = ContextManager.get_global_trace_id()
            self.assertEqual(trace_id1, trace_id)
            ContextManager.stop_span(local_span)
            count_down_latch.count_down()

        def exit_thread():
            exit_span = ContextManager.create_exit_span("/exit", "172.1.1.1")
            ContextManager.continued(context_carrier)
            trace_id2 = ContextManager.get_global_trace_id()
            self.assertEqual(trace_id2, trace_id)
            time.sleep(3)
            ContextManager.stop_span(exit_span)
            count_down_latch.count_down()

        t1 = Thread(target=local_thread, args=())
        t2 = Thread(target=exit_thread, args=())
        t1.start()
        t2.start()
        ContextManager.stop_span(entry_span)
        count_down_latch.wait()

