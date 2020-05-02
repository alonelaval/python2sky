# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: register/Register.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from skywalking.proto.common import common_pb2 as common_dot_common__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='register/Register.proto',
  package='',
  syntax='proto3',
  serialized_options=b'\n-org.apache.skywalking.apm.network.register.v2P\001\252\002\032SkyWalking.NetworkProtocol',
  serialized_pb=b'\n\x17register/Register.proto\x1a\x13\x63ommon/common.proto\"&\n\x08Services\x12\x1a\n\x08services\x18\x01 \x03(\x0b\x32\x08.Service\"j\n\x07Service\x12\x13\n\x0bserviceName\x18\x01 \x01(\t\x12!\n\x04tags\x18\x03 \x03(\x0b\x32\x13.KeyStringValuePair\x12\'\n\nproperties\x18\x04 \x03(\x0b\x32\x13.KeyStringValuePair\"<\n\x16ServiceRegisterMapping\x12\"\n\x08services\x18\x01 \x03(\x0b\x32\x10.KeyIntValuePair\"7\n\x10ServiceInstances\x12#\n\tinstances\x18\x01 \x03(\x0b\x32\x10.ServiceInstance\"\x94\x01\n\x0fServiceInstance\x12\x11\n\tserviceId\x18\x01 \x01(\x05\x12\x14\n\x0cinstanceUUID\x18\x02 \x01(\t\x12\x0c\n\x04time\x18\x03 \x01(\x03\x12!\n\x04tags\x18\x04 \x03(\x0b\x32\x13.KeyStringValuePair\x12\'\n\nproperties\x18\x05 \x03(\x0b\x32\x13.KeyStringValuePair\"L\n\x1eServiceInstanceRegisterMapping\x12*\n\x10serviceInstances\x18\x01 \x03(\x0b\x32\x10.KeyIntValuePair\"!\n\x0cNetAddresses\x12\x11\n\taddresses\x18\x01 \x03(\t\"9\n\x11NetAddressMapping\x12$\n\naddressIds\x18\x01 \x03(\x0b\x32\x10.KeyIntValuePair\")\n\tEndpoints\x12\x1c\n\tendpoints\x18\x01 \x03(\x0b\x32\t.Endpoint\"\x9b\x01\n\x08\x45ndpoint\x12\x11\n\tserviceId\x18\x01 \x01(\x05\x12\x14\n\x0c\x65ndpointName\x18\x02 \x01(\t\x12!\n\x04tags\x18\x03 \x03(\x0b\x32\x13.KeyStringValuePair\x12\'\n\nproperties\x18\x04 \x03(\x0b\x32\x13.KeyStringValuePair\x12\x1a\n\x04\x66rom\x18\x05 \x01(\x0e\x32\x0c.DetectPoint\"<\n\x0f\x45ndpointMapping\x12)\n\x08\x65lements\x18\x01 \x03(\x0b\x32\x17.EndpointMappingElement\"q\n\x16\x45ndpointMappingElement\x12\x11\n\tserviceId\x18\x01 \x01(\x05\x12\x14\n\x0c\x65ndpointName\x18\x02 \x01(\t\x12\x12\n\nendpointId\x18\x03 \x01(\x05\x12\x1a\n\x04\x66rom\x18\x04 \x01(\x0e\x32\x0c.DetectPoint\"V\n ServiceAndNetworkAddressMappings\x12\x32\n\x08mappings\x18\x01 \x03(\x0b\x32 .ServiceAndNetworkAddressMapping\"\x81\x01\n\x1fServiceAndNetworkAddressMapping\x12\x11\n\tserviceId\x18\x01 \x01(\x05\x12\x19\n\x11serviceInstanceId\x18\x02 \x01(\x05\x12\x16\n\x0enetworkAddress\x18\x03 \x01(\t\x12\x18\n\x10networkAddressId\x18\x04 \x01(\x05\x32\xec\x02\n\x08Register\x12\x39\n\x11\x64oServiceRegister\x12\t.Services\x1a\x17.ServiceRegisterMapping\"\x00\x12Q\n\x19\x64oServiceInstanceRegister\x12\x11.ServiceInstances\x1a\x1f.ServiceInstanceRegisterMapping\"\x00\x12\x34\n\x12\x64oEndpointRegister\x12\n.Endpoints\x1a\x10.EndpointMapping\"\x00\x12?\n\x18\x64oNetworkAddressRegister\x12\r.NetAddresses\x1a\x12.NetAddressMapping\"\x00\x12[\n)doServiceAndNetworkAddressMappingRegister\x12!.ServiceAndNetworkAddressMappings\x1a\t.Commands\"\x00\x42N\n-org.apache.skywalking.apm.network.register.v2P\x01\xaa\x02\x1aSkyWalking.NetworkProtocolb\x06proto3'
  ,
  dependencies=[common_dot_common__pb2.DESCRIPTOR,])




