# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DelArcTap.ui'
#
# Created by: PyQt5 UI code generator 5.8.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DelArcTap(object):
    def setupUi(self, DelArcTap):
        DelArcTap.setObjectName("DelArcTap")
        DelArcTap.resize(850, 400)
        DelArcTap.setMinimumSize(QtCore.QSize(850, 400))
        DelArcTap.setMaximumSize(QtCore.QSize(850, 400))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/arcaea_main/res/ase-256x256.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap(":/arcaea_main/res/ase-256x256.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        DelArcTap.setWindowIcon(icon)
        self.gridLayout = QtWidgets.QGridLayout(DelArcTap)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(DelArcTap)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.listView = QtWidgets.QListView(DelArcTap)
        self.listView.setObjectName("listView")
        self.verticalLayout.addWidget(self.listView)
        self.pushButton = QtWidgets.QPushButton(DelArcTap)
        self.pushButton.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(DelArcTap)
        self.listView.clicked['QModelIndex'].connect(DelArcTap.selected)
        self.pushButton.clicked.connect(DelArcTap.select_note)
        QtCore.QMetaObject.connectSlotsByName(DelArcTap)

    def retranslateUi(self, DelArcTap):
        _translate = QtCore.QCoreApplication.translate
        DelArcTap.setWindowTitle(_translate("DelArcTap", "Delete Arc Tap"))
        self.label.setText(_translate("DelArcTap", "削除対象を選択"))
        self.pushButton.setText(_translate("DelArcTap", "次へ"))

import main_rc
