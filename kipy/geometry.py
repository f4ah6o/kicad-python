#!/usr/bin/env python3

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

from kipy.proto.common.types import base_types_pb2

class Vector2:
    def __init__(self, proto: base_types_pb2.Vector2):
        self._proto = proto

    @property
    def x(self) -> int:
        """The X coordinate, in integer nanometers"""
        return self._proto.x_nm
    
    @property
    def y(self) -> int:
        """The Y coordinate, in integer nanometers"""
        return self._proto.y_nm
    
class Box2:
    def __init__(self, pos_proto: base_types_pb2.Vector2, size_proto: base_types_pb2.Vector2):
        self._pos_proto = pos_proto
        self._size_proto = size_proto

    @property
    def pos(self) -> Vector2:
        return Vector2(self._pos_proto)
    
    @property
    def size(self) -> Vector2:
        return Vector2(self._size_proto)