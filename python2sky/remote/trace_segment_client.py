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
        self.q = Queue()
        self.server = config.BACKEND_SERVICE
        self.service_id = config.SERVICE_ID
        self.service_instance_id = config.SERVICE_INSTANCE_ID
        self.channel = None
        self.register_stub = None
        self.trace_segment_stub = None
        ListenerManager.add(self)
        self.connect_status = False
        self.connection()
        self.start()

    def run(self):
        while True:
            try:
                if not self.connect_status:
                    self.connection()
                trace_segment = self.q.get()

                def iter_data():
                    for seg in [trace_segment]:
                        yield seg.transform()

                self.trace_segment_stub.collect(iter_data())

            except Exception as e:
                log.exception("Transform and send UpstreamSegment to collector fail.{}.", self.server, e)
                time.sleep(config.REGISTER_INTERVAL)
                self.channel.close()
                self.connection()

    def connection(self):
        try:
            self.channel = grpc.insecure_channel(self.server)
            self.trace_segment_stub = TraceSegmentReportServiceStub(self.channel)
            self.connect_status = True
        except Exception as e:
            self.channel.close()
            self.connect_status = False
            log.exception("Create channel to {} fail.", self.server, e)

    def after_finished(self, trace_segment):
        self.q.put(trace_segment)


__trace_segment_client = TraceSegmentClient()


def get_trace_segment_client():
    return __trace_segment_client


if __name__ == "__main__":
    get_trace_segment_client()
