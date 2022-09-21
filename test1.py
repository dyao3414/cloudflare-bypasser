

from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as Wait
from pyquery import PyQuery as pq 
import time
from selenium.webdriver.chrome.options import Options
import pandas as pd
import os
import proxy
import re

class CAPTCHA(Exception):
    pass
class WHITEPAGE(Exception):
    pass


os.system("C:\\Users\Di Yao\\Desktop\\chrome-r.bat")
# ip_list,port_list= proxy.get_proxy()
# ip_list,port_list=iter(ip_list),iter(port_list)
# ip=next(ip_list)
# port=next(port_list)
# time.sleep(3)
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
# chrome_options.add_argument(f'--proxy-server={ip}')
browser = webdriver.Chrome(options=chrome_options)

df=pd.DataFrame(columns=['Year','Full Name','Job Title','Annual Wage'])
def scrape(page_num):
    # print('current ip',ip)
    browser.get(fr'https://govsalaries.com/salaries/VA/william-mary-college?page={page_num}')
    ########
    if pq(browser.page_source)('title').text()=='Just a moment...': raise CAPTCHA
    #######
    time.sleep(3)
    pg=pq(browser.page_source)
    items=pg('tr a').items()
    urls=[item.attr('href') for item in items]
    urls=list(set(urls))
    domain='https://govsalaries.com'
    for url in urls:
        browser.get(domain+url)
        #########
        try:
            if pq(browser.page_source)('title').text()=='Just a moment...': raise CAPTCHA
        except Exception:
            browser.get(domain+url)
            if pq(browser.page_source)('title').text()=='Just a moment...': raise CAPTCHA
        #########
        Wait(browser, 60).until(EC.presence_of_element_located((By.CLASS_NAME, "table.table-condensed.FirstBold")))
        doc=pq(browser.page_source)
        print(len(doc('tbody:first tr')))
        try: 
            n=-1
            wage_column=doc('tbody:first tr').eq(n).text().split('\n')[1]
        except IndexError:
            n=-2
            wage_column=doc('tbody:first tr').eq(n).text().split('\n')[1]
        while re.findall('\d+',wage_column)==[]:
            n-=1
            wage_column=doc('tbody:first tr').eq(n).text().split('\n')[1]


        table=[doc('tbody:first tr').eq(0).text().split('\n')[1],doc('tbody:first tr').eq(1).text().split('\n')[1],doc('tbody:first tr').eq(2).text().split('\n')[1],wage_column]
 
        
        df.loc[len(df)]=table
        print(df.loc[len(df)-1])
    df.to_csv('test40.csv')
    
n=80
miss=[]
for num in range(n,172):
    try:
        scrape(num)
    except CAPTCHA:
        # time.sleep(300)
        print(num)
        miss.append(num)
        break
        print('ip invoked')
        browser.quit()
        # browser.close()
        n=num-1
        chrome_options = Options()
        chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
        ip=next(ip_list)
        port=next(port_list)
        chrome_options.add_argument(f'--proxy-server={ip}')
        browser = webdriver.Chrome(options=chrome_options) 
