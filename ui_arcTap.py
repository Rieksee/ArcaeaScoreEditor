# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AddArcTap.ui'
#
# Created by: PyQt5 UI code generator 5.8.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_AddArcTap(object):
    def setupUi(self, AddArcTap):
        AddArcTap.setObjectName("AddArcTap")
        AddArcTap.resize(850, 400)
        AddArcTap.setMinimumSize(QtCore.QSize(850, 400))
        AddArcTap.setMaximumSize(QtCore.QSize(850, 400))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/arcaea_main/res/ase-256x256.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap(":/arcaea_main/res/ase-256x256.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        AddArcTap.setWindowIcon(icon)
        self.gridLayout = QtWidgets.QGridLayout(AddArcTap)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(AddArcTap)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.listView = QtWidgets.QListView(AddArcTap)
        self.listView.setObjectName("listView")
        self.verticalLayout.addWidget(self.listView)
        self.Y_start_label = QtWidgets.QLabel(AddArcTap)
        self.Y_start_label.setObjectName("Y_start_label")
        self.verticalLayout.addWidget(self.Y_start_label)
        self.Y_start = QtWidgets.QSpinBox(AddArcTap)
        self.Y_start.setMaximum(999999)
        self.Y_start.setObjectName("Y_start")
        self.verticalLayout.addWidget(self.Y_start)
        self.pushButton = QtWidgets.QPushButton(AddArcTap)
        self.pushButton.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(AddArcTap)
        self.listView.clicked['QModelIndex'].connect(AddArcTap.set_limit)
        self.pushButton.clicked.connect(AddArcTap.new_note)
        QtCore.QMetaObject.connectSlotsByName(AddArcTap)

    def retranslateUi(self, AddArcTap):
        _translate = QtCore.QCoreApplication.translate
        AddArcTap.setWindowTitle(_translate("AddArcTap", "Add Arc Tap"))
        self.label.setText(_translate("AddArcTap", "追加対象のトレースノートを選択"))
        self.Y_start_label.setText(_translate("AddArcTap", "時間(ミリ秒)"))
        self.pushButton.setText(_translate("AddArcTap", "追加"))

import main_rc
