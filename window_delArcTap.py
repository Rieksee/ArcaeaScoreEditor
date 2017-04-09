# -*- coding: utf-8 -*-
from ui_delArcTap import Ui_DelArcTap
from PyQt5.QtWidgets import *
from PyQt5 import QtGui, QtCore

class window_delArcTap(QWidget):
    def __init__(self, notes, parent=None, isolate=True):
        if not isolate:
            super(window_delArcTap, self).__init__(parent)
        else:
            super(window_delArcTap, self).__init__(None)
        self.ui = Ui_DelArcTap()
        self.parent = parent
        self.ui.setupUi(self)
        self.error = False
        self.selectedRow = None
        self.selectedNote = None
        self.tapSelecting = False
        if not self.show_notes(notes):
            self.error = True

    def select_note(self):
        if not self.tapSelecting:
            note = self.notes[self.selectedRow]
            if not self.show_taps(note):
                self.close()
        else:
            self.note_deleteChk()

    def selected(self, index):
        self.selectedRow = index.row()

    def show_notes(self, notes):
        self.ui.model = QtGui.QStandardItemModel(self.ui.listView)
        if len(notes) <= 0:
            self.parent.dialog_info('選択可能なトレースノートがありません。')
            return False
        self.notes = notes
        for note in notes:
            text = 'start:' + str(note['startY']) + ' end:' + str(note['endY']) + ' stX:' + str(note['startX']) + ' enX:' + str(note['endX'])
            item = QtGui.QStandardItem(text)
            self.ui.model.appendRow(item)
        self.ui.listView.setModel(self.ui.model)
        return True

    def show_taps(self, note):
        if len(note['arcTaps']) < 1:
            self.parent.dialog_info('アークタップがありません。')
            return False
        self.ui.model = QtGui.QStandardItemModel(self.ui.listView)
        for tap in note['arcTaps']:
            item = QtGui.QStandardItem(str(tap))
            self.ui.model.appendRow(item)
        self.ui.listView.setModel(self.ui.model)
        self.selectedRow = None
        self.selectedNote = note
        self.tapSelecting = True
        return True

    def note_deleteChk(self):
        indexOfNoteToDelete = []
        if self.selectedRow is None:
            self.parent.dialog_critical("エラー: ノーツの削除に失敗しました。")
            self.close()
            return False
        count = 0
        for note in self.parent.proj['notes']:
            if note == self.selectedNote:
                indexOfNoteToDelete.append(count)
                break
            count = count + 1
        else:
            self.parent.dialog_critical("エラー: ノーツの削除に失敗しました。")
            self.close()
            return False
        indexOfNoteToDelete.append(self.selectedRow)
        if len(indexOfNoteToDelete) != 2:
            self.parent.dialog_critical("エラー: ノーツの削除に失敗しました。")
            self.close()
            return False
        try:
            self.parent.proj['notes'][indexOfNoteToDelete[0]]['arcTaps'].pop(indexOfNoteToDelete[1])
        except:
            self.parent.dialog_critical("エラー: ノーツの削除に失敗しました。")
            self.close()
            return False
        if len(self.parent.proj['notes'][indexOfNoteToDelete[0]]['arcTaps']) < 1:
            self.parent.proj['notes'][indexOfNoteToDelete[0]]['type'] = 4
        self.parent.dialog_info("ノーツを削除しました。")
        self.parent.window_update()
        self.close()
        return True
