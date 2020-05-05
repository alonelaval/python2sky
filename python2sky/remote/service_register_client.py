# -*- coding:utf-8 -*-
# author：huawei
import threading
import time
import grpc

from python2sky import config
from python2sky.proto.register.InstancePing_pb2 import ServiceInstancePingPkg
from python2sky.proto.register.InstancePing_pb2_grpc import ServiceInstancePingStub
from python2sky.proto.register.Register_pb2 import Service, Services, ServiceInstance, ServiceInstances
from python2sky.proto.register.Register_pb2_grpc import RegisterStub
from python2sky.util.date_util import current_milli_time
from python2sky.util.os_util import get_os_name, get_all_ipv4, get_host_name, get_process_no
from python2sky.util.uuid_util import get_uuid
from python2sky.util.common import build_key_value
import logging


log = logging.getLogger(__name__)


class RegisterClient(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

        self.service_name = config.SERVICE_NAME
        self.agent_version = config.AGENT_VERSION
        self.server = config.BACKEND_SERVICE
        self.service_id = None
        self.service_instance_id = None
        self.uuid = get_uuid()
        self.channel = None
        self.register_stub = None
        self.ping_stub = None
        self.connection()
        self.start()

    def run(self):
        while True:
            try:
                if not self.service_id:
                    service_register_mapping = self.register_service()
                    self.set_service_id(service_register_mapping)
                elif not self.service_instance_id:
                    service_instance_register_mapping = self.register_instance(self.service_id, self.uuid)
                    self.set_service_instance_id(service_instance_register_mapping)
                else:
                    self.instance_ping(self.service_instance_id, self.uuid)
                time.sleep(config.REGISTER_INTERVAL)
            except Exception as e:
                log.exception("register execute fail will be Selected collector grpc service running, reconnect:{}."
                              , self.server, e)
                time.sleep(config.REGISTER_INTERVAL)
                self.connection()

    def connection(self):
        try:

            self.channel = grpc.insecure_channel(self.server)
            self.register_stub = RegisterStub(self.channel)
            self.ping_stub = ServiceInstancePingStub(self.channel)
        except Exception as e:
            log.exception("Create channel to {} fail.", self.server, e)

    def set_service_instance_id(self, service_instance_register_mapping):
        if service_instance_register_mapping and len(service_instance_register_mapping.serviceInstances) > 0:
            self.service_instance_id = service_instance_register_mapping.serviceInstances[0].value
            config.SERVICE_INSTANCE_ID = self.service_instance_id

    def set_service_id(self, service_register_mapping):
        if service_register_mapping and len(service_register_mapping.services) > 0:
            self.service_id = service_register_mapping.services[0].value
            config.SERVICE_ID = self.service_id

    def register_service(self):
        service = Service()
        service.serviceName = self.service_name
        services = Services()
        services.services.append(service)
        return self.register_stub.doServiceRegister(services)

    def register_instance(self, service_id, instance_uuid):
        service_instance = ServiceInstance()
        service_instance.serviceId = service_id
        service_instance.instanceUUID = instance_uuid
        service_instance.time = current_milli_time()

        service_instance.properties.append(build_key_value("os_name", get_os_name()))
        service_instance.properties.append(build_key_value("host_name", get_host_name()))
        ipv4s = get_all_ipv4()
        for v in ipv4s:
            service_instance.properties.append(build_key_value("ipv4", v))

        service_instance.properties.append(build_key_value("process_no", get_process_no()))
        service_instance.properties.append(build_key_value("language", "python"))

        service_instances = ServiceInstances()
        service_instances.instances.append(service_instance)
        return self.register_stub.doServiceInstanceRegister(service_instances)

    def instance_ping(self, instance_id, instance_uuid):
        ping = ServiceInstancePingPkg()
        ping.serviceInstanceId = instance_id
        ping.time = current_milli_time()
        ping.serviceInstanceUUID = instance_uuid
        return self.ping_stub.doPing(ping)


__register = RegisterClient()


def get_service_register():
    return __register


if __name__ == "__main__":
    register = RegisterClient()
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
