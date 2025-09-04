from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import re, time

options = webdriver.ChromeOptions()
# options.add_experimental_option('detach', True)
options.add_argument('headless')
browser = webdriver.Chrome(options=options)
browser.maximize_window()

url ='https://www.weather.go.kr/w/index.do'
browser.get(url)

#전국
el = browser.find_element(By.XPATH, '//a[text()="전국"]')
el.click()
time.sleep(2)

#어제
xpath='//*[@id="content-body"]/div[4]/div/div/div[1]/ul/li[1]/a/span'
el = browser.find_element(By.XPATH, xpath)
el.click()
time.sleep(2)

soup = BeautifulSoup(browser.page_source, 'lxml')
local = soup.find('div', {'id':'minmax'})
els = local.find_all('dl', {'class':re.compile('^po2_1')})
for idx,el in enumerate(els):
    name = el.dt.getText()
    temp_red=el.find('span', {'class':'red'}).getText()
    temp_blue=el.find('span', {'class':'blue'}).getText()
    weather=''
    print(idx+1,name,temp_red,temp_blue)

