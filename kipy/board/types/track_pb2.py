
'Generated protocol buffer code.'
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ...common.types import kiid_pb2 as common_dot_types_dot_kiid__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x17board/types/track.proto\x12\x11KIAPI.BOARD.TYPES\x1a\x17common/types/kiid.proto"\xb9\x01\n\x05TRACK\x12$\n\x02id\x18\x01 \x01(\x0b2\x18.KIAPI.COMMON.TYPES.KIID\x12\x0f\n\x07start_x\x18\x02 \x01(\x03\x12\x0f\n\x07start_y\x18\x03 \x01(\x03\x12\r\n\x05layer\x18\x04 \x01(\x05\x12\x0e\n\x06locked\x18\x05 \x01(\x08\x12\x10\n\x08net_code\x18\x06 \x01(\x05\x12\r\n\x05width\x18\t \x01(\x03\x12\r\n\x05end_x\x18\n \x01(\x03\x12\r\n\x05end_y\x18\x0b \x01(\x03J\x04\x08\x07\x10\x08J\x04\x08\x08\x10\tb\x06proto3')
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'board.types.track_pb2', globals())
if (_descriptor._USE_C_DESCRIPTORS == False):
    DESCRIPTOR._options = None
    _TRACK._serialized_start = 72
    _TRACK._serialized_end = 257
