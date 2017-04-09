# -*- coding: utf-8 -*-
from ui_timing import Ui_Timing
from PyQt5.QtWidgets import *
from PyQt5 import QtGui, QtCore

class window_timing(QWidget):
    def __init__(self, parent=None, isolate=True):
        if not isolate:
            super(window_timing, self).__init__(parent)
        else:
            super(window_timing, self).__init__(None)
        self.ui = Ui_Timing()
        self.parent = parent
        self.ui.setupUi(self)

    def new_note(self):
        starty = self.ui.Y_start.value()
        bpm = self.ui.BPM.value()
        timing = self.ui.timing.value()
        note = {}
        note['type'] = 1
        note['startY'] = starty
        note['BPM'] = bpm
        note['time'] = timing
        self.parent.proj_append(note)
        self.close()
        self = None
