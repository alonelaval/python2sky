# -*- coding:utf-8 -*-
# author： huawei
import time
from datetime import datetime, timedelta


def format_value(obj):
    if obj and type(obj) == datetime:
        return obj.strftime("%Y-%m-%d %H:%M:%S")
    return obj


def parse_value(obj, format_str="%Y-%m-%d %H:%M:%S"):
    if obj and obj != "":
        return datetime.strptime(obj, format_str)
    return obj


def format_value_msec(obj):
    if obj and type(obj) == datetime:
        return obj.strftime("%Y-%m-%d %H:%M:%S.%f")
    return obj


def parse_value_msec(obj, format_str="%Y-%m-%d %H:%M:%S.%f"):
    if obj and obj != "":
        return datetime.strptime(obj, format_str)
    return obj


def timestamp_to_datetime(time_stamp):
    time_stamp = float(time_stamp / 1000)
    time_obj = time.localtime(time_stamp)
    return time.strftime("%Y-%m-%d %H:%M:%S", time_obj)


def datetime_to_timestamp(datetime_obj):
    """将本地(local) datetime 格式的时间 (含毫秒) 转为毫秒时间戳
    :param datetime_obj: {datetime}2016-02-25 20:21:04.242000
    :return: 13 位的毫秒时间戳 1456402864242
    """
    local_timestamp = int(time.mktime(datetime_obj.timetuple()) * 1000.0 + datetime_obj.microsecond / 1000.0)
    return local_timestamp


def exchange_to_time_bucket(obj):
    obj = obj.replace("-", "")
    obj = obj.replace(" ", "")
    obj = obj.replace(":", "")
    return int(obj)


def add_day(datetime_obj, days):
    return datetime_obj + timedelta(days=days)


def subtract_day(datetime_obj, days):
    return datetime_obj - timedelta(days=days)


def start_time_duration_to_second_time_bucket(date_str, step="SECOND"):
    second_time_bucket = 0
    if step == "MONTH":
        second_time_bucket = exchange_to_time_bucket(date_str) * 100 * 100 * 100 * 100
    if step == "DAY":
        second_time_bucket = exchange_to_time_bucket(date_str) * 100 * 100 * 100
    if step == "HOUR":
        second_time_bucket = exchange_to_time_bucket(date_str) * 100 * 100
    if step == "MINUTE":
        second_time_bucket = exchange_to_time_bucket(date_str) * 100
    if step == "SECOND":
        second_time_bucket = exchange_to_time_bucket(date_str)

    return second_time_bucket


def end_time_duration_to_second_time_bucket(date_str, step="SECOND"):
    second_time_bucket = 0
    if step == "MONTH":
        second_time_bucket = (((exchange_to_time_bucket(date_str) * 100 + 99) * 100 + 99) * 100 + 99) * 100 + 99
    if step == "DAY":
        second_time_bucket = ((exchange_to_time_bucket(date_str) * 100 + 99) * 100 + 99) * 100 + 99
    if step == "HOUR":
        second_time_bucket = (exchange_to_time_bucket(date_str) * 100 + 99) * 100 + 99
    if step == "MINUTE":
        second_time_bucket = exchange_to_time_bucket(date_str) * 100 + 99
    if step == "SECOND":
        second_time_bucket = exchange_to_time_bucket(date_str)

    return second_time_bucket


def current_milli_time():
    return int(round(time.time() * 1000))
