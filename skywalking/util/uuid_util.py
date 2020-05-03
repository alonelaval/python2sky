# -*- coding:utf-8 -*-
# author：huawei
import random
import uuid

from skywalking.util.date_util import current_milli_time


def get_uuid():
    uid = uuid.uuid1()
    uid = str(uid).replace("-", "")
    return uid


def global_id_generator(instance_id):
    return [str(instance_id), str(current_milli_time()), str(random.getrandbits(64))]


def global_id_to_string(ids):
    return str(ids[0]) + "." + str(ids[1]) + "." + str(ids[2])


def string_to_global_id(id_str):
    return id_str.split(".")


if __name__ == '__main__':
    print(get_uuid())
    ids = global_id_generator(1)
    print(ids)
    ids_str = global_id_to_string(ids)

    print(ids_str)
    print(string_to_global_id(ids_str))
