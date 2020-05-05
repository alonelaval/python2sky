# -*- coding:utf-8 -*-
# author：huawei
from threading import Thread

import requests
from flask import Flask, request

from python2sky.bootstrap import skywalking_boot
from python2sky.context.common import set_tag_url, set_tag_method, set_tag_status_code, set_layer_http, FLASK, \
    set_component, REQUESTS

skywalking_boot()

from python2sky.context.context_carrier import ContextCarrier
from python2sky.context.context_manager import ContextManager

app = Flask(__name__)


@app.route('/flask/test')
def hello_world():
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

    entry_span = ContextManager.create_entry_span(req.path, context_carrier)
    set_tag_url(entry_span, request.url)
    set_tag_method(entry_span, req.method)
    set_tag_status_code(entry_span, 200)
    set_layer_http(entry_span)
    set_component(entry_span, FLASK)

    exit_url = "http://localhost:8088/project/b"
    exit_carrier = ContextCarrier()
    exit_span = ContextManager.create_inject_exit_span("/project/b", exit_url, exit_carrier)
    set_layer_http(exit_span)
    set_component(exit_span, REQUESTS)
    data = requests.get("http://localhost:8088/project/b", headers={"sw6": exit_carrier.serialize()})
    set_tag_status_code(exit_span, data.status_code)

    ContextManager.stop_span(exit_span)
    ContextManager.stop_span(entry_span)
    return 'cross_process'


@app.route('/flask/cross_thread')
def cross_thread():
    req = request
    entry_span = ContextManager.create_entry_span(req.path, None)
    set_tag_url(entry_span, request.url)
    set_tag_method(entry_span, req.method)
    set_tag_status_code(entry_span, 200)
    set_layer_http(entry_span)
    set_component(entry_span, FLASK)

    exit_url = "http://localhost:8088/project/b"
    snapshot = ContextManager.capture()

    def local_thread():
        local_span = ContextManager.create_local_span("/flask/cross_thread/local")
        ContextManager.continued(snapshot)
        ContextManager.stop_span(local_span)

    def exit_thread():
        exit_carrier = ContextCarrier()
        exit_span = ContextManager.create_exit_span("/flask/cross_thread/exit", exit_url)
        ContextManager.continued(snapshot)
        set_layer_http(exit_span)
        set_component(exit_span, REQUESTS)
        ContextManager.inject(exit_carrier)
        data = requests.get("http://localhost:8088/project/b", headers={"sw6": exit_carrier.serialize()})
        set_tag_status_code(exit_span, data.status_code)
        ContextManager.stop_span(exit_span)

    t1 = Thread(target=local_thread, args=())
    t2 = Thread(target=exit_thread, args=())
    t1.start()
    t2.start()

    ContextManager.stop_span(entry_span)
    return 'cross_thread'


app.run()
