# -*- coding:utf-8 -*-
# author：huawei
import requests
from flask import Flask, request, request_finished, config

from python2sky.bootstrap import skywalking_boot

from flask import request_started

from python2sky.config import SKYWALKING_HERADER_V2
from python2sky.context.common import set_layer_http, set_component, REQUESTS, set_tag_status_code
from python2sky.context.context_carrier import ContextCarrier
from python2sky.context.context_manager import ContextManager
from python2sky.plugin.flask_plugin import trace_request_started, trace_request_finished
config.SERVICE_NAME= "flask_test_trace"
skywalking_boot()

app = Flask(__name__)


@app.route("/test")
def test():
    return "test"


@app.route('/flask/test')
def hello_world():
    return 'Hello, World!'


@app.route('/flask/cross_process')
def cross_process():
    exit_url = "http://localhost:8088/project/b"
    exit_carrier = ContextCarrier()
    exit_span = ContextManager.create_inject_exit_span("/project/b", exit_url, exit_carrier)
    set_layer_http(exit_span)
    set_component(exit_span, REQUESTS)
    data = requests.get("http://localhost:8088/project/b", headers={SKYWALKING_HERADER_V2: exit_carrier.serialize()})
    set_tag_status_code(exit_span, data.status_code)

    ContextManager.stop_span(exit_span)
    return "cross_process"


request_started.connect(trace_request_started, app)
request_finished.connect(trace_request_finished, app)

app.run()
