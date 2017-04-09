# -*- coding: utf-8 -*-
from ui_about import Ui_About
from PyQt5.QtWidgets import *

class window_about(QWidget):
    def __init__(self, parent=None, isolate=True):
        if not isolate:
            super(window_about, self).__init__(parent)
        else:
            super(window_about, self).__init__(None)
        self.ui = Ui_About()
        self.parent = parent
        self.ui.setupUi(self)
        self.ui.label_version.setText(self.parent.version)        

    def chk_new(self):
        # chk = self.parent.updateChk()
        # if chk is not None:
            # if not chk:
        self.parent.messageBox(2, "確認機能は停止しています", self)
