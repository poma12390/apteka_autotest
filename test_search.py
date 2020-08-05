#(в работе) проверка работы поисковой строки, выпадающих подсказок и поиска на транслите
#запуск python test_search.py



import time
import pytest
from selenium import webdriver
import datetime
import re
import xlrd, xlwt

rb = xlrd.open_workbook('adress.xlsx')
regexp = r'(.*)\n'

def writelog(link, text):
    with open("test.txt", "a") as file:
        file.write(link + " " +  text + "\n")
    print(link, text)


link="http://аптека03плюс.рф"
browser = webdriver.Chrome()
browser.implicitly_wait(5)
browser.get(link)
write = "валидол"
poisk=browser.find_element_by_css_selector("[class='input-search']")
poisk.send_keys(write)
time.sleep(2)
podskaz=browser.find_elements_by_tag_name("[class='fast-word']")
for i in range(len(podskaz)):
    print(podskaz[i].text)
time.sleep(2)
podskaz[1].click()
time.sleep(3)
browser.get(link)
poisk=browser.find_element_by_css_selector("[class='input-search']")
poisk.send_keys("dfkbljk")
time.sleep(2)
subm=browser.find_element_by_tag_name("[class='search-button catalog-search hidden-xs']")
subm.click()
proverka=browser.find_elements_by_css_selector("[class='search-title-wrap']")
if len(proverka)==0:
    print("TRANS ERROR")