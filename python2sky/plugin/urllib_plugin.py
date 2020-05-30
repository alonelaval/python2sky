# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

# -*- coding:utf-8 -*-

# author：huawei
# from https://github.com/apache/skywalking-python/blob/master/skywalking/plugins/sw_urllib_request/__init__.py
import logging
import traceback
from urllib.request import Request, OpenerDirector

from python2sky.config import SKYWALKING_HERADER_V2
from python2sky.context.common import set_layer_http, set_component, set_tag_status_code, set_tag_url, set_tag_method
from python2sky.context.context_carrier import ContextCarrier
from python2sky.context.context_manager import ContextManager

logger = logging.getLogger(__name__)


def urllib_install():
    # noinspection PyBroadException
    try:
        from urllib.request import OpenerDirector
        from urllib.error import HTTPError

        _open = OpenerDirector.open

        def _sw_open(this: OpenerDirector, fullurl, data, timeout):
            if isinstance(fullurl, str):
                fullurl = Request(fullurl, data)

            context_carrier = ContextCarrier()

            exit_span = ContextManager.create_inject_exit_span(fullurl.selector or '/', fullurl.host, context_carrier)
            set_layer_http(exit_span)
            set_component(exit_span, "urllib")
            fullurl.add_header(SKYWALKING_HERADER_V2, context_carrier.serialize())
            try:
                res = _open(this, fullurl, data, timeout)
                set_tag_status_code(exit_span, res.code)
                set_tag_url(exit_span, fullurl.full_url)
                set_tag_method(exit_span, fullurl.get_method())

                if res.code >= 400:
                    exit_span.error_occurred = True
            except HTTPError as e:
                exit_span.log(e)
                raise e
            finally:
                ContextManager.stop_span(exit_span)
            return res

        OpenerDirector.open = _sw_open
    except Exception:
        logger.warning('failed to install plugin %s', __name__)
        traceback.print_exc()
