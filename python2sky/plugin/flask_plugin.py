# -*- coding:utf-8 -*-
# author：huawei
import functools

from python2sky.config import SKYWALKING_HERADER_V2
from python2sky.context.common import set_tag_url, set_tag_method, set_layer_http, set_component, FLASK
from python2sky.context.context_carrier import ContextCarrier
from python2sky.context.context_manager import ContextManager
from python2sky.exception.exceptions import SkywalkingException


def trace_flask_request(f):
    @functools.wraps(f)
    def decorated_function(*args, **kwargs):
        try:
            import flask
        except ImportError:
            return f(*args, **kwargs)
        req = flask.request
        sw6 = req.headers.get(SKYWALKING_HERADER_V2)
        context_carrier = None
        if sw6 and sw6 != "":
            context_carrier = ContextCarrier()
            context_carrier.deserialize(sw6)
        entry_span = ContextManager.create_entry_span(req.path, context_carrier)
        set_tag_url(entry_span, req.url)
        set_tag_method(entry_span, req.method)
        set_layer_http(entry_span)
        set_component(entry_span, FLASK)
        try:
            return f(*args, **kwargs)
        except BaseException as ex:
            entry_span.log(ex)
        finally:
            ContextManager.stop_span(entry_span)

    return decorated_function


def trace_request_started(sender, **extra):
    try:
        import flask
    except ImportError:
        return
    req = flask.request
    sw6 = req.headers.get(SKYWALKING_HERADER_V2)
    context_carrier = None
    if sw6 and sw6 != "":
        context_carrier = ContextCarrier()
        context_carrier.deserialize(sw6)
    entry_span = ContextManager.create_entry_span(req.path, context_carrier)
    set_tag_url(entry_span, req.url)
    set_tag_method(entry_span, req.method)
    set_layer_http(entry_span)
    set_component(entry_span, FLASK)


def trace_request_exception(exception=None):
    try:
        import flask
    except ImportError:
        pass
    try:
        span = ContextManager.active_span()
        if exception is not None:
            span.log(exception)
        ContextManager.stop_span(span)
    except SkywalkingException as ex:
        pass


def flask_install(app):
    try:
        import flask
    except ImportError:
        return
    from flask import request_started
    request_started.connect(trace_request_started, app)
    app.teardown_request(trace_request_exception)
