# -*- coding: utf-8 -*-
from ui_newScore import Ui_newScore
from PyQt5.QtWidgets import *
from collections import OrderedDict

class window_newScore(QWidget):
    def __init__(self, parent=None, isolate=True):
        if not isolate:
            super(window_newScore, self).__init__(parent)
        else:
            super(window_newScore, self).__init__(None)
        self.ui = Ui_newScore()
        self.parent = parent
        self.ui.setupUi(self)

    def new_score(self):
        self.parent.proj = OrderedDict()
        self.parent.proj['musicInfo'] = {}
        self.parent.proj['musicInfo']['AudioOffset'] = self.ui.audioOffset.value()
        self.parent.proj['notes'] = []
        self.parent.window_update()
        self.close()
        self = None
