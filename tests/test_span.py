# -*- coding:utf-8 -*-
# author：huawei
from skywalking.context.context_carrier import ContextCarrier
from skywalking.context.span import Span
from skywalking.exception.exceptions import SkywalkingException
from skywalking.proto.common.trace_common_pb2 import Entry, Unknown
from tests.base_test_case import BaseTestCase


class TestSpan(BaseTestCase):
    def setUp(self):
        self.context_carrier = ContextCarrier()
        self.context_carrier.trace_segment_id = [1, 2, 3]
        self.context_carrier.trace_id = [3, 4, 5]
        self.context_carrier.span_id = 4
        self.context_carrier.entry_service_instance_id = 1
        self.context_carrier.parent_service_instance_id = 1
        self.context_carrier.peer_host = "127.0.0.1:8080"
        self.context_carrier.entry_endpoint_name = "/portal"
        self.context_carrier.parent_endpoint_id = 123

        self.span = Span()
        self.span.operation_name = "operation"
        self.span.log(SkywalkingException("test"))
        self.span.operation_id = 1
        self.span.ref(ContextCarrier)
        self.span.parent_span_id = -1
        self.span.start_time = 11111
        self.span.end_time = 11111
        self.span.span_id = -1
        self.span.tag("test", "test")
        self.span.type = Entry
        self.span.component_id = -1
        self.span.component_name = "test"
        self.span.peer_id = -1
        self.span.peer = "localhost:8888"
        self.span.layer = Unknown

    def test_span(self):
        self.assertEqual(self.span.layer, Unknown, "layer not equal")
        self.assertIsNotNone(self.span.logs[0], "logs not none")
        self.assertEqual(self.span.error_occurred, True, "error not True")
        self.assertEqual(self.span.operation_id, 1, "operation_id not equal")
        self.assertIsNotNone(self.span.refs[0], "refs not equal")
        self.assertEqual(self.span.start_time, 11111, "start_time not equal")
        self.assertEqual(self.span.end_time, 11111, "end_time not equal")
        self.assertEqual(self.span.span_id, -1, "span_id not equal")
        self.assertIsNotNone(self.span.tags[0], "tags not equal")
        self.assertEqual(self.span.type, Entry, "type not equal")
        self.assertEqual(self.span.component_id, -1, "component_id not equal")
        self.assertEqual(self.span.component_name, "test", "component_name not equal")
        self.assertEqual(self.span.peer_id, -1, "peer_id not equal")
        self.assertEqual(self.span.peer, "localhost:8888", "peer not equal")
        self.assertEqual(self.span.layer, Unknown, "layer not equal")

        self.span.start()
        self.span.end()
        self.assertIsNotNone(self.span.start_time)
        self.assertIsNotNone(self.span.end_time)
