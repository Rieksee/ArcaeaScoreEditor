# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AddTapNote.ui'
#
# Created by: PyQt5 UI code generator 5.8.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_AddTapNote(object):
    def setupUi(self, AddTapNote):
        AddTapNote.setObjectName("AddTapNote")
        AddTapNote.resize(368, 267)
        AddTapNote.setMinimumSize(QtCore.QSize(368, 267))
        AddTapNote.setMaximumSize(QtCore.QSize(368, 267))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/arcaea_main/res/ase-256x256.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap(":/arcaea_main/res/ase-256x256.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        AddTapNote.setWindowIcon(icon)
        self.gridLayout_2 = QtWidgets.QGridLayout(AddTapNote)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setContentsMargins(-1, -1, -1, 0)
        self.gridLayout.setHorizontalSpacing(50)
        self.gridLayout.setVerticalSpacing(9)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.verticalLayout_4.setContentsMargins(-1, -1, -1, 20)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.Y_start_label = QtWidgets.QLabel(AddTapNote)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.Y_start_label.setFont(font)
        self.Y_start_label.setObjectName("Y_start_label")
        self.verticalLayout_4.addWidget(self.Y_start_label)
        self.Y_start = QtWidgets.QSpinBox(AddTapNote)
        self.Y_start.setMaximum(999999)
        self.Y_start.setObjectName("Y_start")
        self.verticalLayout_4.addWidget(self.Y_start)
        self.X_start_label = QtWidgets.QLabel(AddTapNote)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.X_start_label.setFont(font)
        self.X_start_label.setObjectName("X_start_label")
        self.verticalLayout_4.addWidget(self.X_start_label)
        self.lcdNumber = QtWidgets.QLCDNumber(AddTapNote)
        self.lcdNumber.setMinimumSize(QtCore.QSize(100, 70))
        self.lcdNumber.setProperty("intValue", 1)
        self.lcdNumber.setObjectName("lcdNumber")
        self.verticalLayout_4.addWidget(self.lcdNumber)
        self.horizontalSlider = QtWidgets.QSlider(AddTapNote)
        self.horizontalSlider.setMinimum(1)
        self.horizontalSlider.setMaximum(4)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.verticalLayout_4.addWidget(self.horizontalSlider)
        self.gridLayout.addLayout(self.verticalLayout_4, 0, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(AddTapNote)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMinimumSize(QtCore.QSize(70, 0))
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.retranslateUi(AddTapNote)
        self.horizontalSlider.valueChanged['int'].connect(self.lcdNumber.display)
        self.pushButton.clicked.connect(AddTapNote.new_note)
        QtCore.QMetaObject.connectSlotsByName(AddTapNote)

    def retranslateUi(self, AddTapNote):
        _translate = QtCore.QCoreApplication.translate
        AddTapNote.setWindowTitle(_translate("AddTapNote", "Add Tap Note"))
        self.Y_start_label.setText(_translate("AddTapNote", "時間(ミリ秒)"))
        self.X_start_label.setText(_translate("AddTapNote", "位置(整数)[1-4]"))
        self.pushButton.setText(_translate("AddTapNote", "追加"))

import main_rc
