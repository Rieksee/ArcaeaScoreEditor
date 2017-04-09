# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'newScore.ui'
#
# Created by: PyQt5 UI code generator 5.8.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_newScore(object):
    def setupUi(self, newScore):
        newScore.setObjectName("newScore")
        newScore.resize(300, 250)
        newScore.setMinimumSize(QtCore.QSize(300, 250))
        newScore.setMaximumSize(QtCore.QSize(300, 250))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/arcaea_main/res/ase-256x256.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap(":/arcaea_main/res/ase-256x256.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        newScore.setWindowIcon(icon)
        self.gridLayout = QtWidgets.QGridLayout(newScore)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(newScore)
        self.label.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(newScore)
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.audioOffset = QtWidgets.QSpinBox(newScore)
        self.audioOffset.setObjectName("audioOffset")
        self.verticalLayout.addWidget(self.audioOffset)
        self.pushButton = QtWidgets.QPushButton(newScore)
        self.pushButton.setMaximumSize(QtCore.QSize(16777215, 50))
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(newScore)
        self.pushButton.clicked.connect(newScore.new_score)
        QtCore.QMetaObject.connectSlotsByName(newScore)

    def retranslateUi(self, newScore):
        _translate = QtCore.QCoreApplication.translate
        newScore.setWindowTitle(_translate("newScore", "New Score"))
        self.label.setText(_translate("newScore", "新規楽曲"))
        self.label_2.setText(_translate("newScore", "AudioOffset"))
        self.pushButton.setText(_translate("newScore", "作成"))

import main_rc
