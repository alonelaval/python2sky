# -*- coding:utf-8 -*-
# author：huawei
from python2sky.proto.common.common_pb2 import KeyStringValuePair
from python2sky.proto.common.trace_common_pb2 import UniqueId


def build_key_value(key, value):
    pro = KeyStringValuePair()
    pro.key = key
    pro.value = str(value)
    return pro


def build_unique_id(trace_id):
    unique_id = UniqueId()
    unique_id.idParts.append(int(trace_id[0]))
    unique_id.idParts.append(int(trace_id[1]))
    unique_id.idParts.append(int(trace_id[2]))
    return unique_id


def null_value(id):
    if id == 0 or id is None:
        return True
    return False
