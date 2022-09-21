import requests
from pyquery import PyQuery as pq
import os
import subprocess
from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.chrome.options import Options
def get_proxy():
    '''
    function to retrive proxies from free proxies website
    ----------------------------------------------------
    parameter: 
        None
    return:
        ips: list
            a list of proxies retreive from free proxies website
    '''
    url=r'https://sslproxies.org/'
    headers={"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36"}
    r=requests.get(url,headers=headers)
    doc=pq(r.text)
    a=doc('table:first tr').items()
    ips=[(tr.text().split('\n')[0]+":"+tr.text().split('\n')[1]) for tr in list(a)[1:]]
    # ports=[tr.text().split('\n')[1] for tr in list(b)[1:]]
    return ips
# print(get_proxy())
# a="'8.219.97.248:80', '130.41.15.76:8080', '20.87.219.11:8000', '47.88.50.230:3128', '200.105.215.18:33630', '65.21.141.242:10100', '198.59.191.234:8080', '20.87.220.141:8000', '47.242.202.128:54466', '94.74.111.50:3128', '20.87.215.175:8000', '20.113.137.1:8000', '173.208.249.76:8080', '47.242.254.88:8888', '167.235.66.172:30001', '47.91.107.251:3080', '192.99.182.243:3128', '47.242.12.6:9000', '47.243.138.208:6677', '103.177.224.45:8080', '20.87.216.232:8000', '20.87.219.39:8000', '110.238.104.109:30001', '20.113.143.102:8000', '47.91.124.248:30001', '110.34.1.46:3128', '157.100.12.138:999', '14.207.7.134:8080', '8.242.178.123:999', '119.76.142.134:8080', '181.118.158.133:999', '62.193.108.135:1981', '45.167.126.249:9992', '181.129.49.214:999', '113.252.185.184:3128', '154.13.4.77:59394', '17879.208.64:44554', '8.211.20.219:1080', '110.238.73.59:3128', '46.146.206.106:45854', '154.239.1.72:1976', '45.79.253.142:4153', '197.243.14.45:8889', '114.119.189.123:3128', '149.129.180.195:8118', '110.78.138.168:8080', '103.154.91.182:8080', '133.18.197.218:8080', '143.198.182.218:80', '36.90.34.228:8080', '66.94.121.32:3128', '210.212.227.67:3128', '176.56.107.97:50082', '172.105.190.51:8017', '8.142.149.186:80', '47.88.6.66:46726', '8.211.22.40:1080', '47.250.47.208:36389', '8.211.22.130:5678', '168.138.36.173:33080', '172.105.25.190:8020', '95.17.166.205:8118', '47.91.111.166:28737', '157.230.34.152:39277', '186.215.87.194:6062', '167.114.96.27:9300', '47.91.57.156:30001', '143.244.133.78:80', '113.108.148.102:10415', '96.126.103.64:999', '68.183.185.62:80', '47.88.8.118:30001', '27.159.66.41:20183', '47.101.145.157:9128', '117.121.204.9:7998', '119.3.122.177:5566', '85.159.214.61:4145', '133.18.194.45:8080', '5.196.63.97:8080', '45.79.111.38:9991', '178.63.62.94:10001', '164.138.103.163:3128', '172.104.241.29:808', '213.14.174.70:3128', '182.253.108.50:40448', '104.225.216.161:3128', '94.230.183.226:8080', '181.198.40.145:999', '62.193.108.131:1981', '5.44.62.166:8080', '185.17.132.15:2536'"
# a=a.replace("'",'')
# print(a)
def check_proxy(proxies):
    pass
    # '''
    # function to check which proxy in a given list works
    # ---------------------------------------------------
    # parameter:
    #     proxies: list
    #         a list of proxies
    # return
    #     working_proxies: list
    #         a list of working/living proxies
    # ---------------------------------------------------
    # Note: a proxy server can be living and working but be banned
    # by certain websites'''
chrome=r"C:\Users\Di Yao\AppData\Local\Google\Chrome\Application\chrome.exe"



# p=subprocess.Popen([
#     r'C:\Users\Di Yao\AppData\Local\Google\Chrome\Application\chrome.exe',
#     '--remote-debugging-port=9222',
#     '--user-data-dir={}'.format(r"C:\selenium\ChromeProfile"),
#     '--proxy-server=162.55.186.206:13045',
#     'https://api.ipify.org/'
#     ])

# chrome_options = Options()
# chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
# # chrome_options.add_argument(f'--proxy-server={ip}')
# browser = webdriver.Chrome(options=chrome_options)
# browser.get('https://api.ipify.org/')
# print(browser.page_source)