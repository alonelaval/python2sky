# -*- coding:utf-8 -*-
# author：huawei
import threading
import unittest

local = threading.local()


class TestService:

    def do(self):
        print(local.skywalking)


class TestController:
    def post(self):
        local.skywalking = "dddd"
        TestService().do()


class TestTreadLocal(unittest.TestCase):
    def setUp(self):
        pass

    def setDown(self):
        pass

    def test_thread_local(self):
        TestController().post()
