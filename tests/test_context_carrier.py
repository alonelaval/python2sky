# -*- coding:utf-8 -*-
# author：huawei
import unittest

from skywalking.context import context_carrier
from skywalking.context.context_carrier import ContextCarrier

SW6 = "1-My40LjU=-MS4yLjM=-4-1-1-IzEyNy4wLjAuMTo4MDgw-Iy9wb3J0YWw=-MTIz"


class TestContextCarrier(unittest.TestCase):
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

    def test_serialize(self):
        self.assertEqual(SW6, context_carrier.serialize())

    def test_deserialize(self):
        text = SW6
        context = ContextCarrier()
        context.deserialize(text)
        self.assertEqual(context.peer_host, self.context_carrier.peer_host)
