
'Generated protocol buffer code.'
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ...board.types import board_pb2 as board_dot_types_dot_board__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n%board/commands/board_management.proto\x12\x14KIAPI.BOARD.COMMANDS\x1a\x17board/types/board.proto"\x0b\n\tGET_BOARD"=\n\x12GET_BOARD_RESPONSE\x12\'\n\x05board\x18\x01 \x01(\x0b2\x18.KIAPI.BOARD.TYPES.BOARDb\x06proto3')
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'board.commands.board_management_pb2', globals())
if (_descriptor._USE_C_DESCRIPTORS == False):
    DESCRIPTOR._options = None
    _GET_BOARD._serialized_start = 88
    _GET_BOARD._serialized_end = 99
    _GET_BOARD_RESPONSE._serialized_start = 101
    _GET_BOARD_RESPONSE._serialized_end = 162
