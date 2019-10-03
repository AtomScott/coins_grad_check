import getpass
import os
import time

import mechanize
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def newChromeBrowser(headless=True, downloadPath=None):
    """ Helper function that creates a new Selenium browser """
    options = webdriver.ChromeOptions()
    if headless:
        options.add_argument('headless')
    if downloadPath is not None:
        prefs = {}
        if not os.path.exists(downloadPath):
            os.makedirs(downloadPath)
        prefs["profile.default_content_settings.popups"]=0
        prefs["download.default_directory"]=downloadPath
        options.add_experimental_option("prefs", prefs)
    browser = webdriver.Chrome(options=options, executable_path='./chromedriver')
    return browser

id = input('id: ')
password = getpass.getpass()

driver = newChromeBrowser(headless=True, downloadPath=os.getcwd())
driver.get('https://twins.tsukuba.ac.jp/campusweb/campusportal.do')
#
# ID/PASSを入力
id_form = driver.find_element_by_name('userName')
id_form.send_keys(id)
password_form = driver.find_element_by_name('password')
password_form.send_keys(password)

time.sleep(1)

# ログインボタンをクリック
login_button = driver.find_element_by_xpath('//span[text()="ログイン"]')
login_button.click()

time.sleep(3)

# ページ遷移
button = driver.find_element_by_xpath('//div[img/@src="/campusweb/theme/default/newportal/image/icon/note.png"]')
button.click()

time.sleep(3)

# ページ遷移
button = driver.find_element_by_xpath('//span[img/@src="/campusweb/theme/default/newportal/image/icon/func_refer5.gif"]')
button.click()

time.sleep(3)

# Download
iframe = driver.find_element_by_name('portlet-body')
driver.switch_to.frame(iframe)
driver.find_element_by_xpath("//input[@type='button']").click()
