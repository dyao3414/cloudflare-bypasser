
from typing import Set
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from pyquery import PyQuery as pq
from selenium.webdriver.common.by import By
import time

options = webdriver.ChromeOptions()
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_experimental_option('excludeSwitches', ['enable-automation'])
# options.add_argument('window-size=1200x600'); 
s=Service('chromedriver.exe')
browser=webdriver.Chrome(service=s,options=options)
# browser.maximize_window()
browser.get(r'https://govsalaries.com/salaries/VA/william-mary-college?page=2')
doc=pq(browser.page_source)

a=browser.find_elements(By.CLASS_NAME,"btn.btn-sm.btn-block.btn-primary")
# b=[i.attr('href') for i in a]
# b=list(set(b))
# print(b)
browser.close
domian='https://govsalaries.com/'
for i in a:
    # browser.get(domian+i)
    i.click()
    handle=browser.current_window_handle
    print(handle)
    browser.service.stop()
    time.sleep(5)
    browser=webdriver.Chrome(service=s,options=options)
    browser.switch_to.window(handle)
    # r=requests.get(domian+i, headers={
    #         "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36"})

    # print(i.attr('href'))
a=browser.find_elements(By.CLASS_NAME,"btn.btn-sm.btn-block.btn-primary")
# print(a)
# for element in a:
#     # url=element.get_attribute("href")
#     # browser.get(url)
#     # print(url)
#     # input()
#     element.click()

# with open('./stealth.min.js') as f:
#     js = f.read()

# browser.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
#     "source": js
# })
# browser.close

