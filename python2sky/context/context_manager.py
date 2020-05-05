# -*- coding:utf-8 -*-
# author：huawei
import logging
import threading

from python2sky import config
from python2sky.config import OPERATION_NAME_THRESHOLD
from python2sky.context.trace_context import IgnoredTracerContext, TracingContext
from python2sky.exception.exceptions import SkywalkingException
from python2sky.util import string_util
from python2sky.util.common import null_value

log = logging.Logger(__name__)


class ContextManager:
    CONTEXT = threading.local()

    @classmethod
    def set_tracing_context(cls, tracing_context):
        ContextManager.CONTEXT.trace_context = tracing_context

    @classmethod
    def set_runtime_context(cls, runtime_context):
        ContextManager.CONTEXT.runtime = runtime_context

    @classmethod
    def get_or_create(cls, operation_name, force_sampling):
        if not hasattr(ContextManager.CONTEXT, "trace_context"):
            if not operation_name:
                log.debug("No operation name, ignore this trace.")
                tracing_context = IgnoredTracerContext()
            else:
                if not null_value(config.SERVICE_ID) and not null_value(config.SERVICE_INSTANCE_ID):
                    tracing_context = ContextManager.create_trace_context(operation_name, force_sampling)
                else:
                    log.info("service not register skywalking server!")
                    tracing_context = IgnoredTracerContext()
        else:
            tracing_context = ContextManager.CONTEXT.trace_context
        ContextManager.CONTEXT.trace_context = tracing_context
        return tracing_context

    @classmethod
    def get_global_trace_id(cls):
        tracing_context = ContextManager.get_tracing_context()
        if tracing_context:
            return tracing_context.get_readable_global_trace_id()
        else:
            return "N/A"

    @classmethod
    def create_entry_span(cls, operation_name, context_carrier):
        operation_name = string_util.cut(operation_name, OPERATION_NAME_THRESHOLD)
        tracing_context = ContextManager.get_or_create(operation_name, True)
        entry_span = tracing_context.create_entry_span(operation_name)
        if context_carrier:
            tracing_context.extract(context_carrier)

        return entry_span

    @classmethod
    def create_local_span(cls, operation_name):
        operation_name = string_util.cut(operation_name, OPERATION_NAME_THRESHOLD)
        tracing_context = ContextManager.get_or_create(operation_name, True)
        local_span = tracing_context.create_local_span(operation_name)
        return local_span

    @classmethod
    def create_inject_exit_span(cls, operation_name, remote_peer, context_carrier):
        if not context_carrier:
            raise SkywalkingException("ContextCarrier can't be null.")
        operation_name = string_util.cut(operation_name, OPERATION_NAME_THRESHOLD)
        tracing_context = ContextManager.get_or_create(operation_name, True)
        exit_span = tracing_context.create_exit_span(operation_name, remote_peer)
        tracing_context.inject(context_carrier)
        return exit_span

    @classmethod
    def create_exit_span(cls, operation_name, remote_peer):
        operation_name = string_util.cut(operation_name, OPERATION_NAME_THRESHOLD)
        tracing_context = ContextManager.get_or_create(operation_name, True)
        exit_span = tracing_context.create_exit_span(operation_name, remote_peer)
        return exit_span

    @classmethod
    def inject(cls, context_carrier):
        ContextManager.get_tracing_context().inject(context_carrier)

    @classmethod
    def extract(cls, context_carrier):
        if not context_carrier:
            raise SkywalkingException("ContextCarrier can't be null.")
        ContextManager.get_tracing_context().extract(context_carrier)

    @classmethod
    def capture(cls):
        return ContextManager.get_tracing_context().capture()

    @classmethod
    def continued(cls, snapshot):
        if not snapshot:
            raise SkywalkingException("ContextSnapshot can't be null.")
        ContextManager.get_tracing_context().continued(snapshot)

    @classmethod
    def await_finish_async(cls, span):
        pass

    @classmethod
    def active_span(cls):
        return ContextManager.get_tracing_context().active_span()

    @classmethod
    def stop_active_span(cls):
        tracing_context = ContextManager.get_tracing_context()
        ContextManager.__stop_span(tracing_context.active_span(), tracing_context)

    @classmethod
    def stop_span(cls, span):
        ContextManager.__stop_span(span, ContextManager.get_tracing_context())

    @classmethod
    def __stop_span(cls, span, tracing_context):
        if tracing_context.stop_span(span):
            ContextManager.CONTEXT.__dict__.clear()

    @classmethod
    def get_tracing_context(cls):
        if hasattr(ContextManager.CONTEXT,"trace_context"):
            return ContextManager.CONTEXT.trace_context
        return None

    @classmethod
    def get_run_time_context(cls):
        if hasattr(ContextManager.CONTEXT, "runtime"):
            return ContextManager.CONTEXT.runtime
        return None

    @classmethod
    def create_trace_context(cls, operation_name, force_sampling):
        suffix_idx = operation_name.rfind(".")
        if suffix_idx > -1 and operation_name.rfind(".") in config.IGNORE_SUFFIX:
            context = IgnoredTracerContext()
        else:
            if force_sampling:
                context = TracingContext()
            else:
                context = IgnoredTracerContext()

        return context
