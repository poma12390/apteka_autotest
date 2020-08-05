#проверка входа на сайт под пользователем 9179576275 
#запуск pytest -s test_login.py

import time
import pytest
from selenium import webdriver
import datetime


def setup_module():
    writelog("start ",str(datetime.datetime.today().strftime('%d-%m-%Y %H-%M-%S')))

def teardown_module():
    writelog("finish ",str(datetime.datetime.today().strftime('%d-%m-%Y %H-%M-%S'))+"\n")

def writelog(link, text):
    with open("test.txt", "a") as file:
        file.write(link + " " +  text + "\n")
    print(link, text)



@pytest.mark.parametrize('link', ["http://аптеканабалтахинова.рф/", "http://аптека03плюс.рф",
                                  "https://aptekanabaltakhinova.ru/", "https://apteka03plus.ru/"]
)
def test_guest_should_login_link(link):
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.get(link)
    login = browser.find_element_by_css_selector("[class='authorization login-button']")
    login.click()
    login1 = browser.find_element_by_css_selector("[name='login']")
    login1.send_keys("9179576275")
    password = browser.find_element_by_css_selector("[name='password']")
    password.send_keys("Qwertyuiop")
    vhod = browser.find_element_by_css_selector("[name='autoriz']")
    vhod.click()
    time.sleep(3)
    proverka=browser.find_element_by_css_selector("[class='authorization unauthorization']")
    if proverka.text=="КАБИНЕТ":
        writelog(link, "login true")
    else:
        writelog(link,"login false")
    time.sleep(3)
    browser.quit()



@pytest.mark.parametrize('link', ["http://аптека02плюс.рф"]
)
def test_guest_should_login_link1(link):
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.get(link)
    apteka=browser.find_element_by_css_selector("[class='close']")
    apteka.click()
    cabinet = browser.find_element_by_css_selector("[class='header__cabinet-button']")
    cabinet.click()
    nomer = browser.find_element_by_id("phone")
    nomer.send_keys("9179576275")
    password = browser.find_element_by_id("password")
    password.send_keys("Qwertyuiop2003")
    voity = browser.find_element_by_css_selector("[class='btn btn-primary js-login-btn']")
    voity.click()
    time.sleep(3)
    proverka = browser.find_element_by_css_selector("[class='header__cabinet-link']")
    if proverka.text == "Выйти":
        writelog(link, "login true")
    else:
        writelog(link, "login false")
    browser.quit()


@pytest.mark.parametrize('link', ["http://аптеканабаумана.рф/"]
)
def test_guest_should_login_link2(link):
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.get(link)
    cabinet = browser.find_element_by_css_selector("[class='fancybox cabinet_button']")
    cabinet.click()
    nomer = browser.find_element_by_name("phone")
    nomer.send_keys("9")
    time.sleep(1)
    nomer.send_keys("17")
    nomer.send_keys("9")
    nomer.send_keys("5")
    nomer.send_keys("76")
    nomer.send_keys("27")
    nomer.send_keys("5")
    password = browser.find_element_by_name("password")
    password.send_keys("Qw")
    time.sleep(1)
    password.send_keys("er")
    password.send_keys("ty")
    password.send_keys("ui")
    password.send_keys("op")
    password.send_keys("20")
    password.send_keys("03")
    voity = browser.find_element_by_css_selector("[class='reg_mod_button']")
    voity.click()
    time.sleep(1)
    proverka = browser.find_element_by_css_selector("[class='cabinet_button exit']")
    if proverka.text == "ВЫХОД":
        writelog(link, "login true")
    else:
        writelog(link, "login false")
    browser.quit()