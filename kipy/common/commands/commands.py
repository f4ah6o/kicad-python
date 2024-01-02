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

from ... import _client
from .base_commands_pb2 import *
from .editor_commands_pb2 import *

def get_version():
    """
    :return: the KiCad version as a string, including any package-specific info
    """
    r = GetVersionResponse()
    if _client.send(GetVersion(), r):
        return r.version.full_version
    raise IOError

def run_action(action: str):
    """
    Runs a KiCad tool action, if it is available.
    WARNING: This is an unstable API and is not intended for use other than by API developers.
    KiCad does not guarantee the stability of action names, and running actions may have unintended
    side effects.
    :param action: the name of a KiCad TOOL_ACTION
    :return: a value from the KIAPI.COMMON.COMMANDS.RUN_ACTION_STATUS enum
    """
    r = RunActionResponse()
    if _client.send(RunAction(), r):
        return r.status
    raise IOError

def refresh_editor(editor):
    r = RefreshEditor()
    r.frame = editor
    if _client.send(r, None):
        return
    raise IOError

def begin_commit():
    _client.send(BeginCommit())

def end_commit(message: str):
    m = EndCommit()
    m.message = message
    _client.send(m)
