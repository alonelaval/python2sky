# -*- coding:utf-8 -*-
# author：huawei
import logging
import threading
import time
from queue import Queue

import grpc

from python2sky import config
from python2sky.context.trace_context import ListenerManager
from python2sky.proto.language_agent_v2.trace_pb2_grpc import TraceSegmentReportServiceStub

log = logging.getLogger(__name__)


class TraceSegmentClient(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.__finished = threading.Event()
        self.q = Queue()
        self.server = config.BACKEND_SERVICE
        self.service_id = config.SERVICE_ID
        self.service_instance_id = config.SERVICE_INSTANCE_ID
        self.channel = None
        self.register_stub = None
        self.trace_segment_stub = None
        ListenerManager.add(self)
        self.state = ""
        self.connection()
        self.start()

    def run(self):
        while not self.__finished.is_set():
            try:
                if not self.connected():
                    self.connection()

                def iter_data():
                    trace_segment = self.q.get()
                    yield trace_segment.transform()
                    self.q.task_done()

                self.trace_segment_stub.collect(iter_data())

            except Exception as e:
                log.error("Transform and send UpstreamSegment to collector fail.%s." % self.server)
                self.__finished.wait(config.REGISTER_INTERVAL)
                self.channel.close()
                self.connection()

    def connection(self):
        try:
            self.channel = grpc.insecure_channel(self.server)
            self.trace_segment_stub = TraceSegmentReportServiceStub(self.channel)
            self.state = grpc.ChannelConnectivity.READY
        except Exception as e:
            self.channel.close()
            self.state = grpc.ChannelConnectivity.SHUTDOWN
            log.error("Create channel to %s fail." % self.server)

    def after_finished(self, trace_segment):
        self.q.put(trace_segment)

    def connected(self):
        return self.state == grpc.ChannelConnectivity.READY


__trace_segment_client = TraceSegmentClient()


def get_trace_segment_client():
    return __trace_segment_client


if __name__ == "__main__":
    get_trace_segment_client()
