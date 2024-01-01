
'Generated protocol buffer code.'
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n common/commands/run_action.proto\x12\x15KIAPI.COMMON.COMMANDS"\x1c\n\nRUN_ACTION\x12\x0e\n\x06action\x18\x01 \x01(\t"O\n\x13RUN_ACTION_RESPONSE\x128\n\x06status\x18\x01 \x01(\x0e2(.KIAPI.COMMON.COMMANDS.RUN_ACTION_STATUS*Y\n\x11RUN_ACTION_STATUS\x12\x0f\n\x0bRAS_UNKNOWN\x10\x00\x12\n\n\x06RAS_OK\x10\x01\x12\x0f\n\x0bRAS_INVALID\x10\x02\x12\x16\n\x12RAS_FRAME_NOT_OPEN\x10\x03b\x06proto3')
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'common.commands.run_action_pb2', globals())
if (_descriptor._USE_C_DESCRIPTORS == False):
    DESCRIPTOR._options = None
    _RUN_ACTION_STATUS._serialized_start = 170
    _RUN_ACTION_STATUS._serialized_end = 259
    _RUN_ACTION._serialized_start = 59
    _RUN_ACTION._serialized_end = 87
    _RUN_ACTION_RESPONSE._serialized_start = 89
    _RUN_ACTION_RESPONSE._serialized_end = 168
