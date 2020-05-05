# -*- coding:utf-8 -*-
# author：huawei
import os
import random
import threading
import time
import uuid

from python2sky.util.date_util import current_milli_time


def get_uuid():
    uid = uuid.uuid1()
    uid = str(uid).replace("-", "")
    return uid


lock = threading.Lock()


def global_id_generator(instance_id):
    with lock:
        return [str(instance_id), str(current_milli_time()), random_id()]


def random_id():
    return int(round(time.time() * 10000000)) + random.randrange(11111, 99999)


def global_id_to_string(ids):
    return str(ids[0]) + "." + str(ids[1]) + "." + str(ids[2])


def string_to_global_id(id_str):
    return id_str.split(".")


if __name__ == '__main__':
    print(random_id())
    print(get_uuid())
    ids = global_id_generator(1)
    print(ids)
    ids_str = global_id_to_string(ids)

    print(ids_str)
    print(string_to_global_id(ids_str))
