# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AddLongNote.ui'
#
# Created by: PyQt5 UI code generator 5.8.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_AddLongNote(object):
    def setupUi(self, AddLongNote):
        AddLongNote.setObjectName("AddLongNote")
        AddLongNote.resize(378, 418)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(AddLongNote.sizePolicy().hasHeightForWidth())
        AddLongNote.setSizePolicy(sizePolicy)
        AddLongNote.setMinimumSize(QtCore.QSize(378, 418))
        AddLongNote.setMaximumSize(QtCore.QSize(378, 418))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/arcaea_main/res/ase-256x256.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap(":/arcaea_main/res/ase-256x256.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        AddLongNote.setWindowIcon(icon)
        self.gridLayout = QtWidgets.QGridLayout(AddLongNote)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(-1, -1, -1, 20)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Y_start_label = QtWidgets.QLabel(AddLongNote)
        self.Y_start_label.setMinimumSize(QtCore.QSize(350, 0))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.Y_start_label.setFont(font)
        self.Y_start_label.setObjectName("Y_start_label")
        self.verticalLayout.addWidget(self.Y_start_label)
        self.Y_start = QtWidgets.QSpinBox(AddLongNote)
        self.Y_start.setMaximum(999999)
        self.Y_start.setObjectName("Y_start")
        self.verticalLayout.addWidget(self.Y_start)
        self.Y_end_label = QtWidgets.QLabel(AddLongNote)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.Y_end_label.setFont(font)
        self.Y_end_label.setObjectName("Y_end_label")
        self.verticalLayout.addWidget(self.Y_end_label)
        self.Y_end = QtWidgets.QSpinBox(AddLongNote)
        self.Y_end.setMaximum(999999)
        self.Y_end.setObjectName("Y_end")
        self.verticalLayout.addWidget(self.Y_end)
        self.X_start_label = QtWidgets.QLabel(AddLongNote)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.X_start_label.setFont(font)
        self.X_start_label.setObjectName("X_start_label")
        self.verticalLayout.addWidget(self.X_start_label)
        self.lcdNumber = QtWidgets.QLCDNumber(AddLongNote)
        self.lcdNumber.setMinimumSize(QtCore.QSize(0, 70))
        self.lcdNumber.setProperty("intValue", 1)
        self.lcdNumber.setObjectName("lcdNumber")
        self.verticalLayout.addWidget(self.lcdNumber)
        self.horizontalSlider = QtWidgets.QSlider(AddLongNote)
        self.horizontalSlider.setMinimum(1)
        self.horizontalSlider.setMaximum(4)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setTickPosition(QtWidgets.QSlider.NoTicks)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.verticalLayout.addWidget(self.horizontalSlider)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.pushButton = QtWidgets.QPushButton(AddLongNote)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMinimumSize(QtCore.QSize(0, 60))
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(AddLongNote)
        self.horizontalSlider.valueChanged['int'].connect(self.lcdNumber.display)
        self.pushButton.clicked.connect(AddLongNote.new_note)
        QtCore.QMetaObject.connectSlotsByName(AddLongNote)

    def retranslateUi(self, AddLongNote):
        _translate = QtCore.QCoreApplication.translate
        AddLongNote.setWindowTitle(_translate("AddLongNote", "Add Long Note"))
        self.Y_start_label.setText(_translate("AddLongNote", "開始時間(ミリ秒)"))
        self.Y_end_label.setText(_translate("AddLongNote", "終了時間(ミリ秒)"))
        self.X_start_label.setText(_translate("AddLongNote", "位置(整数)[1-4]"))
        self.pushButton.setText(_translate("AddLongNote", "追加"))

import main_rc