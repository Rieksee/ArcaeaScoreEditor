# -*- coding: utf-8 -*-
from ui_arcTap import Ui_AddArcTap
from PyQt5.QtWidgets import *
from PyQt5 import QtGui, QtCore

class window_arcTap(QWidget):
    def __init__(self, notes, parent=None, isolate=True):
        if not isolate:
            super(window_arcTap, self).__init__(parent)
        else:
            super(window_arcTap, self).__init__(None)
        self.ui = Ui_AddArcTap()
        self.parent = parent
        self.ui.setupUi(self)
        self.error = False
        self.selectedRow = None
        if not self.show_notes(notes):
            self.error = True

    def new_note(self):
        startY = self.ui.Y_start.value()
        if self.selectedRow is None:
            self.parent.dialog_info('対象のトレースノートを選択してください。')
            self.close()
            self = None
            return
        note = self.notes[self.selectedRow]
        if startY > note['endY'] or startY < note['startY']:
            self.parent.dialog_info('アークタップは選択したトレースノートが継続している間にある必要があります。')
            self.close()
            self = None
            return
        index = 0
        for proj in self.parent.proj['notes']:
            if proj['type'] == note['type'] and proj['startY'] == note['startY'] and proj['endY'] == note['endY'] and proj['startX'] == note['startX'] and proj['endX'] == note['endX']:
                self.parent.proj['notes'][index]['arcTaps'].append(startY)
                self.parent.proj['notes'][index]['arcTaps'].sort()
                self.parent.proj['notes'][index]['type'] = 5
                break
            index = index + 1
        self.parent.window_update()
        self.parent.dialog_info('ノーツを追加しました。')
        self.close()
        self = None

    def set_limit(self, index):
        self.selectedRow = index.row()
        note = self.notes[self.selectedRow]
        self.ui.Y_start.setMinimum(note['startY'])
        self.ui.Y_start.setMaximum(note['endY'])

    def show_notes(self, notes):
        self.ui.model = QtGui.QStandardItemModel(self.ui.listView)
        if len(notes) <= 0:
            self.parent.dialog_info('選択可能なトレースノートがありません。\nアークタップを追加するにはトレースノートを追加する必要があります。')
            return False
        self.notes = notes
        for note in notes:
            text = 'start:' + str(note['startY']) + ' end:' + str(note['endY']) + ' stX:' + str(note['startX']) + ' enX:' + str(note['endX'])
            item = QtGui.QStandardItem(text)
            self.ui.model.appendRow(item)
        self.ui.listView.setModel(self.ui.model)
        return True
