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


# 先物・オプション注文入力

# 注文条件確認


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
 

    # 先物・オプション注文入力


    # 注文条件確認
