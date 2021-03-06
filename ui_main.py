# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qtArcaea.ui'
#
# Created by: PyQt5 UI code generator 5.8.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(900, 660)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/arcaea_main/res/ase-256x256.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap(":/arcaea_main/res/ase-256x256.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        icon.addPixmap(QtGui.QPixmap(":/arcaea_main/res/ase-256x256.png"), QtGui.QIcon.Disabled, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap(":/arcaea_main/res/ase-256x256.png"), QtGui.QIcon.Disabled, QtGui.QIcon.On)
        icon.addPixmap(QtGui.QPixmap(":/arcaea_main/res/ase-256x256.png"), QtGui.QIcon.Active, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap(":/arcaea_main/res/ase-256x256.png"), QtGui.QIcon.Active, QtGui.QIcon.On)
        icon.addPixmap(QtGui.QPixmap(":/arcaea_main/res/ase-256x256.png"), QtGui.QIcon.Selected, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap(":/arcaea_main/res/ase-256x256.png"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        mainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(5, 5, 5, -1)
        self.verticalLayout_2.setSpacing(27)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(-1, 0, -1, -1)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName("verticalLayout")
        self.treeWidget = QtWidgets.QTreeWidget(self.centralwidget)
        self.treeWidget.setColumnCount(1)
        self.treeWidget.setObjectName("treeWidget")
        self.treeWidget.header().setVisible(False)
        self.verticalLayout.addWidget(self.treeWidget)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.action_selectAll = QtWidgets.QPushButton(self.centralwidget)
        self.action_selectAll.setObjectName("action_selectAll")
        self.horizontalLayout.addWidget(self.action_selectAll)
        self.action_unSelectAll = QtWidgets.QPushButton(self.centralwidget)
        self.action_unSelectAll.setObjectName("action_unSelectAll")
        self.horizontalLayout.addWidget(self.action_unSelectAll)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setContentsMargins(20, -1, 20, -1)
        self.gridLayout.setSpacing(15)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButtonArcNote = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonArcNote.setObjectName("pushButtonArcNote")
        self.gridLayout.addWidget(self.pushButtonArcNote, 2, 1, 1, 1)
        self.pushButtonNomalTap = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonNomalTap.setObjectName("pushButtonNomalTap")
        self.gridLayout.addWidget(self.pushButtonNomalTap, 1, 0, 1, 1)
        self.pushButtonArcTap = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonArcTap.setObjectName("pushButtonArcTap")
        self.gridLayout.addWidget(self.pushButtonArcTap, 1, 1, 1, 1)
        self.pushButtonNomalLong = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonNomalLong.setObjectName("pushButtonNomalLong")
        self.gridLayout.addWidget(self.pushButtonNomalLong, 2, 0, 1, 1)
        self.pushButtonTiming = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonTiming.setObjectName("pushButtonTiming")
        self.gridLayout.addWidget(self.pushButtonTiming, 3, 0, 1, 1)
        self.pushButtonDelete = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonDelete.setObjectName("pushButtonDelete")
        self.gridLayout.addWidget(self.pushButtonDelete, 3, 1, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.gridLayout_2.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 900, 31))
        self.menubar.setObjectName("menubar")
        self.menuMenu = QtWidgets.QMenu(self.menubar)
        self.menuMenu.setObjectName("menuMenu")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(mainWindow)
        self.actionOpen.setShortcutContext(QtCore.Qt.ApplicationShortcut)
        self.actionOpen.setObjectName("actionOpen")
        self.actionNew = QtWidgets.QAction(mainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionSave = QtWidgets.QAction(mainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionSave_as = QtWidgets.QAction(mainWindow)
        self.actionSave_as.setObjectName("actionSave_as")
        self.actionQuit = QtWidgets.QAction(mainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionImport = QtWidgets.QAction(mainWindow)
        self.actionImport.setObjectName("actionImport")
        self.actionExport = QtWidgets.QAction(mainWindow)
        self.actionExport.setObjectName("actionExport")
        self.actionAbout = QtWidgets.QAction(mainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.menuMenu.addAction(self.actionOpen)
        self.menuMenu.addAction(self.actionNew)
        self.menuMenu.addAction(self.actionSave)
        self.menuMenu.addAction(self.actionSave_as)
        self.menuMenu.addAction(self.actionImport)
        self.menuMenu.addAction(self.actionExport)
        self.menuMenu.addAction(self.actionQuit)
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuMenu.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(mainWindow)
        self.actionQuit.triggered.connect(mainWindow.menu_quit)
        self.actionNew.triggered.connect(mainWindow.reset)
        self.actionOpen.triggered.connect(mainWindow.menu_fileOpen)
        self.actionSave.triggered.connect(mainWindow.menu_save)
        self.actionSave_as.triggered.connect(mainWindow.menu_saveAs)
        self.pushButtonNomalLong.clicked.connect(mainWindow.note_normalLong)
        self.pushButtonNomalTap.clicked.connect(mainWindow.note_normalTap)
        self.pushButtonArcTap.clicked.connect(mainWindow.note_ArcTap)
        self.pushButtonArcNote.clicked.connect(mainWindow.note_ArcNote)
        self.actionImport.triggered.connect(mainWindow.menu_import)
        self.actionExport.triggered.connect(mainWindow.menu_export)
        self.pushButtonTiming.pressed.connect(mainWindow.note_timing)
        self.pushButtonDelete.pressed.connect(mainWindow.note_delete)
        self.action_selectAll.clicked.connect(mainWindow.action_selectAll)
        self.action_unSelectAll.clicked.connect(mainWindow.action_unSelectAll)
        self.actionAbout.triggered.connect(mainWindow.menu_about)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)
        mainWindow.setTabOrder(self.pushButtonArcNote, self.pushButtonNomalLong)
        mainWindow.setTabOrder(self.pushButtonNomalLong, self.pushButtonArcTap)
        mainWindow.setTabOrder(self.pushButtonArcTap, self.pushButtonNomalTap)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "Arcaea Score Editor"))
        self.treeWidget.headerItem().setText(0, _translate("mainWindow", "item"))
        self.action_selectAll.setText(_translate("mainWindow", "全選択"))
        self.action_unSelectAll.setText(_translate("mainWindow", "選択解除"))
        self.pushButtonArcNote.setText(_translate("mainWindow", "アークノート"))
        self.pushButtonNomalTap.setText(_translate("mainWindow", "通常タップ"))
        self.pushButtonArcTap.setText(_translate("mainWindow", "アークタップ"))
        self.pushButtonNomalLong.setText(_translate("mainWindow", "通常ロング"))
        self.pushButtonTiming.setText(_translate("mainWindow", "拍子"))
        self.pushButtonDelete.setText(_translate("mainWindow", "削除"))
        self.menuMenu.setTitle(_translate("mainWindow", "file"))
        self.menuHelp.setTitle(_translate("mainWindow", "help"))
        self.actionOpen.setText(_translate("mainWindow", "&Open"))
        self.actionOpen.setShortcut(_translate("mainWindow", "Ctrl+O"))
        self.actionNew.setText(_translate("mainWindow", "&New"))
        self.actionNew.setShortcut(_translate("mainWindow", "Ctrl+N"))
        self.actionSave.setText(_translate("mainWindow", "&Save"))
        self.actionSave.setShortcut(_translate("mainWindow", "Ctrl+S"))
        self.actionSave_as.setText(_translate("mainWindow", "&Save as..."))
        self.actionSave_as.setShortcut(_translate("mainWindow", "Ctrl+Shift+S"))
        self.actionQuit.setText(_translate("mainWindow", "&Quit"))
        self.actionQuit.setShortcut(_translate("mainWindow", "Ctrl+Q"))
        self.actionImport.setText(_translate("mainWindow", "&Import"))
        self.actionImport.setShortcut(_translate("mainWindow", "Ctrl+I"))
        self.actionExport.setText(_translate("mainWindow", "&Export"))
        self.actionExport.setShortcut(_translate("mainWindow", "Ctrl+E"))
        self.actionAbout.setText(_translate("mainWindow", "&About"))

import main_rc
