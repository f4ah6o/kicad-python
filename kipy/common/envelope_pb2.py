
'Generated protocol buffer code.'
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from ..common.types import api_status_pb2 as common_dot_types_dot_api__status__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15common/envelope.proto\x12\x0cKIAPI.COMMON\x1a\x19google/protobuf/any.proto\x1a\x1dcommon/types/api_status.proto"\x14\n\x12API_REQUEST_HEADER"f\n\x0bAPI_REQUEST\x120\n\x06header\x18\x01 \x01(\x0b2 .KIAPI.COMMON.API_REQUEST_HEADER\x12%\n\x07message\x18\x02 \x01(\x0b2\x14.google.protobuf.Any"\x15\n\x13API_RESPONSE_HEADER"\x98\x01\n\x0cAPI_RESPONSE\x121\n\x06header\x18\x01 \x01(\x0b2!.KIAPI.COMMON.API_RESPONSE_HEADER\x12%\n\x07message\x18\x02 \x01(\x0b2\x14.google.protobuf.Any\x12.\n\x06status\x18\x03 \x01(\x0e2\x1e.KIAPI.COMMON.TYPES.API_STATUSb\x06proto3')
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'common.envelope_pb2', globals())
if (_descriptor._USE_C_DESCRIPTORS == False):
    DESCRIPTOR._options = None
    _API_REQUEST_HEADER._serialized_start = 97
    _API_REQUEST_HEADER._serialized_end = 117
    _API_REQUEST._serialized_start = 119
    _API_REQUEST._serialized_end = 221
    _API_RESPONSE_HEADER._serialized_start = 223
    _API_RESPONSE_HEADER._serialized_end = 244
    _API_RESPONSE._serialized_start = 247
    _API_RESPONSE._serialized_end = 399
