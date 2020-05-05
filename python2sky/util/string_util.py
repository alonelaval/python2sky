# -*- coding:utf-8 -*-
# author：huawei


def cut(operation_name, threshold):
    return operation_name[0, threshold] if operation_name and len(
        operation_name) > threshold else operation_name


def is_empty(string):
    if string is None or string == "":
        return True
    return False
