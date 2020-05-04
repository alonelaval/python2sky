# -*- coding:utf-8 -*-
# author：huawei
import logging

LOG_FORMAT = "%(asctime)s - %(levelname)s - %(filename)s[:%(lineno)d] - %(message)s"
logging.basicConfig( level=logging.DEBUG, format=LOG_FORMAT)

def skywalking_boot():
    import skywalking.remote.service_register_client
    import skywalking.remote.trace_segment_client
