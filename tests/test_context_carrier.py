# -*- coding:utf-8 -*-
# author：huawei

from python2sky.context.context_carrier import ContextCarrier
from tests.base_test_case import BaseTestCase


class TestContextCarrier(BaseTestCase):

    def test_serialize(self):
        print(self.context_carrier.serialize())
        self.assertEqual(self.SW6, self.context_carrier.serialize())

    def test_deserialize(self):
        text = self.SW6
        context = ContextCarrier()
        context.deserialize(text)
        self.assertEqual(context.peer, self.context_carrier.peer)
