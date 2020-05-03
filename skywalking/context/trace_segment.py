# -*- coding:utf-8 -*-
# author：huawei
from skywalking.util.date_util import current_milli_time


class TraceSegment:
    def __init__(self):
        self.trace_segment_id = None
        self.refs = []
        self.spans = []
        self.create_time = current_milli_time()
        self.trace_ids = []

    def ref(self, context_carrier):
        if context_carrier not in self.refs:
            self.refs.append(context_carrier)

    def related_global_traces(self, trace_id):
        self.trace_ids.append(trace_id)

    def archive(self, span):
        span.end()
        self.spans.append(span)
