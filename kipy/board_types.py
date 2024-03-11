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

from kipy.enums import PCB_LAYER_ID
from kipy.proto.common.types import KIID
from kipy.proto.board import board_types_pb2
from kipy.common_types import TextAttributes
from kipy.geometry import Vector2
from kipy.wrapper import Wrapper

class Text(Wrapper):
    """Wraps a kiapi.board.types.Text, aka PCB_TEXT object"""
    def __init__(self, proto: board_types_pb2.Text = board_types_pb2.Text()):
        self._proto = proto

    @property
    def id(self) -> KIID:
        return self._proto.text.id
    
    @property
    def position(self) -> Vector2:
        return Vector2(self._proto.text.position)
    
    @position.setter
    def position(self, pos: Vector2):
        self._proto.text.position.CopyFrom(pos.proto)

    @property
    def layer(self) -> PCB_LAYER_ID:
        return self._proto.text.layer.id
    
    @layer.setter
    def layer(self, layer: PCB_LAYER_ID):
        self._proto.text.layer.id = layer

    @property
    def locked(self) -> bool:
        return self._proto.text.locked
    
    @locked.setter
    def locked(self, locked: bool):
        self._proto.text.locked = locked

    @property
    def text(self) -> str:
        return self._proto.text.text
    
    @text.setter
    def text(self, text: str):
        self._proto.text.text = text

    @property
    def attributes(self) -> TextAttributes:
        return TextAttributes(self._proto.text.attributes)
    
    @attributes.setter
    def attributes(self, attributes: TextAttributes):
        self._proto.text.attributes.CopyFrom(attributes.proto)

class Footprint(Wrapper):
    """Represents a library footprint"""
    pass

class FootprintInstance(Wrapper):
    """Represents a footprint instance on a board"""
    pass