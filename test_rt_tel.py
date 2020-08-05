#проверка корректности адреса режима работы аптек на основании файла adress.xlsx
#запуск python proverka_rt_tel.py


import time
import pytest
from selenium import webdriver
import datetime
import re
import xlrd, xlwt

rb = xlrd.open_workbook('adress.xlsx')
regexp = r'(.*)\n'

def writelog(text):
    with open("test.txt", "a") as file:
        file.write(text+"\n")
    print(text)

def setup_module():
    writelog("\n" + "start " + str(datetime.datetime.today().strftime('%d-%m-%Y %H-%M-%S'))+"\n")


def teardown_module():
    writelog("\n" + "finish " + str(datetime.datetime.today().strftime('%d-%m-%Y %H-%M-%S')) + "\n")

link=("      http://аптека03плюс.рф" + "\n")
writelog("               PROVERKA ADRESS TELEPHONE " + '\n')
writelog(link)
browser = webdriver.Chrome()
browser.implicitly_wait(5)
browser.get(link)
vibor=browser.find_element_by_css_selector("[class='repick-apt']")
vibor.click()
apteki=browser.find_elements_by_css_selector("[class='apt-list__drugstore-addr drugstore-addr']")
curapteka=browser.find_element_by_css_selector("[class='apt-list__drugstore-addr drugstore-addr active-addr']")
result = re.match(regexp, curapteka.text)
ex=browser.find_element_by_css_selector("[class='closeplace confirm-apt']")
ex.click()
curtown=browser.find_element_by_css_selector("[class='apt-num']")
curadr=browser.find_element_by_css_selector("[class='apt-adr']")
adress = str(curtown.text) + " " + (curadr.text)
writelog(" adress " + adress + "\n")
tel=browser.find_elements_by_css_selector("[class='tel']")
for i in range(len(tel)):
    rez_sait = re.split(r"\n\s*", tel[i].get_attribute("textContent").strip())
sheet = rb.sheet_by_index(0)
if (sheet.row_values(0)[0].lower())==(result.group(1).lower()):
    writelog("")
else:
    writelog("ОЖИДАЛОСЬ " + sheet.row_values(0)[0].lower() + " ПОЛУЧЕНО " + result.group(1).lower())
if adress.lower()==(sheet.row_values(0)[3].lower()):
    writelog(" ")
else:
    writelog("ОЖИДАЛОСЬ " + adress.lower() + " ПОЛУЧЕНО " + sheet.row_values(0)[3].lower())
for i in range(2):
    k=i
    if i==1:
        k=2
    if rez_sait[k].lower()==sheet.row_values(0)[i+1].lower():
        continue
    else:
        writelog("ОЖИДАЛОСЬ " + rez_sait[k].lower() + " ПОЛУЧЕНО " +sheet.row_values(0)[i+1].lower())
browser.quit()
link="http://аптека03плюс.рф"
browser = webdriver.Chrome()
browser.implicitly_wait(5)
browser.get(link)
vibor=browser.find_element_by_css_selector("[class='repick-apt']")
vibor.click()
apteki_id=browser.find_elements_by_css_selector("[class='apt-list__drugstore-addr drugstore-addr']")
apteki=apteki_id.copy()

for i in range(len(apteki)):
    result = re.match(regexp, apteki_id[i].text)
    apteki[i]=result.group(1) #apteki все адреса
close = browser.find_element_by_css_selector("[class='closeplace confirm-apt']")
close.click()
time.sleep(3)
for i in range(len(apteki_id)):
    vibor = browser.find_element_by_css_selector("[class='repick-apt']")
    vibor.click()
    time.sleep(2)
    apteki_id = browser.find_elements_by_css_selector("[class='apt-list__drugstore-addr drugstore-addr']")
    apteki_id[i].click()
    close = browser.find_element_by_css_selector("[class='closeplace confirm-apt']")
    time.sleep(2)
    close.click()
    curtown = browser.find_element_by_css_selector("[class='apt-num']")
    curadr = browser.find_element_by_css_selector("[class='apt-adr']")
    adress = str(curtown.text) + " " + (curadr.text)
    writelog(" adress " + adress + "\n")
    tel = browser.find_elements_by_css_selector("[class='tel']")
    for j in range(len(tel)):
        rez_sait = re.split(r"\n\s*", tel[j].get_attribute("textContent").strip())
    sheet = rb.sheet_by_index(0)
    if (sheet.row_values(i+1)[0].lower()) == (apteki[i].lower()):
        continue
    else:
        writelog + ("ОЖИДАЛОСЬ ", sheet.row_values(i+1)[0].lower(), " ПОЛУЧЕНО ", apteki[i].lower())
    if adress.lower() == (sheet.row_values(i+1)[3].lower()):
        continue
    else:
        writelog("ОЖИДАЛОСЬ " +  adress.lower() + " ПОЛУЧЕНО " + sheet.row_values(i+1)[3].lower())
    for l in range(2):
        k = l
        if l == 1:
            k = 2
        if (sheet.row_values(i + 1)[l+1].lower()) == (rez_sait[(k//2)*2].lower()):
            continue
        else:
            writelog("ОЖИДАЛОСЬ " + sheet.row_values(i + 1)[l+1].lower() + " ПОЛУЧЕНО1 " +  (rez_sait[(k//2)*2].lower()))
browser.quit()

