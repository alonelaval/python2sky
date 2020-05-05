# -*- coding:utf-8 -*-
# author：huawei


URL = "url"

STATUS_CODE = "status_code"

DB_TYPE = "db.type"

DB_INSTANCE = "db.instance"

DB_STATEMENT = "db.statement"

DB_BIND_VARIABLES = "db.bind_vars"

MQ_QUEUE = "mq.queue"

MQ_BROKER = "mq.broker"

MQ_TOPIC = "mq.topic"

METHOD = "http.method"

UNKNOWN = 0
DATABASE = 1
RPC_FRAMEWORK = 2
HTTP = 3
MQ = 4
CACHE = 5


class Component:
    def __init__(self, id, name):
        self.id = id
        self.name = name


FLASK = Component(6001, "Flask")
REQUESTS = Component(6002, "requests")


def set_component(span, component):
    span.component_id = component.name
    span.component_id = component.id


def set_layer_db(span):
    span.layer = DATABASE


def set_layer_rpc_framework(span):
    span.layer = RPC_FRAMEWORK


def set_layer_http(span):
    span.layer = HTTP


def set_layer_mq(span):
    span.layer = MQ


def set_layer_cache(span):
    span.layer = CACHE


def set_tag_url(span, v):
    span.tag(URL, v)


def set_tag_method(span, v):
    span.tag(METHOD, v)


def set_tag_status_code(span, v):
    span.tag(STATUS_CODE, v)


def set_tag_db_type(span, v):
    span.tag(DB_TYPE, v)


def set_tag_db_instance(span, v):
    span.tag(DB_INSTANCE, v)


def set_tag_db_statement(span, v):
    span.tag(DB_STATEMENT, v)


def set_tag_db_bind_variables(span, v):
    span.tag(DB_BIND_VARIABLES, v)


def set_tag_mq_queue(span, v):
    span.tag(MQ_QUEUE, v)


def set_tag_mq_broker(span, v):
    span.tag(MQ_BROKER, v)


def set_tag_mq_topic(span, v):
    span.tag(MQ_TOPIC, v)
