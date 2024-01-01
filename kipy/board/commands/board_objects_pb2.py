
'Generated protocol buffer code.'
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ...board.types import track_pb2 as board_dot_types_dot_track__pb2
from ...common.types import command_status_pb2 as common_dot_types_dot_command__status__pb2
from ...common.types import kiid_pb2 as common_dot_types_dot_kiid__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n"board/commands/board_objects.proto\x12\x14KIAPI.BOARD.COMMANDS\x1a\x17board/types/track.proto\x1a!common/types/command_status.proto\x1a\x17common/types/kiid.proto\x1a google/protobuf/field_mask.proto"7\n\x0cDELETE_ITEMS\x12\'\n\x05items\x18\x01 \x03(\x0b2\x18.KIAPI.COMMON.TYPES.KIID"B\n\nGET_TRACKS\x12.\n\nfield_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMaskJ\x04\x08\x01\x10\x02";\n\x0fTRACKS_RESPONSE\x12(\n\x06tracks\x18\x01 \x03(\x0b2\x18.KIAPI.BOARD.TYPES.TRACK"a\n\tGET_TRACK\x12$\n\x02id\x18\x01 \x01(\x0b2\x18.KIAPI.COMMON.TYPES.KIID\x12.\n\nfield_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMask"m\n\x0eTRACK_RESPONSE\x12\'\n\x05track\x18\x01 \x01(\x0b2\x18.KIAPI.BOARD.TYPES.TRACK\x122\n\x06status\x18\x02 \x01(\x0e2".KIAPI.COMMON.TYPES.COMMAND_STATUS"g\n\x0cCREATE_TRACK\x12\'\n\x05track\x18\x01 \x01(\x0b2\x18.KIAPI.BOARD.TYPES.TRACK\x12.\n\nfield_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMask"\x8d\x01\n\x0cUPDATE_TRACK\x12$\n\x02id\x18\x01 \x01(\x0b2\x18.KIAPI.COMMON.TYPES.KIID\x12\'\n\x05track\x18\x02 \x01(\x0b2\x18.KIAPI.BOARD.TYPES.TRACK\x12.\n\nfield_mask\x18\x03 \x01(\x0b2\x1a.google.protobuf.FieldMaskb\x06proto3')
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'board.commands.board_objects_pb2', globals())
if (_descriptor._USE_C_DESCRIPTORS == False):
    DESCRIPTOR._options = None
    _DELETE_ITEMS._serialized_start = 179
    _DELETE_ITEMS._serialized_end = 234
    _GET_TRACKS._serialized_start = 236
    _GET_TRACKS._serialized_end = 302
    _TRACKS_RESPONSE._serialized_start = 304
    _TRACKS_RESPONSE._serialized_end = 363
    _GET_TRACK._serialized_start = 365
    _GET_TRACK._serialized_end = 462
    _TRACK_RESPONSE._serialized_start = 464
    _TRACK_RESPONSE._serialized_end = 573
    _CREATE_TRACK._serialized_start = 575
    _CREATE_TRACK._serialized_end = 678
    _UPDATE_TRACK._serialized_start = 681
    _UPDATE_TRACK._serialized_end = 822
