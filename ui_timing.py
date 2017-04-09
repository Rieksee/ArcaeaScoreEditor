# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AddTiming.ui'
#
# Created by: PyQt5 UI code generator 5.8.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Timing(object):
    def setupUi(self, Timing):
        Timing.setObjectName("Timing")
        Timing.resize(400, 300)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/arcaea_main/res/ase-256x256.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap(":/arcaea_main/res/ase-256x256.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        Timing.setWindowIcon(icon)
        self.gridLayout = QtWidgets.QGridLayout(Timing)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Timing)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.Y_start = QtWidgets.QSpinBox(Timing)
        self.Y_start.setMaximum(999999)
        self.Y_start.setObjectName("Y_start")
        self.verticalLayout.addWidget(self.Y_start)
        self.label_2 = QtWidgets.QLabel(Timing)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.BPM = QtWidgets.QDoubleSpinBox(Timing)
        self.BPM.setDecimals(1)
        self.BPM.setMaximum(999.0)
        self.BPM.setObjectName("BPM")
        self.verticalLayout.addWidget(self.BPM)
        self.label_3 = QtWidgets.QLabel(Timing)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.timing = QtWidgets.QDoubleSpinBox(Timing)
        self.timing.setDecimals(1)
        self.timing.setMaximum(99.0)
        self.timing.setSingleStep(0.5)
        self.timing.setProperty("value", 4.0)
        self.timing.setObjectName("timing")
        self.verticalLayout.addWidget(self.timing)
        self.pushButton = QtWidgets.QPushButton(Timing)
        self.pushButton.setMinimumSize(QtCore.QSize(0, 64))
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(Timing)
        self.pushButton.clicked.connect(Timing.new_note)
        QtCore.QMetaObject.connectSlotsByName(Timing)

    def retranslateUi(self, Timing):
        _translate = QtCore.QCoreApplication.translate
        Timing.setWindowTitle(_translate("Timing", "Add Timing"))
        self.label.setText(_translate("Timing", "時間"))
        self.label_2.setText(_translate("Timing", "BPM"))
        self.label_3.setText(_translate("Timing", "拍子"))
        self.pushButton.setText(_translate("Timing", "追加"))

import main_rc
