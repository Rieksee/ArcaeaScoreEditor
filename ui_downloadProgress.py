# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DownloadProgress.ui'
#
# Created by: PyQt5 UI code generator 5.8.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Download_progress(object):
    def setupUi(self, Download_progress):
        Download_progress.setObjectName("Download_progress")
        Download_progress.resize(317, 167)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/arcaea_main/res/ase-256x256.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap(":/arcaea_main/res/ase-256x256.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        Download_progress.setWindowIcon(icon)
        self.gridLayout = QtWidgets.QGridLayout(Download_progress)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(-1, -1, -1, 20)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Download_progress)
        self.label.setMinimumSize(QtCore.QSize(0, 0))
        self.label.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.progressBar = QtWidgets.QProgressBar(Download_progress)
        self.progressBar.setMinimumSize(QtCore.QSize(0, 50))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout.addWidget(self.progressBar)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(Download_progress)
        QtCore.QMetaObject.connectSlotsByName(Download_progress)

    def retranslateUi(self, Download_progress):
        _translate = QtCore.QCoreApplication.translate
        Download_progress.setWindowTitle(_translate("Download_progress", "Downloading..."))
        self.label.setText(_translate("Download_progress", "ダウンロードしています。"))

import main_rc
