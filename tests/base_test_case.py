# -*- coding:utf-8 -*-
# author：huawei
import logging
import unittest

from python2sky.context.context_carrier import ContextCarrier

LOG_FORMAT = "%(asctime)s - %(levelname)s - %(filename)s[:%(lineno)d] - %(message)s"
logging.basicConfig( level=logging.DEBUG, format=LOG_FORMAT)


class BaseTestCase(unittest.TestCase):
    def setUp(self):
        self.SW6 = "1-My40LjU=-MS4yLjM=-4-1-1-IzEyNy4wLjAuMTo4MDgw-Iy9wb3J0YWw=-MTIz"
        self.context_carrier = ContextCarrier()
        self.context_carrier.trace_segment_id = [1, 2, 3]
        self.context_carrier.trace_id = [3, 4, 5]
        self.context_carrier.span_id = 4
        self.context_carrier.entry_service_instance_id = 1
        self.context_carrier.parent_service_instance_id = 1
        self.context_carrier.peer = "127.0.0.1:8080"
        self.context_carrier.entry_endpoint_name = "/portal"
        self.context_carrier.parent_endpoint_id = 123

    def tearDown(self):
        pass