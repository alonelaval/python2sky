# -*- coding:utf-8 -*-
# author：huawei
import traceback

from python2sky.proto.common.trace_common_pb2 import Entry, Exit
from python2sky.util.common import build_key_value, null_value
from python2sky.proto.language_agent_v2.trace_pb2 import Log, SpanObjectV2
from python2sky.util.date_util import current_milli_time
from python2sky.util.string_util import is_empty



class Span:
    def __init__(self):
        self.span_id = -1
        self.parent_span_id = None
        self.tags = None
        self.operation_name = None
        self.operation_id = None
        self.logs = None
        self.start_time = None
        self.end_time = None
        self.error_occurred = False
        self.component_id = 0
        self.component_name = ""
        self.refs = None
        self.type = None
        self.layer = None
        self.peer = None
        self.peer_id = None
        self.error_occurred = False

    def is_entry(self):
        return self.type == Entry

    def is_exit(self):
        return self.type == Exit

    def tag(self, key, value):
        if not self.tags:
            self.tags = []
        self.tags.append(build_key_value(key, value))
        return self

    def start(self):
        self.start_time = current_milli_time()
        return self

    def end(self):
        self.end_time = current_milli_time()
        return self

    def ref(self, context_carrier):
        if not self.refs:
            self.refs = []
        if context_carrier not in self.refs:
            self.refs.append(context_carrier)

    def log(self, ex):
        if not self.logs:
            self.logs = []
        self.error_occurred = True
        log = Log()
        log.time = current_milli_time()
        log.data.append(build_key_value("event", "error"))
        log.data.append(build_key_value("error.kind", type(ex)))
        log.data.append(build_key_value("message", str(ex)))
        log.data.append(build_key_value("stack", traceback.format_exc()))
        self.logs.append(log)
        return self

    def transform(self):
        span_object_v2 = SpanObjectV2()
        span_object_v2.spanId = self.span_id
        span_object_v2.parentSpanId = self.parent_span_id
        span_object_v2.startTime = self.start_time
        span_object_v2.endTime = self.end_time
        if not null_value(self.operation_id):
            span_object_v2.operationNameId = self.operation_id
        else:
            span_object_v2.operationName = self.operation_name

        span_object_v2.spanType = self.type

        if self.layer is not None:
            span_object_v2.spanLayer = self.layer

        if not null_value(self.component_id):
            span_object_v2.componentId = self.component_id
        else:
            if not is_empty(self.component_name):
                span_object_v2.component = self.component_name

        span_object_v2.isError = self.error_occurred

        if self.tags:
            for tag in self.tags:
                span_object_v2.tags.append(tag)

        if self.logs:
            for log in self.logs:
                span_object_v2.logs.append(log)

        if self.refs:
            for ref in self.refs:
                span_object_v2.refs.append(ref.transform())

        if not null_value(self.peer_id):
            span_object_v2.peerId = self.peer_id
        else:
            if not is_empty(self.peer):
                span_object_v2.peer = self.peer

        return span_object_v2
