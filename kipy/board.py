# This program source code file is part of KiCad, a free EDA CAD application.
#
# Copyright (C) 2024 KiCad Developers
#
# This program is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the
# Free Software Foundation, either version 3 of the License, or (at your
# option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program.  If not, see <http://www.gnu.org/licenses/>.

from typing import List, Dict, Union, Iterable
from google.protobuf.message import Message
from google.protobuf.any_pb2 import Any
from google.protobuf.empty_pb2 import Empty

from kipy.board_types import (
    Arc,
    FootprintInstance,
    Net,
    Pad,
    Text,
    Track,
    Via,
)
from kipy.client import KiCadClient
from kipy.common_types import TextAttributes
from kipy.enums import KICAD_T
from kipy.geometry import Box2
from kipy.util import pack_any, unpack_any
from kipy.wrapper import Wrapper

from kipy.proto.common.types import DocumentSpecifier, KIID
from kipy.proto.common.commands.editor_commands_pb2 import (
    CreateItems, CreateItemsResponse,
    BoundingBoxResponse
)
from kipy.proto.board import board_pb2
from kipy.proto.board import board_types_pb2
from kipy.proto.board import board_commands_pb2

# Re-exported protobuf enum types
from kipy.proto.board.board_pb2 import (    # noqa
    BoardLayerClass 
)

_proto_to_object = {
    board_types_pb2.Arc: Arc,
    board_types_pb2.FootprintInstance: FootprintInstance,
    board_types_pb2.Net: Net,
    board_types_pb2.Pad: Pad,
    board_types_pb2.Text: Text,
    board_types_pb2.Track: Track,
    board_types_pb2.Via: Via,
}

def _unwrap(message: Any) -> Union[Message, Wrapper]:
    concrete = unpack_any(message)
    wrapper = _proto_to_object.get(type(concrete), None)
    assert(wrapper is not None)
    return wrapper(concrete)

class BoardLayerGraphicsDefaults(Wrapper):
    """Wraps a kiapi.board.types.BoardLayerGraphicsDefaults object"""
    def __init__(self, proto: board_pb2.BoardLayerGraphicsDefaults = board_pb2.BoardLayerGraphicsDefaults()):
        self._proto = proto

    @property
    def text(self) -> TextAttributes:
        return TextAttributes(self._proto.text)
        
class Board:
    def __init__(self, kicad: KiCadClient, document: DocumentSpecifier):
        self._kicad = kicad
        self._doc = document

    @property
    def document(self) -> DocumentSpecifier:
        return self._doc

    @property
    def name(self) -> str:
        """Returns the file name of the board"""
        return self._doc.board_filename
    
    def create_items(self, items: Union[Wrapper, Iterable[Wrapper]]) -> List[Wrapper]:
        command = CreateItems()

        if isinstance(items, Wrapper):
            command.items.append(pack_any(items.proto))
        else:
            command.items.extend([pack_any(i.proto) for i in items])

        command.header.document.CopyFrom(self._doc)
        return [_unwrap(result.item) for result in self._kicad.send(command, CreateItemsResponse).created_items]

    def get_items(self, type_filter: Union[KICAD_T, List[KICAD_T]]) -> List[Wrapper]:
        # return [_unwrap(result.item) for result in cmd]
        pass

    def get_tracks(self) -> List[Track]:
        return self.get_items(type_filter=[KICAD_T.PCB_TRACE_T, KICAD_T.PCB_ARC_T])
    
    def get_vias(self) -> List[Via]:
        return self.get_items(type_filter=[KICAD_T.PCB_VIA_T])
    
    def get_pads(self) -> List[Pad]:
        return self.get_items(type_filter=[KICAD_T.PCB_PAD_T])

    def get_nets(self) -> List[Net]:
        pass

    def get_selection(self):
        pass

    def add_to_selection(self, items):
        pass

    def remove_from_selection(self, items):
        pass

    def clear_selection(self):
        pass

    def get_stackup(self) -> board_pb2.BoardStackup:
        command = board_commands_pb2.GetBoardStackup()
        command.board.CopyFrom(self._doc)
        return self._kicad.send(command, board_commands_pb2.BoardStackupResponse).stackup
    
    def get_graphics_defaults(self) -> Dict[int, BoardLayerGraphicsDefaults]:
        cmd = board_commands_pb2.GetGraphicsDefaults()
        cmd.board.CopyFrom(self._doc)
        reply = self._kicad.send(cmd, board_commands_pb2.GraphicsDefaultsResponse)
        return {
            board_pb2.BoardLayerClass.BLC_SILKSCREEN:  BoardLayerGraphicsDefaults(reply.defaults.layers[0]),
            board_pb2.BoardLayerClass.BLC_COPPER:      BoardLayerGraphicsDefaults(reply.defaults.layers[1]),
            board_pb2.BoardLayerClass.BLC_EDGES:       BoardLayerGraphicsDefaults(reply.defaults.layers[2]),
            board_pb2.BoardLayerClass.BLC_COURTYARD:   BoardLayerGraphicsDefaults(reply.defaults.layers[3]),
            board_pb2.BoardLayerClass.BLC_FABRICATION: BoardLayerGraphicsDefaults(reply.defaults.layers[4]),
            board_pb2.BoardLayerClass.BLC_OTHER:       BoardLayerGraphicsDefaults(reply.defaults.layers[5])
        }
    
    def get_text_extents(self, text: Text) -> Box2:
        cmd = board_commands_pb2.GetTextExtents()
        cmd.text.CopyFrom(text.proto)
        reply = self._kicad.send(cmd, BoundingBoxResponse)
        return Box2(reply.position, reply.size)
    
    def interactive_move(self, items: Union[KIID, Iterable[KIID]]):
        cmd = board_commands_pb2.InteractiveMoveItems()
        cmd.board.CopyFrom(self._doc)

        if isinstance(items, KIID):
            cmd.items.append(items)
        else:
            cmd.items.extend(items)

        self._kicad.send(cmd, Empty)

    def refill_zones(self):
        pass
