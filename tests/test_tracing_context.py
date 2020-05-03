# -*- coding:utf-8 -*-
# author：huawei
import time
from threading import Thread

from skywalking import config
from skywalking.context.context_carrier import ContextCarrier
from skywalking.context.context_manager import ContextManager
from skywalking.util.count_down_latch import CountDownLatch
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
        tracing_context = ContextManager.get_tracing_context()
        count_down_latch = CountDownLatch(2)

        def local_thread():
            ContextManager.set_tracing_context(tracing_context)
            local_span = tracing_context.create_local_span("/local")
            ContextManager.stop_span(local_span)
            count_down_latch.count_down()

        def exit_thread():
            ContextManager.set_tracing_context(tracing_context)
            exit_span = tracing_context.create_exit_span("/exit", "172.1.1.1")
            ContextManager.stop_span(exit_span)
            time.sleep(10)
            count_down_latch.count_down()

        t1 = Thread(target=local_thread, args=())
        t2 = Thread(target=exit_thread, args=())
        t1.start()
        t2.start()
        count_down_latch.wait()
        ContextManager.stop_span(entry_span)
