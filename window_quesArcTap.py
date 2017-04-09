# -*- coding: utf-8 -*-
from ui_quesArcTap import Ui_window_quesArcTap
from window_arcTap import window_arcTap
from window_delArcTap import window_delArcTap
from PyQt5.QtWidgets import *

class window_quesArcTap(QWidget):
    def __init__(self, parent=None, isolate=True):
        if not isolate:
            super(window_quesArcTap, self).__init__(parent)
        else:
            super(window_quesArcTap, self).__init__(None)
        self.ui = Ui_window_quesArcTap()
        self.parent = parent
        self.ui.setupUi(self)

    def note_add(self):
        arcnotes = self.getNote_isTrace()
        self.window_arcTap = window_arcTap(arcnotes, self.parent)
        if self.window_arcTap.error:
            return
        self.window_arcTap.show()
        self.close()

    def note_delete(self):
        arcnotes = self.getNote_hasArcTap()
        self.window_delArcTap = window_delArcTap(arcnotes, self.parent)
        if self.window_delArcTap.error:
            return
        self.window_delArcTap.show()
        self.close()

    def getNote_isTrace(self):
        arcnotes = []
        for note in self.parent.proj['notes']:
            if note['type'] == 4 or note['type'] == 5:
                if note['isTrace']:
                    arcnotes.append(note)
        return arcnotes

    def getNote_hasArcTap(self):
        arcnotes = []
        for note in self.parent.proj['notes']:
            if note['type'] == 5:
                if note['isTrace']:
                    arcnotes.append(note)
        return arcnotes