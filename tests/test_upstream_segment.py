# -*- coding:utf-8 -*-
# author：huawei
import base64

import grpc

from python2sky.proto.common.trace_common_pb2 import UpstreamSegment
from python2sky.proto.language_agent_v2.trace_pb2 import SegmentObject
from python2sky.proto.language_agent_v2.trace_pb2_grpc import TraceSegmentReportServiceStub
from tests.base_test_case import BaseTestCase


class Trace_segment_client(BaseTestCase):
    def test(self):

        py = "ChEKDy7e5MGeni75mdHzr5qcHBLMAQoRCg8u3+TBnp4unobR86+anBwSsgEQ////////////ARjf5MGeni4g+eTBnp4uKkEIARIRCg8u3uTBnp4utqXQ86+anBw4LkITL2ZsYXNrL2Nyb3NzX3RocmVhZFITL2ZsYXNrL2Nyb3NzX3RocmVhZDoYL2ZsYXNrL2Nyb3NzX3RocmVhZC9leGl0Sh9odHRwOi8vbG9jYWxob3N0OjgwODgvcHJvamVjdC9iUAFYA2DyLnoSCgtzdGF0dXNfY29kZRIDMjAwGAMgLg=="

        java = "CgwKCiA8k9qD3eKFnBwSbwoMCgogPJLag93ihZwcElsQ////////////ARjhhOH8nS4g44Th/J0uMARYA2AOeiYKA3VybBIfaHR0cDovLzEyNy4wLjAuMTo4MDg4L3Byb2plY3QvYnoSCgtodHRwLm1ldGhvZBIDR0VUGAUgIA=="
        py_up_seg = UpstreamSegment()
        py_up_seg.ParseFromString(base64.b64decode(py))
        py_segment = SegmentObject()
        py_segment.ParseFromString(py_up_seg.segment)

        java_up_seg = UpstreamSegment()
        java_up_seg.ParseFromString(base64.b64decode(java))
        java_segment = SegmentObject()
        java_segment.ParseFromString(java_up_seg.segment)

        # client = get_trace_segment_client()
        # client.after_finished(java_up_seg)

        # def stream():
        #     for i in [java_up_seg,py_up_seg]:
        #         yield i
        #
        # result = self.__test2(stream())
        # print(result.__next__())

        # trace_segment_stub.collect(java_up_seg, timeout=1000)

        print(py_up_seg)
        print("------------------------------------------")
        print(java_up_seg)
        print("------------------------------------------")
        print(py_segment)
        print("------------------------------------------")
        print(java_segment)

    def __test2(self, up_seg):
        channel = grpc.insecure_channel("127.0.0.1:11800")
        trace_segment_stub = TraceSegmentReportServiceStub(channel)
        feature_future = trace_segment_stub.collect(up_seg, timeout=199)
        yield feature_future


    def __test(self, up_seg):
        channel = grpc.insecure_channel("127.0.0.1:11800")
        trace_segment_stub = TraceSegmentReportServiceStub(channel)
        feature_future = trace_segment_stub.collect.future(up_seg, timeout=199)

        yield feature_future.result()
