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

from python2sky.config import SKYWALKING_HERADER_V2
from python2sky.context.common import set_layer_http, set_component, set_tag_status_code, set_tag_url, set_tag_method, \
    REQUESTS
from python2sky.context.context_carrier import ContextCarrier
from python2sky.context.context_manager import ContextManager

logger = logging.getLogger(__name__)


def requests_install():
    # noinspection PyBroadException
    try:
        from requests import Session

        _request = Session.request

        def _sw_request(this: Session, method, url,
                     params=None, data=None, headers=None, cookies=None, files=None,
                     auth=None, timeout=None, allow_redirects=True, proxies=None,
                     hooks=None, stream=None, verify=None, cert=None, json=None):

            context_carrier = ContextCarrier()
            from urllib.parse import urlparse
            res = urlparse(url)

            exit_span = ContextManager.create_inject_exit_span(res.path, res.netloc, context_carrier)
            set_layer_http(exit_span)
            set_component(exit_span, REQUESTS)

            if headers is None:
                headers = {SKYWALKING_HERADER_V2: context_carrier.serialize()}
            else:
                headers[SKYWALKING_HERADER_V2] = context_carrier.serialize()

            try:
                res = _request(this, method, url, params, data, headers, cookies, files, auth, timeout, allow_redirects,
                               proxies,
                               hooks, stream, verify, cert, json)
                set_tag_status_code(exit_span, res.status_code)
                set_tag_url(exit_span, url)
                set_tag_method(exit_span, method)

                if res.status_code >= 400:
                    exit_span.error_occurred = True
            except BaseException as e:
                exit_span.log(e)
                raise e
            finally:
                ContextManager.stop_span(exit_span)
            return res

        Session.request = _sw_request
    except Exception:
        logger.warning('failed to install plugin %s', __name__)
        traceback.print_exc()
