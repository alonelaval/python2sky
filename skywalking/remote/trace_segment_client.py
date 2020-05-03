# -*- coding:utf-8 -*-
# author：huawei
import threading
import time
import grpc
from skywalking.proto.common.common_pb2 import KeyStringValuePair
from skywalking.proto.register.InstancePing_pb2 import ServiceInstancePingPkg
from skywalking.proto.register.InstancePing_pb2_grpc import ServiceInstancePingStub
from skywalking.proto.register.Register_pb2 import Service, Services, ServiceInstance, ServiceInstances
from skywalking.proto.register.Register_pb2_grpc import RegisterStub
from skywalking.util.date_util import current_milli_time
from skywalking.util.os_util import get_os_name, get_all_ipv4, get_host_name, get_process_no
from skywalking.util.uuid_util import get_uuid
import logging

INTERVAL = 30

class TraceSegmentClient(threading.Thread):
    pass




if __name__ == "__main__":
    pass
    # register = RegisterClient("127.0.0.1", "11800", "huawei", "v1")
    # register.start()
    # serviceRegisterMapping = register_service()
    # service_id = serviceRegisterMapping.services[0].value
    # uuid = get_uuid()
    # serviceInstanceRegisterMapping = register_instance(service_id, uuid)
    # print(serviceRegisterMapping)
    # print(serviceInstanceRegisterMapping.serviceInstances)
    # serviceInstanceRegisterMapping = register_instance(service_id, uuid)
    # serviceInstanceRegisterMapping = register_instance(service_id, uuid)
    # serviceInstanceRegisterMapping = register_instance(service_id, uuid)
    # print(serviceInstanceRegisterMapping.serviceInstances)
