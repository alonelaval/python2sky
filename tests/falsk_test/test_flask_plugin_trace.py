# -*- coding:utf-8 -*-
# author：huawei
import requests
from flask import Flask, request

from python2sky import config
from python2sky.bootstrap import skywalking_boot
from python2sky.config import SKYWALKING_HERADER_V2
from python2sky.context.common import set_layer_http, set_component, REQUESTS, set_tag_status_code
from python2sky.context.context_carrier import ContextCarrier

from python2sky.plugin.flask_plugin import trace_flask_request

config.SERVICE_NAME= "flask_test_trace"
skywalking_boot()

from python2sky.context.context_manager import ContextManager

app = Flask(__name__)


@app.route('/flask/test')
@trace_flask_request
def hello_world():
    exit_url = "www.google.com"
    local_span = ContextManager.create_local_span("/locahost_span")
    exit_span = ContextManager.create_exit_span("/exit_span", exit_url)
    ContextManager.stop_span(exit_span)
    ContextManager.stop_span(local_span)
    return 'Hello, World!'


@app.route('/flask/cross_process')
@trace_flask_request
def cross_process():
    exit_url = "http://localhost:8088/project/b"
    exit_carrier = ContextCarrier()
    exit_span = ContextManager.create_inject_exit_span("/project/b", exit_url, exit_carrier)
    set_layer_http(exit_span)
    set_component(exit_span, REQUESTS)
    data = requests.get("http://localhost:8088/project/b", headers={SKYWALKING_HERADER_V2: exit_carrier.serialize()})
    set_tag_status_code(exit_span, data.status_code)

    ContextManager.stop_span(exit_span)
    return 'cross_process'


@app.route('/flask/cross_thread')
@trace_flask_request
def cross_thread():
    return 'cross_thread'



app.run()
