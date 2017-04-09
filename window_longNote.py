# -*- coding: utf-8 -*-
from ui_longNote import Ui_AddLongNote
from PyQt5.QtWidgets import *

class window_longNote(QWidget):
    def __init__(self, parent=None, isolate=True):
        if not isolate:
            super(window_longNote, self).__init__(parent)
        else:
            super(window_longNote, self).__init__(None)
        self.ui = Ui_AddLongNote()
        self.parent = parent
        self.ui.setupUi(self)

    def new_note(self):
        endY = int(self.ui.Y_end.value())
        startY = int(self.ui.Y_start.value())
        if endY <= startY:
            self.parent.dialog_info('終了時間は開始時間より後でなければなりません。\nノーツは追加されませんでした。')
            self.close()
            self = None
            return
        note = {}
        note['type'] = 3
        note['startY'] = startY
        note['endY'] = endY
        note['startX'] = self.ui.horizontalSlider.value()
        self.parent.proj_append(note)
        self.close()
        self = None
