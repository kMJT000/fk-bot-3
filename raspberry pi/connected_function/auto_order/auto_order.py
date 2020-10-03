#!/usr/bin/python3
# coding:utf-8
import matsui_login
import matsui_move_to_confirm

# 松井証券のログインから注文確認画面まで
# pyautoguiのソースコード（/home/pi/.local/lib/python3.7/site-packages/pyscreeze/__init__.py）もいじってる（confidenceの値、grayscaleをオンにする）
matsui_login.auto_operation()
matsui_move_to_confirm.auto_operation()

# 注文する
# matsui_move_to_confirm.auto_operation_order() 