_SERVICES = _descriptor.Descriptor(
  name='Services',
  full_name='Services',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='services', full_name='Services.services', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=48,
  serialized_end=86,
)


_SERVICE = _descriptor.Descriptor(
  name='Service',
  full_name='Service',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='serviceName', full_name='Service.serviceName', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tags', full_name='Service.tags', index=1,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='properties', full_name='Service.properties', index=2,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=88,
  serialized_end=194,
)


_SERVICEREGISTERMAPPING = _descriptor.Descriptor(
  name='ServiceRegisterMapping',
  full_name='ServiceRegisterMapping',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='services', full_name='ServiceRegisterMapping.services', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=196,
  serialized_end=256,
)


_SERVICEINSTANCES = _descriptor.Descriptor(
  name='ServiceInstances',
  full_name='ServiceInstances',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='instances', full_name='ServiceInstances.instances', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=258,
  serialized_end=313,
)


_SERVICEINSTANCE = _descriptor.Descriptor(
  name='ServiceInstance',
  full_name='ServiceInstance',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='serviceId', full_name='ServiceInstance.serviceId', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='instanceUUID', full_name='ServiceInstance.instanceUUID', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='time', full_name='ServiceInstance.time', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tags', full_name='ServiceInstance.tags', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='properties', full_name='ServiceInstance.properties', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=316,
  serialized_end=464,
)


_SERVICEINSTANCEREGISTERMAPPING = _descriptor.Descriptor(
  name='ServiceInstanceRegisterMapping',
  full_name='ServiceInstanceRegisterMapping',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='serviceInstances', full_name='ServiceInstanceRegisterMapping.serviceInstances', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=466,
  serialized_end=542,
)


_NETADDRESSES = _descriptor.Descriptor(
  name='NetAddresses',
  full_name='NetAddresses',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='addresses', full_name='NetAddresses.addresses', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=544,
  serialized_end=577,
)


_NETADDRESSMAPPING = _descriptor.Descriptor(
  name='NetAddressMapping',
  full_name='NetAddressMapping',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='addressIds', full_name='NetAddressMapping.addressIds', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=579,
  serialized_end=636,
)


_ENDPOINTS = _descriptor.Descriptor(
  name='Endpoints',
  full_name='Endpoints',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='endpoints', full_name='Endpoints.endpoints', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=638,
  serialized_end=679,
)


_ENDPOINT = _descriptor.Descriptor(
  name='Endpoint',
  full_name='Endpoint',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='serviceId', full_name='Endpoint.serviceId', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='endpointName', full_name='Endpoint.endpointName', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tags', full_name='Endpoint.tags', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='properties', full_name='Endpoint.properties', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='from', full_name='Endpoint.from', index=4,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=682,
  serialized_end=837,
)


_ENDPOINTMAPPING = _descriptor.Descriptor(
  name='EndpointMapping',
  full_name='EndpointMapping',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='elements', full_name='EndpointMapping.elements', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=839,
  serialized_end=899,
)


