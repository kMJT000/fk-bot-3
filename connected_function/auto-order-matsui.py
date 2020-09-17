#!/usr/bin/python3
# coding:utf-8
import sys
import os
sys.path.append('/usr/bin/python3')
import time
import pyautogui
import re

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from subprocess import Popen, PIPE

chrome_options = Options()
chrome_options.binary_location = '/usr/bin/chromium-browser'
browser = webdriver.Chrome(executable_path='/usr/bin/chromedriver',options=chrome_options)

# URL
URL_LOGIN = 'https://www.deal.matsui.co.jp/ITS/login/MemberLogin.jsp'

# フォーム画面
USER_ID = '61952577'
USER_PASS = 'a4173080'
TRADE_PASS = 'e0767545'

# ロード待ち時間(秒)
wait_time = 7

# ログイン画面
LOGIN_INPUT_FORM_CLASS_NAME = 'm-frm-txt'
LOGIN_INPUT_FORM_ID_NAME_PASS = 'passwd'
LOGIN_RADIO_BUTTON_EASY_ORDER = 'input[type="radio"][value="1"]'
LOGIN_SELECTOR_SUBMIT = '.g-non-rwd form'

# 取引暗証番号事前入力
PREV_TRADE_PASS_ID_NAME_INPUT_FORM = 'pinNo'
PREV_TRADE_PASS_BUTTON_NEXT = 'input[type="image"][alt="次へ"]'

# ホーム → 新規注文入力
CMD_WINDOW_INFO_MATSUI_HOME = 'xwininfo,-name,松井証券【ホーム】 - Chromium'
POSITION_REGEX = 'X:\s+(\d+)[^Y]+Y:\s+(\d+)'
TAB_FUTURE_OP_POSITION_X, TAB_FUTURE_OP_POSITION_Y = 405, 150
NAV_FUTURE_NEW_POSITION_X, NAV_FUTURE_NEW_POSITION_Y = 40, 235
FUTURE_MINI_ORDER_LINK_POSITION_X, FUTURE_MINI_ORDER_LINK_POSITION_Y = 300, 970

# 先物・オプション注文入力
FUTURE_MINI_ORDER_RADIO_BUY_POSITION_X, FUTURE_MINI_ORDER_RADIO_BUY_POSITION_Y = 346, 550
FUTURE_MINI_ORDER_RADIO_SELL_POSITION_X, FUTURE_MINI_ORDER_RADIO_SELL_POSITION_Y = FUTURE_MINI_ORDER_RADIO_BUY_POSITION_X, FUTURE_MINI_ORDER_RADIO_BUY_POSITION_Y + 23
FUTURE_MINI_ORDER_SHEET_POSITION_X, FUTURE_MINI_ORDER_SHEET_POSITION_Y = FUTURE_MINI_ORDER_RADIO_BUY_POSITION_X + 134, FUTURE_MINI_ORDER_RADIO_BUY_POSITION_Y + 58
FUTURE_MINI_ORDER_MARKET_POSITION_X, FUTURE_MINI_ORDER_MARKET_POSITION_Y = FUTURE_MINI_ORDER_RADIO_BUY_POSITION_X, FUTURE_MINI_ORDER_RADIO_BUY_POSITION_Y + 118
FUTURE_MINI_ORDER_CONFIRM_POSITION_X, FUTURE_MINI_ORDER_CONFIRM_POSITION_Y = FUTURE_MINI_ORDER_RADIO_BUY_POSITION_X, FUTURE_MINI_ORDER_RADIO_BUY_POSITION_Y + 370

# 注文条件確認
ORDER_CONFIRM_BUTTON_POSITION_X, ORDER_CONFIRM_BUTTON_POSITION_Y = 0, 0

def auto_click(position_x,position_y,wait_time):
    pyautogui.click(position_x, position_y)
    time.sleep(wait_time)

