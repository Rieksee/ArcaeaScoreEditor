# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QuesArcTAp.ui'
#
# Created by: PyQt5 UI code generator 5.8.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_window_quesArcTap(object):
    def setupUi(self, window_quesArcTap):
        window_quesArcTap.setObjectName("window_quesArcTap")
        window_quesArcTap.resize(388, 250)
        window_quesArcTap.setMinimumSize(QtCore.QSize(388, 250))
        window_quesArcTap.setMaximumSize(QtCore.QSize(388, 250))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/arcaea_main/res/ase-256x256.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap(":/arcaea_main/res/ase-256x256.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        window_quesArcTap.setWindowIcon(icon)
        self.gridLayout = QtWidgets.QGridLayout(window_quesArcTap)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(window_quesArcTap)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.note_delete = QtWidgets.QPushButton(window_quesArcTap)
        self.note_delete.setMinimumSize(QtCore.QSize(0, 70))
        self.note_delete.setObjectName("note_delete")
        self.gridLayout.addWidget(self.note_delete, 2, 0, 1, 1)
        self.note_add = QtWidgets.QPushButton(window_quesArcTap)
        self.note_add.setEnabled(True)
        self.note_add.setMinimumSize(QtCore.QSize(0, 70))
        self.note_add.setObjectName("note_add")
        self.gridLayout.addWidget(self.note_add, 1, 0, 1, 1)

        self.retranslateUi(window_quesArcTap)
        self.note_add.clicked.connect(window_quesArcTap.note_add)
        self.note_delete.clicked.connect(window_quesArcTap.note_delete)
        QtCore.QMetaObject.connectSlotsByName(window_quesArcTap)

    def retranslateUi(self, window_quesArcTap):
        _translate = QtCore.QCoreApplication.translate
        window_quesArcTap.setWindowTitle(_translate("window_quesArcTap", "Arc Tap"))
        self.label.setText(_translate("window_quesArcTap", "アークタップのノーツをどうする？"))
        self.note_delete.setText(_translate("window_quesArcTap", "削除"))
        self.note_add.setText(_translate("window_quesArcTap", "追加"))

import main_rc
