# -*- coding: utf-8 -*-
from ui_arcNote import Ui_AddArcNote
from PyQt5.QtWidgets import *

class window_arcNote(QWidget):
    def __init__(self, parent=None, isolate=True):
        if not isolate:
            super(window_arcNote, self).__init__(parent)
        else:
            super(window_arcNote, self).__init__(None)
        self.ui = Ui_AddArcNote()
        self.parent = parent
        self.ui.setupUi(self)

    def new_note(self):
        endY = self.ui.Y_end.value()
        startY = self.ui.Y_start.value()
        if endY - startY <= 0:
            self.parent.dialog_info('終了時間は開始時間より後でなければなりません。\nノーツは追加されませんでした。')
            self.close()
            self = None
            return
        note = {}
        note['type'] = 4
        note['startY'] = startY
        note['endY'] = endY
        note['startX'] = self.ui.X_start.value()
        note['endX'] = self.ui.X_end.value()
        note['startZ'] = self.ui.Z_start.value()
        note['endZ'] = self.ui.Z_end.value()
        note['color'] = self.ui.color.value()
        curve = self.ui.curve.text()
        if curve not in ['s', 'b', 'si', 'so']:
            self.parent.dialog_info('カーブの種類は[s, b, si, so]のいずれかでなければなりません。\nノーツは追加されませんでした。')
            self.close()
            self = None
            return
        note['curve'] = curve
        note['arcTaps'] = []
        note['option'] = 'none'
        note['isTrace'] = self.ui.isTrace.isChecked()
        self.parent.proj_append(note)
        self.close()
        self = None
