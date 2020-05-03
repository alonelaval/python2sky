# -*- coding:utf-8 -*-
# author：huawei
from skywalking import config
from skywalking.util.date_util import current_milli_time
from skywalking.util.uuid_util import global_id_generator


class TraceSegment:
    def __init__(self):
        self.application_instance_id = config.SERVICE_INSTANCE_ID
        self.service_id = config.SERVICE_ID
        self.trace_segment_id = global_id_generator(self.application_instance_id)
        self.refs = []
        self.spans = []
        self.create_time = current_milli_time()
        self.id = global_id_generator(self.application_instance_id)
        self.trace_ids = [id]

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
