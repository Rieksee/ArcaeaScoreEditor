# -*- coding: utf-8 -*-
from ui_tapNote import Ui_AddTapNote
from PyQt5.QtWidgets import *

class window_tapNote(QWidget):
    def __init__(self, parent=None, isolate=True):
        if not isolate:
            super(window_tapNote, self).__init__(parent)
        else:
            super(window_tapNote, self).__init__(None)
        self.ui = Ui_AddTapNote()
        self.parent = parent
        self.ui.setupUi(self)

    def new_note(self):
        note = {}
        note['type'] = 2
        note['startY'] = self.ui.Y_start.value()
        note['startX'] = self.ui.horizontalSlider.value()
        self.parent.proj_append(note)
        self.close()
        self = None