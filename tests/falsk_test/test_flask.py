# -*- coding:utf-8 -*-
# author：huawei
import requests
from flask import Flask, request

from skywalking.bootstrap import skywalking_boot
from skywalking.context.common import set_tag_url, set_tag_method, set_tag_status_code, set_layer_http, FLASK, \
    set_component

skywalking_boot()

from skywalking.context.context_carrier import ContextCarrier
from skywalking.context.context_manager import ContextManager

app = Flask(__name__)


@app.route('/flask/test')
def hello_world():
    sw6 = request.headers.get("sw6")
    req = request
    entry_span = ContextManager.create_entry_span(request.path, None)
    set_tag_url(entry_span, request.url)
    set_tag_method(entry_span, req.method)
    set_tag_status_code(entry_span, 200)
    set_layer_http(entry_span)
    set_component(entry_span, FLASK)
    exit_url = "www.google.com"
    local_span = ContextManager.create_local_span("/locahost_span")
    exit_span = ContextManager.create_exit_span("/exit_span", exit_url)
    ContextManager.stop_span(exit_span)
    ContextManager.stop_span(local_span)
    ContextManager.stop_span(entry_span)
    return 'Hello, World!'

@app.route('/flask/cross_process')
def cross_process():
    sw6 = request.headers.get("sw6")
    req = request
    context_carrier = None
    if sw6 and sw6 != "":
        context_carrier = ContextCarrier()
        context_carrier.deserialize(sw6)

    entry_span = ContextManager.create_entry_span("/", None)
    set_tag_url(entry_span, request.url)
    set_tag_method(entry_span, req.method)
    set_tag_status_code(entry_span, 200)
    set_layer_http(entry_span)
    set_component(entry_span, FLASK)

    exit_url = "localhost:8088"
    exit_carrier = ContextCarrier()
    exit_span = ContextManager.create_inject_exit_span("/project/b", exit_url, exit_carrier)

    requests.get("http://localhost:8088/project/b", headers={"sw6": exit_carrier.serialize()})

    ContextManager.stop_span(exit_span)
    ContextManager.stop_span(entry_span)
    return 'cross_process'




app.run()
