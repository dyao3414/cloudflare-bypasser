import time
import requests
import subprocess
# from selenium import webdriver
# # from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import WebDriverWait as Wait
from pyquery import PyQuery as pq 
import os
from selenium.webdriver.chrome.options import Options
import proxy
import urllib.request , socket
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium import webdriver


socket.setdefaulttimeout(5)


ip_list=proxy.get_proxy()
print(ip_list)
works=[]

def is_bad_proxy(pip):    
    try:        
        proxy_handler = urllib.request.ProxyHandler({'http': pip})        
        opener = urllib.request.build_opener(proxy_handler)
        opener.addheaders = [('User-agent', 'Mozilla/5.0')]
        urllib.request.install_opener(opener)        
        sock=urllib.request.urlopen('https://api.ipify.org')
        # print(sock.read().decode('utf-8'))
    except urllib.error.HTTPError as e:        
        print('Error code: ', e.code)
        return e.code
    except Exception as detail:

        print( "ERROR:", detail)
        return 1
    return 0

for item in ip_list:
    if is_bad_proxy(item):
        print ("Bad Proxy", item)
    else:
        works.append(item)
print(works)

for i in works:
    print(i)
    p=subprocess.Popen([
        r'C:\Users\Di Yao\AppData\Local\Google\Chrome\Application\chrome.exe',
        '--remote-debugging-port=9222',
        '--user-data-dir={}'.format(r"C:\selenium\ChromeProfile",
        '--proxy-server={}'.format(i))
        ])
    chrome_options = Options()
    chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
    chrome_options.add_argument("--proxy-server={}".format(i))
    browser = webdriver.Chrome(options=chrome_options)
    browser.get('https://api.ipify.org/')
    browser.quit()
    input()
# '--proxy-server=%s' % PROXY





# ip='8.219.97.248:80'
# def hand_test():
#     # print(ip)
#     chrome_options = Options()
#     os.system("C:\\Users\Di Yao\\Desktop\\chrome-r.bat")
#     # chrome_options.add_argument(f'--proxy-server=http://{ip}')
#     # chrome_options.add_experimental_option("detach", True)
#     # chrome_options.add_argument('--ignore-ssl-errors=yes')
#     # chrome_options.add_argument('--ignore-certificate-errors')
#     chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
#     # chrome_options.add_argument(f'--proxy-server=http://{ip}')
#     # chrome_options.add_argument(f'--proxy-server=https:\\{ip}:{port}')
#     browser = webdriver.Chrome(options=chrome_options)
#     browser.get(f'https://api.ipify.org?format=json')
# hand_test()
# for i in ip_list:
#     print(i)
#     r=requests.get("https://api.ipify.org",proxies = { 
#               "http" : f'{i}'}).text
#     print(r)
#     input()
    # try:
    #     urllib.request.urlopen(
    #         "http://google.com",
    #         proxies={'http':f'{i}'}
    #     )
    # except IOError:
    #     print("Connection error! (Check proxy)")
    # else:
    #     print("All was fine")
    # input()
# hand_test(ip)
# browser.quit()
# print(f'--proxy-server=https:\\\\{ip}:{port}')
# 172.67.176.135:80
# para={'data':ip}
# r=requests.post(r'https://hidemy.name/api/checker.php?out=js&action=list_new&tasks=http,ssl,socks4,socks5&parser=lines',data=para,stream=True)
# time.sleep(20)
# print(r.text)