if __name__ == '__main__':
    # ログイン画面
    browser.get(URL_LOGIN)

    login_element_input_form = browser.find_element_by_class_name(LOGIN_INPUT_FORM_CLASS_NAME)
    login_element_input_form_pass = browser.find_element_by_id(LOGIN_INPUT_FORM_ID_NAME_PASS)
    login_element_radio_button_easy_order = browser.find_elements_by_css_selector(LOGIN_RADIO_BUTTON_EASY_ORDER)
    login_element_submit = browser.find_element_by_css_selector(LOGIN_SELECTOR_SUBMIT)
    
    login_element_input_form.send_keys(USER_ID)
    login_element_input_form_pass.send_keys(USER_PASS)
    login_element_radio_button_easy_order[0].click()
    login_element_submit.submit()

    # 取引暗証番号事前入力
    prev_trade_pass_element_input_form = browser.find_element_by_id(PREV_TRADE_PASS_ID_NAME_INPUT_FORM)
    prev_trade_pass_element_next_button = browser.find_elements_by_css_selector(PREV_TRADE_PASS_BUTTON_NEXT)

    prev_trade_pass_element_input_form.send_keys(TRADE_PASS)
    prev_trade_pass_element_next_button[0].click()
    
    # ホーム → 先物OP
    cmd_result_std = Popen(CMD_WINDOW_INFO_MATSUI_HOME.split(','),stdout = PIPE, stderr = PIPE)
    window_position = re.search(POSITION_REGEX,str(cmd_result_std.communicate()))
    window_positon_x,window_positon_y = int(window_position.groups()[0]) ,int(window_position.groups()[1])

    tab_future_position_x, tab_future_home_position_y = window_positon_x + TAB_FUTURE_OP_POSITION_X, window_positon_y + TAB_FUTURE_OP_POSITION_Y
    nav_future_position_x, nav_future_home_position_y = window_positon_x + NAV_FUTURE_NEW_POSITION_X, window_positon_y + NAV_FUTURE_NEW_POSITION_Y
    link_future_mini_position_x, link_future_mini_position_y = window_positon_x + FUTURE_MINI_ORDER_LINK_POSITION_X, window_positon_y + FUTURE_MINI_ORDER_LINK_POSITION_Y

    auto_click(tab_future_position_x, tab_future_home_position_y, wait_time)
    auto_click(nav_future_position_x, nav_future_home_position_y, wait_time)
    auto_click(link_future_mini_position_x, link_future_mini_position_y, wait_time)

    # 先物・オプション注文入力
    new_radio_buy_position_x, new_radio_buy_position_y = window_positon_x + FUTURE_MINI_ORDER_RADIO_BUY_POSITION_X, window_positon_y + FUTURE_MINI_ORDER_RADIO_BUY_POSITION_Y
    new_radio_sell_position_x, new_radio_sell_position_y = window_positon_x + FUTURE_MINI_ORDER_RADIO_SELL_POSITION_X, window_positon_y + FUTURE_MINI_ORDER_RADIO_SELL_POSITION_Y
    sheet_num_position_x, sheet_num_position_y = window_positon_x + FUTURE_MINI_ORDER_SHEET_POSITION_X, window_positon_y + FUTURE_MINI_ORDER_SHEET_POSITION_Y
    market_order_position_x, market_order_position_y = window_positon_x + FUTURE_MINI_ORDER_MARKET_POSITION_X, window_positon_y + FUTURE_MINI_ORDER_MARKET_POSITION_Y
    confirm_button_mini_position_x, confirm_button_mini_position_y = window_positon_x + FUTURE_MINI_ORDER_CONFIRM_POSITION_X, window_positon_y + FUTURE_MINI_ORDER_CONFIRM_POSITION_Y

    auto_click(new_radio_buy_position_x, new_radio_buy_position_y, wait_time)
    auto_click(new_radio_sell_position_x, new_radio_sell_position_y, wait_time)
    auto_click(sheet_num_position_x, sheet_num_position_y, wait_time)
    auto_click(market_order_position_x, market_order_position_y, wait_time)
    auto_click(confirm_button_mini_position_x, confirm_button_mini_position_y, wait_time)

    # 注文条件確認
