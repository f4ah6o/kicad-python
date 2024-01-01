
'Generated protocol buffer code.'
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ...common.types import version_pb2 as common_dot_types_dot_version__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!common/commands/get_version.proto\x12\x15KIAPI.COMMON.COMMANDS\x1a\x1acommon/types/version.proto"\r\n\x0bGET_VERSION"J\n\x14GET_VERSION_RESPONSE\x122\n\x07version\x18\x01 \x01(\x0b2!.KIAPI.COMMON.TYPES.KICAD_VERSIONb\x06proto3')
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'common.commands.get_version_pb2', globals())
if (_descriptor._USE_C_DESCRIPTORS == False):
    DESCRIPTOR._options = None
    _GET_VERSION._serialized_start = 88
    _GET_VERSION._serialized_end = 101
    _GET_VERSION_RESPONSE._serialized_start = 103
    _GET_VERSION_RESPONSE._serialized_end = 177
