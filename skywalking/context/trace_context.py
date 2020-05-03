# -*- coding:utf-8 -*-
# author：huawei
from skywalking.context.noop_span import NoopSpan
from skywalking.context.span import Span
from skywalking.context.trace_segment import TraceSegment
from skywalking.exception.exceptions import SkywalkingException
from skywalking.proto.common.trace_common_pb2 import Entry, Local, Exit
from skywalking.util.uuid_util import global_id_to_string

INEXISTENCE = -1

from abc import ABC


class AbstractTracerContext(ABC):
    def inject(self, context_carrier):
        pass

    def extract(self, context_carrier):
        pass

    def capture(self):
        pass

    def continued(self, snapshot):
        pass

    def get_readable_global_trace_id(self):
        pass

    def create_entry_span(self, operation_name):
        pass

    def create_local_span(self, operation_name):
        pass

    def create_exit_span(self, operation_name, remote_peer):
        pass

    def active_span(self):
        pass

    def stop_span(self):
        pass

    def await_finish_async(self):
        pass

    def async_stop(self):
        pass


class TracingContext(AbstractTracerContext):
    def __init__(self):
        self.segment = TraceSegment()
        self.spans = []
        self.span_id_generator = 0

    def inject(self, context_carrier):
        span = self.active_span()
        if span.is_exit():
            raise SkywalkingException("Inject can be done only in Exit Span")
        context_carrier.peer = span.peer
        context_carrier.trace_segment_id = self.segment.trace_segment_id
        context_carrier.span_id = span.span_id
        context_carrier.parent_service_instance_id = self.segment.application_instance_id

        first_span = self.first()

        if self.segment.refs and len(self.segment.refs) > 0:
            ref = self.segment.refs[0]
            operation_id = ref.entry_endpoint_id
            operation_name = ref.entry_endpoint_name
            entry_service_instance_id = ref.entry_service_instance_id
        else:
            if first_span.is_entry():
                operation_id = first_span.operation_id
                operation_name = first_span.operation_name
            entry_service_instance_id = self.segment.application_instance_id

        context_carrier.entry_service_instance_id = entry_service_instance_id

        parent_operation_id = first_span.operation_id

        if parent_operation_id == 0:
            if operation_name:
                context_carrier.entry_endpoint_name = operation_name
            else:
                context_carrier.entry_endpoint_id = INEXISTENCE
        else:
            context_carrier.entry_endpoint_id = operation_id

        context_carrier.trace_id = self.segment.trace_ids[0]

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

    def get_readable_global_trace_id(self):
        return global_id_to_string(self.segment.get_related_global_traces()[0])

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
            entry_span = self.__create_span(operation_name, Entry, parent_span_id)

        return self.push(entry_span)

    def create_local_span(self, operation_name):
        if self.is_limit_mechanism_working():
            noopSpan = NoopSpan()
            self.spans.append(noopSpan)
            return noopSpan

        parent_span = self.peek()
        parent_span_id = parent_span.span_id if parent_span else -1
        local_span = self.__create_span(operation_name, Local, parent_span_id)

        return self.push(local_span)

    def create_exit_span(self, operation_name, remote_peer):
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
            exit_span = self.__create_span(operation_name, Exit, parent_span_id)
            exit_span.peer = remote_peer

        return self.push(exit_span)

    def __create_span(self, operation_name, span_type, parent_span_id):
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
            return self.spans[len(self.spans) - 1]
        return None

    def first(self):
        if self.spans:
            return self.spans[0]
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
        self.finish()
        return len(self.spans) == 0

    def finish(self):
        if len(self.spans) == 0:
            pass

        print("not finish!")





class IgnoredTracerContext(AbstractTracerContext):
    pass
