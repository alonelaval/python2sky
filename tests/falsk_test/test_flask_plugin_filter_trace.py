# -*- coding:utf-8 -*-
# author：huawei
import logging

import requests
from flask import Flask, request, request_finished, config

from python2sky.bootstrap import skywalking_boot
from python2sky.plugin.requests_plugin import requests_install
from python2sky.plugin.trace_plugin import trace
from python2sky.plugin.urllib3_plugin import urllib3_install
from python2sky.plugin.urllib_plugin import urllib_install

LOG_FORMAT = "%(asctime)s - %(levelname)s - %(filename)s[:%(lineno)d] - %(message)s"
logging.basicConfig(level=logging.DEBUG, format=LOG_FORMAT)

logger = logging.getLogger("python2sky")

from python2sky.plugin.flask_plugin import trace_request_started, flask_install

config.SERVICE_NAME = "flask_test_trace"
skywalking_boot()

app = Flask(__name__)


@app.route("/test")
def test():
    return "test"


@app.route('/flask/test')
def hello_world():
    raise BaseException("exception")
    return 'Hello, World!'


@trace()
def test_trace(v1, v2):
    return v1 + v2


@app.route('/flask/cross_process')
def cross_process():

    test_trace(1,2)

    # exit_carrier = ContextCarrier()
    # exit_span = ContextManager.create_inject_exit_span("/project/b", exit_url, exit_carrier)
    # set_layer_http(exit_span)
    # set_component(exit_span, REQUESTS)
    data = requests.get("http://localhost:8088/project/b")
    # set_tag_status_code(exit_span, data.status_code)

    # ContextManager.stop_span(exit_span)
    return "cross_process"


flask_install(app)
urllib_install()
urllib3_install()
requests_install()

app.run(debug=True, threaded=True)
