# -*- coding:utf-8 -*-
# author：huawei
from python2sky import config
from python2sky.proto.common.trace_common_pb2 import UpstreamSegment
from python2sky.proto.language_agent_v2.trace_pb2 import SegmentObject
from python2sky.util.common import build_unique_id
from python2sky.util.date_util import current_milli_time
from python2sky.util.uuid_util import global_id_generator


class TraceSegment:
    def __init__(self):
        self.application_instance_id = config.SERVICE_INSTANCE_ID
        self.service_id = config.SERVICE_ID
        self.trace_segment_id = global_id_generator(self.application_instance_id)
        self.refs = []
        self.spans = []
        self.create_time = current_milli_time()
        self.id = global_id_generator(self.application_instance_id)
        self.trace_ids = [self.id]
        self.is_size_limited = False

    def ref(self, context_carrier):
        if context_carrier not in self.refs:
            self.refs.append(context_carrier)

    def related_global_traces(self, trace_id):
        if len(self.trace_ids) > 0 and self.id == self.trace_ids[0]:
            self.trace_ids.remove(self.id)

        if trace_id not in self.trace_ids:
            self.trace_ids.append(trace_id)

    def get_related_global_traces(self):
        return self.trace_ids

    def archive(self, span):
        span.end()
        self.spans.append(span)

    def transform(self):
        upstream_segment = UpstreamSegment()

        for trace_id in self.trace_ids:
            upstream_segment.globalTraceIds.append(build_unique_id(trace_id))

        segment_obj = SegmentObject()
        segment_obj.traceSegmentId.CopyFrom(build_unique_id(self.trace_segment_id))
        for span in self.spans:
            segment_obj.spans.append(span.transform())

        segment_obj.serviceId = self.service_id
        segment_obj.serviceInstanceId = self.application_instance_id
        segment_obj.isSizeLimited = self.is_size_limited

        upstream_segment.segment = segment_obj.SerializeToString()

        return upstream_segment
