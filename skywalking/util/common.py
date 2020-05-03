# -*- coding:utf-8 -*-
# author：huawei
from skywalking.proto.common.common_pb2 import KeyStringValuePair


def build_key_value(key, value):
    pro = KeyStringValuePair()
    pro.key = key
    pro.value = str(value)
    return pro