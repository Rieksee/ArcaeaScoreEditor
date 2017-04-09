# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QFileDialog, QTreeWidgetItem, QApplication
from PyQt5 import QtCore, QtGui, QtWidgets
from ui_main import Ui_mainWindow
from window_longNote import window_longNote
from window_newScore import window_newScore
from window_tapNote import window_tapNote
from window_arcNote import window_arcNote
from window_quesArcTap import window_quesArcTap
from window_timing import window_timing
from window_downloadProgress import window_downloadProgress
from window_about import window_about
from urllib.error import URLError, HTTPError
from urllib.request import Request, urlopen, urlretrieve
from math import ceil
import json
import os
import urllib
import sys
import time
import codecs
from collections import OrderedDict


class mainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(mainWindow, self).__init__(parent)
        self.ui = Ui_mainWindow()
        self.ui.setupUi(self)
        # self.ui.treeWidget.header().setResizeMode(QtGui.QHeaderView.ResizeToContents)
        self.ui.treeWidget.header().resizeSection(1, 70)
        self.ui.treeWidget.header().resizeSection(2, 70)
        self.path = None
        self.file_opened = False
        self.version = "0.0.3"
        self.is32 = 1
        self.updateChk_URL = ""
        self.proj = OrderedDict()
        self._translate = QtCore.QCoreApplication.translate
        self.title = 'Arcaea Score Editor'
        self.isModified = False
        self.file_newline = '\n'
        self.file_ext = {}
        self.count = 0
        self.error = False
        self.keyfile = "key.txt"
        self.file_ext['arcaea'] = '.aff'
        self.file_ext['proj'] = '.arcscoproj'
        self.note_types = {
            1: "timing",
            2: "single Tap",
            3: "long note",
            4: "arc Note without arctap",
            5: "arc Note with arctap"
        }
        # self.updateChk()

    def getPath(self):
        if getattr(sys, 'frozen', False):
            # frozen
            return os.path.dirname(sys.executable)
        else:
            # unfrozen
            return os.path.dirname(os.path.realpath(__file__))

    def download_progress(self, blocknum, blocksize, totalsize):
        readsofar = blocknum * blocksize
        if totalsize > 0:
            percent = readsofar * 1e2 / totalsize
            self.window_downloadProgress.set_val(ceil(percent))
            QApplication.processEvents()
            if readsofar >= totalsize: # near the end
                self.window_downloadProgress.close()
                self.window_downloadProgress = None
        else: # total size is unknown
            pass

    def reset(self):
        self.window_newSet = window_newScore(self)
        self.window_newSet.show()
        self.proj = OrderedDict()
        self.path_set(None)
        self.file_opened = True

    def menu_fileOpen(self):
        path = self.dialog_file(False, 'プロジェクトファイルを開く')
        if path == "":
            # self.dialog_info('中断しました。')
            return
        with open(path, "r") as f:
            try:
                self.proj = json.loads(f.read(), object_pairs_hook=OrderedDict)
            except Exception as e:
                res = self.dialog_critical('読み込みに失敗しました。')
                self.proj = OrderedDict()
                return False
            self.path_set(path)
            self.file_opened = True
            self.window_update()
            self.file_unmodified()
            return True

    def menu_save(self):
        if self.path is None:
            self.menu_saveAs()
        else:
            self.save(self.path)
        self.file_unmodified()

    def menu_saveAs(self,):
        path = self.dialog_file(True, '名前をつけて保存')
        if path == "":
            # self.dialog_info('保存を中断しました。')
            return
        if self.save(path):
            self.path_set(path)
        self.file_unmodified()

    def menu_import(self):
        if self.isModified:
            if QMessageBox.No == self.dialog_alert("ファイルが変更されています。変更を破棄して新しくファイルを読み込みますか？"):
                return
        path = self.dialog_file(False, 'Arcaea譜面ファイルをインポート', self.file_ext['arcaea'])
        if path == "":
            # self.dialog_info('読み込みを中断しました。')
            return
        with open(path, "r") as f:
            try:
                ff = f.read()
            except:
                self.dialog_critical('読み込みに失敗しました。')
                self.proj = OrderedDict()
                return False
            proj = self.proj_read_original(ff)
            if not proj:
                self.dialog_critical('ファイルの解析に失敗しました。')
                self.proj = OrderedDict()
                return False
            self.proj = proj
            self.dialog_info('ファイルを読み込みました。')
            self.window_update()
            self.path_set(None)
            self.file_unmodified()
            self.file_opened = True
            return True
        self.file_opened = True

    def menu_export(self):
        if not self.file_opened:
            self.dialog_critical('出力すべきファイルがありません。')
            return
        path = self.dialog_file(True, 'Arcaea譜面ファイルをエクスポート', self.file_ext['arcaea'])
        if path == "":
            # self.dialog_info('出力を中断しました。')
            return
        if not self.proj_write_original(path):
            self.dialog_critical('ファイルの出力に失敗しました。')
            return
        self.file_unmodified()

    def user_quit(self):
        if not self.isModified:
            return True
        if QMessageBox.Yes == self.dialog_alert('ファイルが変更されています。保存せずに終了しますか？'):
            return True
        else:
            return False

    def menu_quit(self):
        if self.user_quit():
            self.close()

    def closeEvent(self, event):
        if self.user_quit():
            event.accept()
        else:
            event.ignore()

    def menu_about(self):
        self.window_about = window_about(self)
        self.window_about.show()

    def note_normalLong(self):
        if not self.file_opened:
            self.file_alert_notOpened()
            return
        self.window_longNote = window_longNote(self)
        self.window_longNote.show()

    def note_normalTap(self):
        if not self.file_opened:
            self.file_alert_notOpened()
            return
        self.window_tapNote = window_tapNote(self)
        self.window_tapNote.show()

    def note_ArcTap(self):
        if not self.file_opened:
            self.file_alert_notOpened()
            return
        self.window_quesArcTap = window_quesArcTap(self)
        self.window_quesArcTap.show()

    def note_ArcNote(self):
        if not self.file_opened:
            self.file_alert_notOpened()
            return
        self.window_arcNote = window_arcNote(self)
        self.window_arcNote.show()

    def note_timing(self):
        if not self.file_opened:
            self.file_alert_notOpened()
            return
        self.window_timing = window_timing(self)
        self.window_timing.show()

    def note_delete(self):
        if not self.file_opened:
            self.file_alert_notOpened()
            return
        notes = self.find_checked_note()
        count = len(notes.values())
        if count < 1:
            self.dialog_info("削除するノーツが選択されていません。")
            return
        elif count > 10:
            text = "本当に" + str(count) + "個のノーツを削除しますか？"
        else:
            text = "本当に以下のノーツを削除しますか？\n"
            for note in notes.values():
                text = text + note + "\n"
        if QMessageBox.Yes != self.dialog_alert(text):
            return
        keys = list(notes.keys())
        keys.sort()
        keys.reverse()
        for key in keys:
            self.proj['notes'].pop(key)
        self.window_update()

    def action_selectAll(self):
        self.action_check(True)

    def action_unSelectAll(self):
        self.action_check(False)

    def action_check(self, check):
        if not self.file_opened:
            return
        root = self.ui.treeWidget.invisibleRootItem()
        signal_count = root.childCount()
        if check:
            state = QtCore.Qt.Checked
        else:
            state = QtCore.Qt.Unchecked

        for i in range(signal_count):
            signal = root.child(i)
            if signal.text(0) != "notes":
                continue
            checked_sweeps = list()
            num_children = signal.childCount()

            for n in range(num_children):
                child = signal.child(n)
                child.setCheckState(0, state)

    def find_checked_note(self):
        checked = {}
        root = self.ui.treeWidget.invisibleRootItem()
        signal_count = root.childCount()

        for i in range(signal_count):
            signal = root.child(i)
            if signal.text(0) != "notes":
                continue
            checked_sweeps = list()
            num_children = signal.childCount()

            for n in range(num_children):
                child = signal.child(n)
                if child.checkState(0) == QtCore.Qt.Checked:
                    checked[n] = child.text(0)
        return checked

    def window_update(self):
        # QtGui.QTreeWidgetItemModel(self.ui.treeWidget)
        items = []
        self.ui.treeWidget.clear()
        for proj in self.proj.items():
            item = QTreeWidgetItem([str(proj[0])])
            settedItem = self.window_tree_itemSet_loop(item, proj[1])
            items.append(settedItem)
        for item in items:
            self.ui.treeWidget.addTopLevelItem(item)
        # self.window_tree_itemSet_loop(self.ui.treeWidget, self.proj)
        self.file_modified()

    def window_tree_itemSet_loop(self, parent, proj):
        # print(proj)
        if type(proj) == dict:
            for item in proj.items():
                label = self.window_tree_item(item[0])
                child = self.window_tree_itemSet_loop(label, item[1])
                parent.addChild(label)
        elif type(proj) == OrderedDict:
            for item in proj.items():
                label = self.window_tree_item(item[0])
                child = self.window_tree_itemSet_loop(label, item[1])
                parent.addChild(label)
        elif type(proj) == tuple:
            # if len(proj) != 2:
            self.dialog_critical("タプルが出現しました")
        elif type(proj) == list:
            if self.all_item_of_list_is_int(proj):
                text = ""
                for item in proj:
                    text = text + str(item) + ", "
                label = self.window_tree_item(text)
                parent.addChild(label)
            else:
                count = 0
                for item in proj:
                    count = count + 1
                    label = self.window_tree_item("No." + str(count) + " " + self.note_types[item['type']], True)
                    label = self.window_tree_addButton(label)
                    self.window_tree_itemSet_loop(label, item)
                    parent.addChild(label)
        else:
            # print(type(proj))
            parent.addChild(self.window_tree_item(proj))
        return parent

    def window_tree_item(self, text, edit=False):
        if type(text) in [int, float, bool]:
            text = str(text)
        item = QTreeWidgetItem()
        item.setText(0, text)
        # editButton = QtWidgets.QPushButton("edit button")
        # editButton.setObjectName("editButton")
        # self.ui.treeWidget.setItemWidget(item, 0, editButton)
        # if edit:
        #     item.setFlags(item.flags() | QtCore.Qt.ItemIsEditable)
        return item

    def window_tree_addButton(self, item):
        item.setCheckState(0, QtCore.Qt.Unchecked);
        return item

    def all_item_of_list_is_int(self, lis):
        for item in lis:
            if type(item) != int:
                return False
        return True

    def save(self, path):
        if path == '':
            # self.dialog_info('保存を中断しました。')
            return
        if self.proj is None or len(self.proj) == 0:
            res = self.dialog_alert('何もデータが登録されていません。本当に保存しますか？')
            if res == QMessageBox.No:
                return False
            self.proj = OrderedDict()
        self.proj_write(path)
        self.file_unmodified()
        return True

    def dialog_question(self, message):
        return self.messageBox(1, message)

    def dialog_info(self, message):
        return self.messageBox(2, message)

    def dialog_alert(self, message):
        return self.messageBox(3, message)

    def dialog_critical(self, message):
        return self.messageBox(4, message)

    def messageBox(self, typeId, message, parent=None):
        if parent is None:
            parent = self
        msg = QMessageBox()
        msg.setIconPixmap(QtGui.QPixmap(":/arcaea_main/res/ase-256x256.png"))
        if typeId == 1:
            msg = msg.question(parent, 'question', message, QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        elif typeId == 2:
            msg = msg.information(parent, 'info', message,  QMessageBox.Ok, QMessageBox.Ok)
        elif typeId == 3:
            msg = msg.warning(parent, 'warning', message,  QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        elif typeId == 4:
            msg = msg.critical(parent, 'ERROR', message,  QMessageBox.Ok, QMessageBox.Ok)
        return msg

    def sort(self):
        ret = {}
        ret['musicInfo'] = self.proj['musicInfo']
        for note in self.proj['notes']:
            pass
        return json.dumps(ret)

    def dialog_file(self, save, name, ext=None):
        if ext is None:
            ext = self.file_ext['proj']
        if save:
            fname = QFileDialog.getSaveFileName(self, name, 'default' + ext, '*' + ext)
        else:
            fname = QFileDialog.getOpenFileName(self, name, filter='*' + ext)
        return fname[0]

    def path_set(self, path):
        self.path = path
        if path is None:
            self.title = 'Arcaea Score Editor (untitled)'
        else:
            self.title = 'Arcaea Score Editor' + ' (' + path + ')'
        self.set_title()

    def set_title(self):
        self.setWindowTitle(self._translate("mainWindow", self.title))
        return True

    def proj_read_original(self, text):
        res = OrderedDict()
        res['musicInfo'] = OrderedDict()
        res['notes'] = []
        lis = text.split("\n")
        for row in lis:
            note = {}
            if row.startswith("AudioOffset:"):
                num = row.lstrip("AudioOffset:")
                try:
                    num = int(num)
                except:
                    continue
                res['musicInfo']['AudioOffset'] = num
                continue
            elif row.startswith("timing("):
                timing = self.stripAndSplit(row, "timing(", ");", ",")
                note['type'] = 1
                note['startY'] = int(timing[0])
                note['BPM'] = float(timing[1])
                note['time'] = float(timing[2])
            elif row.startswith("("):
                tap = self.stripAndSplit(row, "(", ");", ",")
                note['type'] = 2
                note['startY'] = int(tap[0])
                note['startX'] = int(tap[1])
            elif row.startswith("hold("):
                hold = self.stripAndSplit(row, "hold(", ");", ",")
                note['type'] = 3
                note['startY'] = int(hold[0])
                note['endY'] = int(hold[1])
                note['startX'] = int(hold[2])
            elif row.startswith("arc("):
                if row not in ')[':
                    arc = self.stripAndSplit(row, "arc(", ");", ",")
                    note['type'] = 4
                    note['startY'] = int(arc[0])
                    note['endY'] = int(arc[1])
                    note['startX'] = float(arc[2])
                    note['endX'] = float(arc[3])
                    note['curve'] = str(arc[4])
                    note['startZ'] = float(arc[5])
                    note['endZ'] = float(arc[6])
                    note['color'] = int(arc[7])
                    note['option'] = str(arc[8])
                    if str(arc[9]).lower() == "false":
                        arc[9] = False
                    else:
                        arc[9] = True
                    note['isTrace'] = arc[9] 
                    note['arcTaps'] = []
                else:
                    arc = self.stripAndSplit(row, "arc(", "];", ')[')
                    sky = arc[0].split(',')
                    note['type'] = 5
                    note['startY'] = int(sky[0])
                    note['endY'] = int(sky[1])
                    note['startX'] = float(sky[2])
                    note['endX'] = float(sky[3])
                    note['curve'] = str(sky[4])
                    note['startZ'] = float(sky[5])
                    note['endZ'] = float(sky[6])
                    note['color'] = int(sky[7])
                    note['option'] = str(sky[8])
                    if str(sky[9]).lower() == "false":
                        sky[9] = False
                    else:
                        sky[9] = True
                    note['isTrace'] = sky[9] 
                    taps = arc[1].split(',')
                    note['arcTaps'] = []
                    for tap in taps:
                        tap = tap.lstrip("arctap(")
                        tap = tap.rstrip(")")
                        note['arcTaps'].append(int(tap))
            else:
                continue
            res['notes'].append(note)
        if len(res['notes']) < 1:
            return False
        return res

    def proj_read(self, text):
        try:
            obj = json.loads(text, object_pairs_hook=OrderedDict)
            retObj = {}
            retObj['musicInfo'] = obj['musicInfo']
            retObj['notes'] = []
            for one in obj['notes']:
                if one['type'] == 1:
                    try:
                        one['time']
                    except:
                        one['time'] = one['tem']
                        del one['tem']
                        self.file_modified()
                retObj['notes'].append(one)
            return retObj
        except:
            return False

    def proj_write_original(self, path):
        try:
            res = ""
            res = res + 'AudioOffset:' + str(self.proj['musicInfo']['AudioOffset']) + self.file_newline
            res = res + '-' + self.file_newline
            for note in self.proj['notes']:
                if note['type'] == 1:
                    try:
                        res = res + 'timing(' + str(note['startY']) + ',' + str(note['BPM']) + ',' + str(note['time']) + ');' + self.file_newline
                    except:
                        res = res + 'timing(' + str(note['startY']) + ',' + str(note['BPM']) + ',' + str(note['tem']) + ');' + self.file_newline
                elif note['type'] == 2:
                    res = res + '(' + str(note['startY']) + ',' + str(note['startX']) + ');' + self.file_newline
                elif note['type'] == 3:
                    res = res + 'hold(' + str(note['startY']) + ',' + str(note['endY']) + ',' + str(note['startX']) + ');' + self.file_newline
                elif note['type'] == 4:
                    res = res + 'arc(' + str(note['startY']) + ',' + str(note['endY']) + ',' + str(note['startX']) + ',' + str(note['endX']) +\
                     ',' + str(note['curve']) + ',' + str(note['startZ']) + ',' + str(note['endZ']) + ',' + str(note['color']) + ',' +\
                     str(note['option']) + ',' + str(note['isTrace']) + ');' + self.file_newline
                elif note['type'] == 5:
                    res = res + 'arc(' + str(note['startY']) + ',' + str(note['endY']) + ',' + str(note['startX']) + ',' + str(note['endX']) +\
                     ',' + str(note['curve']) + ',' + str(note['startZ']) + ',' + str(note['endZ']) + ',' + str(note['color']) + ',' +\
                     str(note['option']) + ',' + str(note['isTrace']) + ')['
                    for arctap in note['arcTaps']:
                        res = res + 'arctap(' + str(arctap) + '),'
                    res = res.rstrip(',')
                    res = res + '];' + self.file_newline
            res = res.rstrip("\n")
            with open(path, 'w') as f:
                f.write(res)
            self.file_unmodified()
            return True
        except:
            return False

    def proj_write(self, path):
        with open(path, 'w') as f:
            f.write(str(json.dumps(self.proj, indent=4)))
        return True

    def stripAndSplit(self, text, l, r, split):
        anly = text.lstrip(l)
        anly = anly.rstrip(r)
        return anly.split(split)

    def file_modified(self):
        if self.isModified:
            return False
        self.isModified = True
        self.title = self.title + " *"
        return self.set_title()

    def file_unmodified(self):
        self.isModified = False
        self.title = self.title.rstrip(' *')
        return self.set_title()

    def proj_append(self, newNote):
        Y = newNote['startY']
        proj = OrderedDict()
        proj['musicInfo'] = self.proj['musicInfo']
        proj['notes'] = []
        addNote = True
        for note in self.proj['notes']:
            if note['startY'] > Y and addNote:
                proj['notes'].append(newNote)
                addNote = False
            proj['notes'].append(note)
        if addNote:
            proj['notes'].append(newNote)
        self.proj = proj
        self.dialog_info('ノーツを追加しました。')
        self.window_update()
        return True

    def file_alert_notOpened(self):
        self.dialog_info('ファイルが開かれていません！新規で作成する場合はメニューからnewを選択してください。')
