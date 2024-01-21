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

from PyQt6.QtWidgets import *
from random import randrange

from kipy import KiCad

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("KiCad Python Example")
        btn1 = QPushButton("Check KiCad Version")
        self.st1 = QLabel("")
        szr = QVBoxLayout()
        szr.addWidget(btn1)
        szr.addWidget(self.st1)

        btn1.clicked.connect(lambda _: self.st1.setText(kicad.get_version()))

        widget = QWidget()
        widget.setLayout(szr)
        self.setCentralWidget(widget)


if __name__=='__main__':
    kicad = KiCad()
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
    print(kicad.get_version())
