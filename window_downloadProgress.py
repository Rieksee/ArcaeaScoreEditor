# -*- coding: utf-8 -*-
from ui_downloadProgress import Ui_Download_progress
from PyQt5.QtWidgets import *
from PyQt5 import QtGui, QtCore

class window_downloadProgress(QWidget):
    def __init__(self, parent=None, isolate=True):
        if not isolate:
            super(window_downloadProgress, self).__init__(parent)
        else:
            super(window_downloadProgress, self).__init__(None)
        self.ui = Ui_Download_progress()
        self.ui.setupUi(self)

    def set_val(self, val):
        self.ui.progressBar.setValue(val)