# Copyright The KiCad Developers
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the “Software”), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import nox
from nox.sessions import Session

nox.options.sessions = ["lint", "mypy", "tests"]

PROJECT_LINT_DIRS = ["examples", "kipy", "tests", "tools"]

@nox.session
def fmt(session: Session):
    session.install("ruff")
    session.run("ruff", "format", *PROJECT_LINT_DIRS)

@nox.session
@nox.parametrize(
    "command",
    [
        nox.param(["ruff", "check", *PROJECT_LINT_DIRS], id="lint_check"),
        nox.param(["ruff", "format", "--check", *PROJECT_LINT_DIRS], id="format_check"),
    ],
)
def lint(session: Session, command: list[str]) -> None:
    session.install("ruff")
    session.run(*command)

@nox.session
def mypy(session: Session) -> None:
    session.install("poetry")
    session.run("poetry", "install", "--with", "dev")
    session.run("mypy", "-p", "kipy")

@nox.session
def tests(session: Session) -> None:
    session.install("poetry")
    session.run("poetry", "install", "--with", "dev")
    session.run("pytest")
