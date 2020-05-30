# -*- coding:utf-8 -*-
# author：huawei
import sys
from functools import wraps

from python2sky.context.context_manager import ContextManager


def trace(operation_name=None):
    def wrapper(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            local_span = ContextManager.create_local_span(operation_name or "/"+f.__name__)
            try:
                return f(*args, **kwargs)
            except BaseException as ex:
                local_span.log(ex)
                raise ex
            finally:
                ContextManager.stop_span(local_span)

        return decorated_function
    return wrapper
