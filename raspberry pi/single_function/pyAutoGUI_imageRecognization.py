#!/usr/bin/env python3
# coding:utf-8
import pyautogui
import time
import re

PATH_IMG_MATSUI = '/home/pi/Documents/raspberrypi/single_function/images/'

LOCATE_ELEMENTS_IMG = {
    'IMG_TAB_FUTURE_OP': PATH_IMG_MATSUI + 'future_op.png',
    'IMG_NAV_FUTURE_NEW': PATH_IMG_MATSUI + 'nav_future_new.png',
    'IMG_FUTURE_NEW_ORDER_TITLE': PATH_IMG_MATSUI + 'title_future_new_order.png',
    'IMG_FUTURE_MINI_LINK': PATH_IMG_MATSUI + 'future_mini_link.png',
    'IMG_ORDER_INPUT_BUY': PATH_IMG_MATSUI + 'order_input_buy.png',
    'IMG_ORDER_INPUT_SELL': PATH_IMG_MATSUI + 'order_input_sell.png',
    'IMG_INPUT_SHEET': PATH_IMG_MATSUI + 'order_input_sheet.png',
    'IMG_INPUT_MARKET_ORDER': PATH_IMG_MATSUI + 'order_input_market_order.png',
    'IMG_INPUT_CONFIRM': PATH_IMG_MATSUI + 'order_input_confirm.png'
}

BROWSER_ACTION_MATSUI = {
    'HOME': {
        'LOCATE_CLICK_1': LOCATE_ELEMENTS_IMG['IMG_TAB_FUTURE_OP']
    },
    'FUTURE_OP': {
        'LOCATE_CLICK_1': LOCATE_ELEMENTS_IMG['IMG_NAV_FUTURE_NEW']
    },
    'FUTURE_OP_NEW': {
        'LOCATE_CLICK_1': LOCATE_ELEMENTS_IMG['IMG_FUTURE_NEW_ORDER_TITLE'],
        'SCROLL_1': -100,
        'LOCATE_CLICK_2': LOCATE_ELEMENTS_IMG['IMG_FUTURE_MINI_LINK']
    },
    'FUTURE_ORDER_FORM': {
        'LOCATE_CLICK_1_BUY': LOCATE_ELEMENTS_IMG['IMG_ORDER_INPUT_BUY'],
        'LOCATE_CLICK_1_SELL': LOCATE_ELEMENTS_IMG['IMG_ORDER_INPUT_SELL'],
        'LOCATE_CLICK_2': LOCATE_ELEMENTS_IMG['IMG_INPUT_SHEET'],
        'KEY_PRESS_SHEET_NUM': '1',
        'LOCATE_CLICK_3': LOCATE_ELEMENTS_IMG['IMG_INPUT_MARKET_ORDER'],
        'SCROLL_1': -100,
        'LOCATE_CLICK_4': LOCATE_ELEMENTS_IMG['IMG_INPUT_CONFIRM']
    }
}

for page in BROWSER_ACTION_MATSUI:
    for action in BROWSER_ACTION_MATSUI[page]:
        if 'LOCATE_CLICK' in action:
            while True:
                if pyautogui.locateCenterOnScreen(BROWSER_ACTION_MATSUI[page][action]) != None:
                    position_x, position_y = pyautogui.locateCenterOnScreen(BROWSER_ACTION_MATSUI[page][action])
                    pyautogui.click(position_x, position_y)
                    break
                else:
                    time.sleep(1)
        elif 'SCROLL' in action:
            pyautogui.scroll(BROWSER_ACTION_MATSUI[page][action])
        elif 'KEY_PRESS' in action:
            pyautogui.press(BROWSER_ACTION_MATSUI[page][action])
        else:
            print('不明なアクションが登録されています。') 
