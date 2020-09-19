#!/usr/bin/python3
# coding:utf-8
import matsui_login
import matsui_move_to_confirm

# 松井証券のログインから注文確認画面まで
matsui_login.auto_operation()
matsui_move_to_confirm.auto_operation()

# 注文する
# matsui_move_to_confirm.auto_operation_order() 
