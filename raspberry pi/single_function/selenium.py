#!/usr/bin/python3
# coding:utf-8
import sys
import os
sys.path.append('/usr/bin/python3')
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.binary_location = '/usr/bin/chromium-browser'
browser = webdriver.Chrome(executable_path='/usr/bin/chromedriver',options=chrome_options)

URL = 'https://www.google.com/'
INPUT = '//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input'
WORD = 'test'

if __name__ == '__main__':
    browser.get(URL)
    time.sleep(3)

    Field = browser.find_element_by_xpath(INPUT)
    Field.click()
    Field.send_keys(WORD)
    Field.send_keys(Keys.RETURN)