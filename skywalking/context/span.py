# -*- coding:utf-8 -*-
# author：huawei
import traceback

from skywalking.proto.common.trace_common_pb2 import Entry, Exit
from skywalking.util.common import build_key_value
from skywalking.proto.language_agent_v2.trace_pb2 import Log
from skywalking.util.date_util import current_milli_time


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
        self.component_name = None
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
