# -*- coding:utf-8 -*-
# author：huawei
import time

from python2sky import config
from python2sky.context.context_carrier import ContextCarrier
from python2sky.context.context_manager import ContextManager
from python2sky.remote.service_register_client import get_service_register
from python2sky.remote.trace_segment_client import get_trace_segment_client
from python2sky.util.uuid_util import global_id_to_string
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

