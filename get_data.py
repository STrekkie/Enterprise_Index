from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.options import Options
import time
import random
from dataset_funcs import *

# opt = Options()
# opt.add_argument('--headless')

date = time.strftime('%Y-%m-%d',time.localtime(time.time()-86400))
add_column(date)

s = set()

for i in range(1,151):

    url = 'https://www.yuncaijing.com/data/mai/p{n}.html'.format(n=i)
    web = Chrome(service=Service(executable_path='./chromedriver'))
    web.get(url)

    a = web.find_elements(By.XPATH, '//*[@id="container"]/section/article[2]/table/tbody/tr')

    for i in a:
        name = i.find_element(By.XPATH, './td[1]/a').text
        num = i.find_element(By.XPATH, './td[2]').text
        mai = i.find_element(By.XPATH, './td[3]').text
        num = int(float(num))
        mai = int(float(mai))
        n = name[:-8]
        c = name[-7:-1]
        if c in s:
            continue
        s.add(c)
        update_data(c, date, num)

    web.close()
    time.sleep(5 + random.random()*10)
