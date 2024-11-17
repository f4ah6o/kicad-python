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

from typing import Optional
from kipy.proto.common import types
from kipy.proto.common.types.base_types_pb2 import KIID
from kipy.wrapper import Wrapper

class Commit:
    def __init__(self, id: KIID):
        self._id = id

    @property
    def id(self) -> KIID:
        return self._id

class TextAttributes(Wrapper):
    def __init__(self, proto: Optional[types.TextAttributes] = None,
                 proto_ref: Optional[types.TextAttributes] = None):
        self._proto = proto_ref if proto_ref is not None else types.TextAttributes()

        if proto is not None:
            self._proto.CopyFrom(proto)

    @property
    def visible(self) -> bool:
        return self._proto.visible

    @visible.setter
    def visible(self, visible: bool):
        self._proto.visible = visible

class LibraryIdentifier(Wrapper):
    """A KiCad library identifier (LIB_ID), consisting of a library nickname and entry name"""
    def __init__(self, proto: Optional[types.LibraryIdentifier] = None,
                 proto_ref: Optional[types.LibraryIdentifier] = None):
        self._proto = proto_ref if proto_ref is not None else types.LibraryIdentifier()

        if proto is not None:
            self._proto.CopyFrom(proto)

    @property
    def library(self) -> str:
        return self._proto.library_nickname

    @library.setter
    def library(self, library: str):
        self._proto.library_nickname = library

    @property
    def name(self) -> str:
        return self._proto.entry_name

    @name.setter
    def name(self, name: str):
        self._proto.entry_name = name

    def __str__(self) -> str:
        return f"{self.library}:{self.name}"