_ENDPOINTMAPPINGELEMENT = _descriptor.Descriptor(
  name='EndpointMappingElement',
  full_name='EndpointMappingElement',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='serviceId', full_name='EndpointMappingElement.serviceId', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='endpointName', full_name='EndpointMappingElement.endpointName', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='endpointId', full_name='EndpointMappingElement.endpointId', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='from', full_name='EndpointMappingElement.from', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=901,
  serialized_end=1014,
)


_SERVICEANDNETWORKADDRESSMAPPINGS = _descriptor.Descriptor(
  name='ServiceAndNetworkAddressMappings',
  full_name='ServiceAndNetworkAddressMappings',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='mappings', full_name='ServiceAndNetworkAddressMappings.mappings', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1016,
  serialized_end=1102,
)


_SERVICEANDNETWORKADDRESSMAPPING = _descriptor.Descriptor(
  name='ServiceAndNetworkAddressMapping',
  full_name='ServiceAndNetworkAddressMapping',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='serviceId', full_name='ServiceAndNetworkAddressMapping.serviceId', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='serviceInstanceId', full_name='ServiceAndNetworkAddressMapping.serviceInstanceId', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='networkAddress', full_name='ServiceAndNetworkAddressMapping.networkAddress', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='networkAddressId', full_name='ServiceAndNetworkAddressMapping.networkAddressId', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1105,
  serialized_end=1234,
)

_SERVICES.fields_by_name['services'].message_type = _SERVICE
_SERVICE.fields_by_name['tags'].message_type = common_dot_common__pb2._KEYSTRINGVALUEPAIR
_SERVICE.fields_by_name['properties'].message_type = common_dot_common__pb2._KEYSTRINGVALUEPAIR
_SERVICEREGISTERMAPPING.fields_by_name['services'].message_type = common_dot_common__pb2._KEYINTVALUEPAIR
_SERVICEINSTANCES.fields_by_name['instances'].message_type = _SERVICEINSTANCE
_SERVICEINSTANCE.fields_by_name['tags'].message_type = common_dot_common__pb2._KEYSTRINGVALUEPAIR
_SERVICEINSTANCE.fields_by_name['properties'].message_type = common_dot_common__pb2._KEYSTRINGVALUEPAIR
_SERVICEINSTANCEREGISTERMAPPING.fields_by_name['serviceInstances'].message_type = common_dot_common__pb2._KEYINTVALUEPAIR
_NETADDRESSMAPPING.fields_by_name['addressIds'].message_type = common_dot_common__pb2._KEYINTVALUEPAIR
_ENDPOINTS.fields_by_name['endpoints'].message_type = _ENDPOINT
_ENDPOINT.fields_by_name['tags'].message_type = common_dot_common__pb2._KEYSTRINGVALUEPAIR
_ENDPOINT.fields_by_name['properties'].message_type = common_dot_common__pb2._KEYSTRINGVALUEPAIR
_ENDPOINT.fields_by_name['from'].enum_type = common_dot_common__pb2._DETECTPOINT
_ENDPOINTMAPPING.fields_by_name['elements'].message_type = _ENDPOINTMAPPINGELEMENT
_ENDPOINTMAPPINGELEMENT.fields_by_name['from'].enum_type = common_dot_common__pb2._DETECTPOINT
_SERVICEANDNETWORKADDRESSMAPPINGS.fields_by_name['mappings'].message_type = _SERVICEANDNETWORKADDRESSMAPPING
DESCRIPTOR.message_types_by_name['Services'] = _SERVICES
DESCRIPTOR.message_types_by_name['Service'] = _SERVICE
DESCRIPTOR.message_types_by_name['ServiceRegisterMapping'] = _SERVICEREGISTERMAPPING
DESCRIPTOR.message_types_by_name['ServiceInstances'] = _SERVICEINSTANCES
DESCRIPTOR.message_types_by_name['ServiceInstance'] = _SERVICEINSTANCE
DESCRIPTOR.message_types_by_name['ServiceInstanceRegisterMapping'] = _SERVICEINSTANCEREGISTERMAPPING
DESCRIPTOR.message_types_by_name['NetAddresses'] = _NETADDRESSES
DESCRIPTOR.message_types_by_name['NetAddressMapping'] = _NETADDRESSMAPPING
DESCRIPTOR.message_types_by_name['Endpoints'] = _ENDPOINTS
DESCRIPTOR.message_types_by_name['Endpoint'] = _ENDPOINT
DESCRIPTOR.message_types_by_name['EndpointMapping'] = _ENDPOINTMAPPING
DESCRIPTOR.message_types_by_name['EndpointMappingElement'] = _ENDPOINTMAPPINGELEMENT
DESCRIPTOR.message_types_by_name['ServiceAndNetworkAddressMappings'] = _SERVICEANDNETWORKADDRESSMAPPINGS
DESCRIPTOR.message_types_by_name['ServiceAndNetworkAddressMapping'] = _SERVICEANDNETWORKADDRESSMAPPING
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Services = _reflection.GeneratedProtocolMessageType('Services', (_message.Message,), {
  'DESCRIPTOR' : _SERVICES,
  '__module__' : 'register.Register_pb2'
  # @@protoc_insertion_point(class_scope:Services)
  })
