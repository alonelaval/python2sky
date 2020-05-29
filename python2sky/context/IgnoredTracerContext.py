# -*- coding:utf-8 -*-
# author：huawei
import threading

from python2sky.context.context_carrier import ContextCarrier
from python2sky.context.noop_span import NoopSpan
from python2sky.context.trace_context import AbstractTracerContext


class IgnoredTracerContext(AbstractTracerContext):
    __noop_span = NoopSpan()

    def __init__(self):
        self.stack_depth = 0

    def inject(self, context_carrier):
        pass

    def extract(self, context_carrier):
        pass

    def capture(self):
        return ContextCarrier()

    def continued(self, snapshot):
        pass

    def get_readable_global_trace_id(self):
        return "[Ignored Trace]"

    def create_entry_span(self, operation_name):
        self.stack_depth += 1
        return IgnoredTracerContext.__noop_span

    def create_local_span(self, operation_name):
        self.stack_depth += 1
        return IgnoredTracerContext.__noop_span

    def create_exit_span(self, operation_name, remote_peer):
        self.stack_depth += 1
        return IgnoredTracerContext.__noop_span

    def active_span(self):
        return IgnoredTracerContext.__noop_span

    def stop_span(self, span):
        self.stack_depth -= 1
        if self.stack_depth == 0:
            IgnoredListenerManager.notify_finish(self)

    def await_finish_async(self):
        pass

    def async_stop(self):
        pass


class IgnoredListenerManager:
    __LISTENERS = []
    __lock = threading.Lock()

    @classmethod
    def notify_finish(cls, ignoredTracerContext):
        for listener in IgnoredListenerManager.__LISTENERS:
            listener.after_finished(ignoredTracerContext)

    @classmethod
    def add(cls, listener):
        with IgnoredListenerManager.__lock:
            IgnoredListenerManager.__LISTENERS.append(listener)

    @classmethod
    def remove(cls, listener):
        with IgnoredListenerManager.__lock:
            IgnoredListenerManager.__LISTENERS.remove(listener)
