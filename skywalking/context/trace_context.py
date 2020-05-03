# -*- coding:utf-8 -*-
# author：huawei
from skywalking.context.noop_span import NoopSpan
from skywalking.context.span import Span
from skywalking.context.trace_segment import TraceSegment
from skywalking.exception.exceptions import SkywalkingException
from skywalking.proto.common.trace_common_pb2 import Entry, Local, Exit


class TracingContext:
    def __init__(self):
        self.segment = TraceSegment()
        self.spans = []
        self.span_id_generator = 0

    def inject(self, context_carrier):
        span = self.active_span()
        if span.is_exit():
            raise SkywalkingException("Inject can be done only in Exit Span")

    def extract(self, context_carrier):
        self.segment.ref(context_carrier)
        self.segment.related_global_traces(context_carrier.trace_id)
        span = self.active_span()
        if span.is_entry():
            span.ref(context_carrier)

    def capture(self):
        pass
    def continued(self):
        pass

    def create_entry_span(self, operation_name):
        if self.is_limit_mechanism_working():
            noopSpan = NoopSpan()
            self.spans.append(noopSpan)
            return noopSpan

        parent_span = self.peek()
        parent_span_id = parent_span.span_id if parent_span else -1

        if parent_span and parent_span.is_entry():
            parent_span.operation_name = operation_name
            entry_span = parent_span
            return entry_span.start()
        else:
            entry_span = self.create_span(operation_name, Entry, parent_span_id)

        return self.push(entry_span)

    def create_local_span(self, operation_name):
        if self.is_limit_mechanism_working():
            noopSpan = NoopSpan()
            self.spans.append(noopSpan)
            return noopSpan

        parent_span = self.peek()
        parent_span_id = parent_span.span_id if parent_span else -1
        entry_span = self.create_span(operation_name, Local, parent_span_id)

        return self.push(entry_span)

    def create_exit_span(self, operation_name):
        if self.is_limit_mechanism_working():
            noopSpan = NoopSpan()
            self.spans.append(noopSpan)
            return noopSpan

        parent_span = self.peek()
        parent_span_id = parent_span.span_id if parent_span else -1

        if parent_span and parent_span.is_exit():
            parent_span.operation_name = operation_name
            exit_span = parent_span
            return exit_span.start()
        else:
            exit_span = self.create_span(operation_name, Exit, parent_span_id)
        return self.push(exit_span)

    def create_span(self, operation_name, span_type, parent_span_id):
        span = Span()
        self.span_id_generator += 1
        span.span_id = self.span_id_generator
        span.parent_span_id = parent_span_id
        span.operation_name = operation_name
        span.type = span_type

        return span.start()

    def push(self, span):
        self.spans.append(span)
        return span

    def active_span(self):
        span = self.peek()
        if not span:
            raise SkywalkingException("No active span.")

    def peek(self):
        if self.spans:
            return self.spans.index(len(self.spans) - 1)
        return None

    def is_limit_mechanism_working(self):
        return False

    def stop_span(self, span):
        last_span = self.active_span()
        if span == last_span:
            if type(last_span) != NoopSpan:
                self.segment.archive(span)
            self.spans.pop()

        else:
            raise SkywalkingException("Stopping the unexpected span = " + span)

        return len(self.spans) == 0

    def finish(self):
        if len(self.spans) == 0:
            pass
