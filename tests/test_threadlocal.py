# -*- coding:utf-8 -*-
# author：huawei
import threading
import unittest

local = threading.local()


class TestService:
    def do(self):
        return local.skywalking == "dddd"


class TestController:
    def post(self):
        local.skywalking = "dddd"
        return TestService().do()


class TestTreadLocal(unittest.TestCase):
    def setUp(self):
        local.test = 100

    def setDown(self):
        pass

    def test_thread_local(self):
        self.assertEqual(TestController().post(), True)
        self.assertEqual(local.test, 100)