_sym_db.RegisterMessage(Services)

Service = _reflection.GeneratedProtocolMessageType('Service', (_message.Message,), {
  'DESCRIPTOR' : _SERVICE,
  '__module__' : 'register.Register_pb2'
  # @@protoc_insertion_point(class_scope:Service)
  })
_sym_db.RegisterMessage(Service)

ServiceRegisterMapping = _reflection.GeneratedProtocolMessageType('ServiceRegisterMapping', (_message.Message,), {
  'DESCRIPTOR' : _SERVICEREGISTERMAPPING,
  '__module__' : 'register.Register_pb2'
  # @@protoc_insertion_point(class_scope:ServiceRegisterMapping)
  })
_sym_db.RegisterMessage(ServiceRegisterMapping)

ServiceInstances = _reflection.GeneratedProtocolMessageType('ServiceInstances', (_message.Message,), {
  'DESCRIPTOR' : _SERVICEINSTANCES,
  '__module__' : 'register.Register_pb2'
  # @@protoc_insertion_point(class_scope:ServiceInstances)
  })
_sym_db.RegisterMessage(ServiceInstances)

ServiceInstance = _reflection.GeneratedProtocolMessageType('ServiceInstance', (_message.Message,), {
  'DESCRIPTOR' : _SERVICEINSTANCE,
  '__module__' : 'register.Register_pb2'
  # @@protoc_insertion_point(class_scope:ServiceInstance)
  })
_sym_db.RegisterMessage(ServiceInstance)

ServiceInstanceRegisterMapping = _reflection.GeneratedProtocolMessageType('ServiceInstanceRegisterMapping', (_message.Message,), {
  'DESCRIPTOR' : _SERVICEINSTANCEREGISTERMAPPING,
  '__module__' : 'register.Register_pb2'
  # @@protoc_insertion_point(class_scope:ServiceInstanceRegisterMapping)
  })
_sym_db.RegisterMessage(ServiceInstanceRegisterMapping)

NetAddresses = _reflection.GeneratedProtocolMessageType('NetAddresses', (_message.Message,), {
  'DESCRIPTOR' : _NETADDRESSES,
  '__module__' : 'register.Register_pb2'
  # @@protoc_insertion_point(class_scope:NetAddresses)
  })
_sym_db.RegisterMessage(NetAddresses)

NetAddressMapping = _reflection.GeneratedProtocolMessageType('NetAddressMapping', (_message.Message,), {
  'DESCRIPTOR' : _NETADDRESSMAPPING,
  '__module__' : 'register.Register_pb2'
  # @@protoc_insertion_point(class_scope:NetAddressMapping)
  })
_sym_db.RegisterMessage(NetAddressMapping)

