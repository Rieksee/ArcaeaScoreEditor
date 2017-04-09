# -*- coding: utf-8 -*-
import sys
import os
from cx_Freeze import setup, Executable

base = None

#コンソールアプリの場合は↓この行コメントアウト or 削除すること
# if sys.platform == 'win32' : 
base = 'Win32GUI'

# exe にしたい python ファイルを指定
exe = Executable(
	script='ArcaeaScoreEditor.py',
	icon="res\\ase.ico",
	base=base,
	)

# セットアップ
setup(name = 'Arcaea score editor',
    version = '0.0.3',
    description = 'test',
    executables = [exe])
