# -*- coding:utf-8 -*-
# author：huawei
import unittest

from tests.base_test_case import BaseTestCase


class TestSuffix(BaseTestCase):

    def test_t4e(self):
        op = "/favicon.ico"
        print(op[op.rfind("."):len(op)])

        self.assertEqual(op[op.rfind(".")+1:], "ico")




