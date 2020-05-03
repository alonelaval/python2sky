# -*- coding:utf-8 -*-
# author：huawei
from skywalking.context.context_carrier import ContextCarrier
from skywalking.context.context_manager import ContextManager
from skywalking.context.span import Span
from skywalking.context.trace_segment import TraceSegment
from skywalking.exception.exceptions import SkywalkingException
from skywalking.proto.common.trace_common_pb2 import Entry, Unknown
from tests.base_test_case import BaseTestCase


class TestTraceSegment(BaseTestCase):
    def setUp(self):
        super().setUp()
        self.segment = TraceSegment()
        self.segment.application_instance_id = 1
        self.segment.ref(self.context_carrier)
        self.segment.service_id = -1
        self.segment.trace_segment_id = -1

    def test_segment(self):
        self.assertIsNotNone(self.context_carrier)
        self.assertEqual(self.segment.application_instance_id, 1)
        self.assertEqual(self.segment.service_id, -1)
        self.assertEqual(self.segment.trace_segment_id, -1)
        self.assertIsNotNone(self.segment.refs[0])

    def test_segment(self):
        entry_span = ContextManager.create_entry_span("/oparetion",None)
        local_span = ContextManager.create_local_span("/local")
        exit_span = ContextManager.create_exit_span("/exit", "172.1.1.1")
        ContextManager.stop_span(exit_span)
        ContextManager.stop_span(local_span)
        ContextManager.stop_span(entry_span)


