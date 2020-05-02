# -*- coding:utf-8 -*-
# author：huawei

from skywalking.util.uuid_util import global_id_to_string, string_to_global_id
from skywalking.util.base64_util import encode, decode


class ContextCarrier:
    def __init__(self):
        self.trace_segment_id = None
        self.span_id = -1
        self.parent_service_instance_id = 0
        self.entry_service_instance_id = 0
        self.peer_host = None
        self.entry_endpoint_name = None
        self.parent_endpoint_name = None
        self.trace_id = []
        self.sample = None
        self.parent_endpoint_id = 0
        self.network_address_id = None
        self.entry_endpoint_id =None

    def deserialize(self, text):
        parts = text.split("-", 9)
        self.sample = parts[0]
        self.trace_id = string_to_global_id(decode(parts[1]))
        self.trace_segment_id = string_to_global_id(decode(parts[2]))
        self.span_id = int(parts[3])
        self.parent_service_instance_id = int(parts[4])
        self.entry_service_instance_id = int(parts[5])
        self.peer_host = self.decode_field(parts[6])
        self.entry_endpoint_name = self.decode_field(parts[7])
        self.parent_endpoint_name = self.decode_field(parts[8])

    def serialize(self):
        return "-".join(["1",
                         encode(global_id_to_string(self.trace_id)),
                         encode(global_id_to_string(self.trace_segment_id)),
                         str(self.span_id),
                         str(self.parent_service_instance_id),
                         str(self.entry_service_instance_id),
                         self.encode_compressed_field(self.network_address_id, self.peer_host),
                         self.encode_compressed_field(self.entry_endpoint_id, self.entry_endpoint_name),
                         self.encode_compressed_field(self.parent_endpoint_id, self.parent_endpoint_name)
                         ])

    def encode_compressed_field(self, id, text):
        if id and id != 0:
            return encode(str(id))
        return encode("#" + text)

    def decode_field(self,text):
        text = decode(text)
        if text and text.startswith("#"):
            return text[1:]
        return ""
