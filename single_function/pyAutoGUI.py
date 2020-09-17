#!/usr/bin/env python3
# coding:utf-8
import pyautogui
import time
import re
from subprocess import Popen, PIPE

time.sleep(5)

# コマンド
cmd_matsui = 'xwininfo,-name,松井証券【先物ＯＰ】 - Chromium'
p = Popen(cmd_matsui.split(','),stdout = PIPE, stderr = PIPE)
ret = str(p.communicate())
coord = re.search('X:\s+(\d+)[^Y]+Y:\s+(\d+)',ret)

window_x,window_y = int(coord.groups()[0]) ,int(coord.groups()[1])
print(window_x,window_y)

cursor_position_x, cursor_position_y = pyautogui.position()
print(cursor_position_x, cursor_position_y)

