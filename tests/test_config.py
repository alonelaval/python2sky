# -*- coding:utf-8 -*-
# author：huawei
import unittest

from python2sky import config


class TestConfig(unittest.TestCase):

    def testConfig(self):
        self.assertEqual(config.SERVICE_ID, 0)
        config.SERVICE_ID = 1
        self.assertEqual(config.SERVICE_ID, 1)
        config.SERVICE_ID = 2
        self.assertEqual(config.SERVICE_ID, 2)
        config.SERVICE_INSTANCE_ID = 1
        self.assertEqual(config.SERVICE_INSTANCE_ID, 1)

