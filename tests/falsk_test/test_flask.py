# -*- coding:utf-8 -*-
# author：huawei
import requests
from flask import Flask, request

from skywalking.boot_starp import skywalking_boot

skywalking_boot()

from skywalking.context.context_carrier import ContextCarrier
from skywalking.context.context_manager import ContextManager

app = Flask(__name__)


@app.route('/flask/test')
def hello_world():
    sw6 = request.headers.get("sw6")
    context_carrier = None
    if sw6 and sw6 != "":
        context_carrier = ContextCarrier()
        context_carrier.deserialize(sw6)

    entry_span = ContextManager.create_entry_span("/", None)

    exit_url = "localhost:8088"
    # exit_carrier = ContextCarrier()
    # exit_span = ContextManager.create_inject_exit_span("/project/b", exit_url, exit_carrier)

    # requests.get("http://localhost:8088/project/b", headers={"sw6": exit_carrier.serialize()})

    # ContextManager.stop_span(exit_span)
    ContextManager.stop_span(entry_span)
    return 'Hello, World!'


app.run()