Endpoints = _reflection.GeneratedProtocolMessageType('Endpoints', (_message.Message,), {
  'DESCRIPTOR' : _ENDPOINTS,
  '__module__' : 'register.Register_pb2'
  # @@protoc_insertion_point(class_scope:Endpoints)
  })
_sym_db.RegisterMessage(Endpoints)

Endpoint = _reflection.GeneratedProtocolMessageType('Endpoint', (_message.Message,), {
  'DESCRIPTOR' : _ENDPOINT,
  '__module__' : 'register.Register_pb2'
  # @@protoc_insertion_point(class_scope:Endpoint)
  })
_sym_db.RegisterMessage(Endpoint)

EndpointMapping = _reflection.GeneratedProtocolMessageType('EndpointMapping', (_message.Message,), {
  'DESCRIPTOR' : _ENDPOINTMAPPING,
  '__module__' : 'register.Register_pb2'
  # @@protoc_insertion_point(class_scope:EndpointMapping)
  })
_sym_db.RegisterMessage(EndpointMapping)

EndpointMappingElement = _reflection.GeneratedProtocolMessageType('EndpointMappingElement', (_message.Message,), {
  'DESCRIPTOR' : _ENDPOINTMAPPINGELEMENT,
  '__module__' : 'register.Register_pb2'
  # @@protoc_insertion_point(class_scope:EndpointMappingElement)
  })
_sym_db.RegisterMessage(EndpointMappingElement)

ServiceAndNetworkAddressMappings = _reflection.GeneratedProtocolMessageType('ServiceAndNetworkAddressMappings', (_message.Message,), {
  'DESCRIPTOR' : _SERVICEANDNETWORKADDRESSMAPPINGS,
  '__module__' : 'register.Register_pb2'
  # @@protoc_insertion_point(class_scope:ServiceAndNetworkAddressMappings)
  })
_sym_db.RegisterMessage(ServiceAndNetworkAddressMappings)

ServiceAndNetworkAddressMapping = _reflection.GeneratedProtocolMessageType('ServiceAndNetworkAddressMapping', (_message.Message,), {
  'DESCRIPTOR' : _SERVICEANDNETWORKADDRESSMAPPING,
  '__module__' : 'register.Register_pb2'
  # @@protoc_insertion_point(class_scope:ServiceAndNetworkAddressMapping)
  })
_sym_db.RegisterMessage(ServiceAndNetworkAddressMapping)


DESCRIPTOR._options = None

_REGISTER = _descriptor.ServiceDescriptor(
  name='Register',
  full_name='Register',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=1237,
  serialized_end=1601,
  methods=[
  _descriptor.MethodDescriptor(
    name='doServiceRegister',
    full_name='Register.doServiceRegister',
    index=0,
    containing_service=None,
    input_type=_SERVICES,
    output_type=_SERVICEREGISTERMAPPING,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='doServiceInstanceRegister',
    full_name='Register.doServiceInstanceRegister',
    index=1,
    containing_service=None,
    input_type=_SERVICEINSTANCES,
    output_type=_SERVICEINSTANCEREGISTERMAPPING,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='doEndpointRegister',
    full_name='Register.doEndpointRegister',
    index=2,
    containing_service=None,
    input_type=_ENDPOINTS,
    output_type=_ENDPOINTMAPPING,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='doNetworkAddressRegister',
    full_name='Register.doNetworkAddressRegister',
    index=3,
    containing_service=None,
    input_type=_NETADDRESSES,
    output_type=_NETADDRESSMAPPING,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='doServiceAndNetworkAddressMappingRegister',
    full_name='Register.doServiceAndNetworkAddressMappingRegister',
    index=4,
    containing_service=None,
    input_type=_SERVICEANDNETWORKADDRESSMAPPINGS,
    output_type=common_dot_common__pb2._COMMANDS,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_REGISTER)

DESCRIPTOR.services_by_name['Register'] = _REGISTER

# @@protoc_insertion_point(module_scope)
