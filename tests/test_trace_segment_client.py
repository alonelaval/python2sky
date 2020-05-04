# -*- coding:utf-8 -*-
# author：huawei
import time

from skywalking import config
from skywalking.context.context_carrier import ContextCarrier
from skywalking.context.context_manager import ContextManager
from skywalking.remote.service_register_client import get_service_register
from skywalking.remote.trace_segment_client import get_trace_segment_client
from skywalking.util.uuid_util import global_id_to_string
from tests.base_test_case import BaseTestCase


class Trace_segment_client(BaseTestCase):

    def test_send(self):
        # get_service_register()
        # time.sleep(10)
        get_trace_segment_client()
        # time.sleep(0)
        # carrier = ContextCarrier()
        # carrier.deserialize(self.SW6)
        config.SERVICE_ID = 3
        config.SERVICE_INSTANCE_ID = 53
        entry_span = ContextManager.create_entry_span("/operation", None)
        # local_span = ContextManager.create_local_span("/local")
        # carrier2 = ContextCarrier()
        # exit_span = ContextManager.create_inject_exit_span("/exit", "172.1.1.1:8080", carrier2)
        # sw6 = carrier.serialize()
        # self.assertEqual(sw6, carrier.serialize())
        # self.assertEqual(ContextManager.get_global_trace_id(), global_id_to_string(["3", "4", "5"]))
        # ContextManager.stop_span(exit_span)
        # ContextManager.stop_span(local_span)
        ContextManager.stop_span(entry_span)

