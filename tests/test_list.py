# -*- coding:utf-8 -*-
# author：huawei
import unittest

from skywalking.util.uuid_util import global_id_generator, global_id_to_string, string_to_global_id


class TestList(unittest.TestCase):
    def test_list(self):
        id = global_id_generator(1)

        id_str = global_id_to_string(id)

        id2 = string_to_global_id(id_str)

        self.assertEqual(id, id2)

