# -*- coding:utf-8 -*-
# author：huawei
import base64
import logging
import threading
import time
from queue import Queue

import grpc

from skywalking import config
from skywalking.context.trace_context import ListenerManager
from skywalking.proto.language_agent_v2.trace_pb2_grpc import TraceSegmentReportServiceStub

INTERVAL = 30
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

    # def iter_queue(self):
    #     sentinel = object()
    #     for trace_segment in iter(self.queue.get, sentinel):
    #         yield trace_segment.transform()

    def run(self):
        while True:
            try:
                if not self.connect_status:
                    self.connection()
                trace_segment = self.q.get()

                def iter_data():
                    for seg in [trace_segment]:
                        yield seg.transform()

                response = self.trace_segment_stub.collect(iter_data())
                print(response)
            except Exception as e:
                log.exception("Transform and send UpstreamSegment to collector fail.{}.", self.server, e)
                time.sleep(INTERVAL)
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
