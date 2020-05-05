# -*- coding:utf-8 -*-
# author：huawei
from python2sky.proto.common.trace_common_pb2 import CrossProcess
from python2sky.proto.language_agent_v2.trace_pb2 import SegmentReference
from python2sky.util.common import null_value, build_unique_id
from python2sky.util.string_util import is_empty
from python2sky.util.uuid_util import global_id_to_string, string_to_global_id
from python2sky.util.base64_util import encode, decode


def encode_compressed_field(id, text):
    if id and id != 0:
        return encode(str(id))
    return encode("#" + text)


def decode_field(text):
    text = decode(text)
    if text and text.startswith("#"):
        return text[1:], 0
    return None, int(text)


class ContextCarrier:
    def __init__(self):
        self.trace_segment_id = None
        self.span_id = -1
        self.parent_service_instance_id = 0
        self.entry_service_instance_id = 0
        self.peer = None
        self.peer_id = None
        self.entry_endpoint_name = None
        self.parent_endpoint_name = None
        self.trace_id = None
        self.sample = None
        self.parent_endpoint_id = 0
        self.network_address_id = None
        self.entry_endpoint_id = None
        self.type = None

    def deserialize(self, text):
        parts = text.split("-", 9)
        self.sample = parts[0]
        self.trace_id = string_to_global_id(decode(parts[1]))
        self.trace_segment_id = string_to_global_id(decode(parts[2]))
        self.span_id = int(parts[3])
        self.parent_service_instance_id = int(parts[4])
        self.entry_service_instance_id = int(parts[5])
        self.peer, self.peer_id = decode_field(parts[6])
        self.entry_endpoint_name, self.entry_endpoint_id = decode_field(parts[7])
        self.parent_endpoint_name, self.parent_endpoint_id = decode_field(parts[8])

    def serialize(self):
        if self.trace_id is None:
            return None
        return "-".join(["1",
                         encode(global_id_to_string(self.trace_id)),
                         encode(global_id_to_string(self.trace_segment_id)),
                         str(self.span_id),
                         str(self.parent_service_instance_id),
                         str(self.entry_service_instance_id),
                         encode_compressed_field(self.network_address_id, self.peer),
                         encode_compressed_field(self.entry_endpoint_id, self.entry_endpoint_name),
                         encode_compressed_field(self.parent_endpoint_id, self.parent_endpoint_name)
                         ])

    def transform(self):
        segment_reference = SegmentReference()

        if self.type == CrossProcess:
            segment_reference.refType = self.type
            if null_value(self.peer_id):
                segment_reference.networkAddress = self.peer
            else:
                segment_reference.networkAddressId = self.peer_id
        else:
            segment_reference.refType = self.type

        segment_reference.parentServiceInstanceId = self.parent_service_instance_id
        segment_reference.entryServiceInstanceId = self.entry_service_instance_id
        segment_reference.parentTraceSegmentId.CopyFrom(build_unique_id(self.trace_segment_id))
        segment_reference.parentSpanId = self.span_id

        if null_value(self.entry_endpoint_id):
            if not is_empty(self.entry_endpoint_name):
                segment_reference.entryEndpoint = self.entry_endpoint_name
        else:
            segment_reference.entryEndpointId = self.entry_endpoint_id

        if null_value(self.parent_endpoint_id):
            if not is_empty(self.parent_endpoint_name):
                segment_reference.parentEndpoint = self.parent_endpoint_name
        else:
            segment_reference.parentEndpointId = self.parent_endpoint_id

        return segment_reference







