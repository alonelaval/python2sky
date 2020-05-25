# -*- coding:utf-8 -*-
# author：huawei
from python2sky.context.span import Span


class NoopSpan(Span):

    def is_entry(self):
        return False

    def is_exit(self):
        return False

    def tag(self, key, value):
        return self

    def start(self):
        return self

    def end(self):
        return self

    def ref(self, context_carrier):
        pass

    def log(self, ex):
        return self

    def transform(self):
        pass