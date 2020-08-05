#проверка ранжирования цен в поиске и наличие подстроки поиска у найденых наименованиях
#запуск pytest -s test_price.py


import time
import pytest
import re
from selenium import webdriver
import datetime

g = "валидол"
regexp = r'(.*)\n'


def setup_module():
    writelog("\n" + "start " + str(datetime.datetime.today().strftime('%d-%m-%Y %H-%M-%S'))+"\n")


def teardown_module():
    writelog("\n" + "finish " + str(datetime.datetime.today().strftime('%d-%m-%Y %H-%M-%S')) + "\n")


def writelog(text):
    with open("test.txt", "a") as file:
        file.write(text+"\n")
    print(text)


@pytest.mark.parametrize('link', ["http://аптеканабалтахинова.рф/", "http://аптека03плюс.рф"]
                         )
def test_guest_tseni(link):
    k = 0
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.get(link)
    poisk = browser.find_element_by_css_selector("[class='input-search']")
    poisk.send_keys(g)
    knopka = browser.find_element_by_css_selector("[class='search-button catalog-search hidden-xs']")
    knopka.click()
    time.sleep(3)
    name = browser.find_elements_by_css_selector("[class='search-title-wrap']")
    price = browser.find_elements_by_css_selector("[class='active-price']")

    if len(price) == 0:
        writelog("\n" +  link +"\n" "ТОВАРЫ НЕ НАЙДЕНЫ" + "\n")
        browser.quit()
    else:
        for i in range(len(price)):
            if g.lower() in name[i].text.lower():
                writelog("\n")
            else:
                writelog("NAME ERROR"+ " " + name[i].text)
        for i in range(len(price)):
            result = re.match(regexp, name[i].text)
            if result:
                if result.group(1).startswith(g.capitalize()):
                    k = k + 1
            else:
                writelog("BAD STRING")
        writelog(link + "\n")
        d = len(name) - k

        for i in range(k):
            result = re.match(regexp, name[i].text)
            writelog(result.group(1)+ "\n" + price[i].text[:-1]+"\n")
    for i in range(k - 1):
        if price[i].text.lower() == "нет в наличии" or price[i+1].text.lower() == "нет в наличии":
            continue
        if float(price[i].text[:-4]) > float(price[i + 1].text[:-4]):
            writelog("\n" + link +"\n" "RANGE ERROR" + "\n")
            writelog(price[i].text)
            writelog(price[i + 1].text)
    n=len(name)
    for i in range(d):
        result = re.match(regexp, name[n-i-1].text)
        writelog(result.group(1) + "\n" + "Товара нет в наличии" + "\n")
    browser.quit()


@pytest.mark.parametrize('link', ["http://аптека02плюс.рф"]
                         )
def test_guest_tsen2(link):
    k = 0
    browser = webdriver.Chrome()
    browser.implicitly_wait(10)
    browser.get(link)
    apteka = browser.find_element_by_css_selector("[class='close']")
    apteka.click()
    poisk = browser.find_element_by_css_selector("[class='search__search-bar']")
    poisk.send_keys(g)
    knopka = browser.find_element_by_css_selector("[class='search__submit-button']")
    knopka.click()
    sort = browser.find_element_by_css_selector("[class='filter__arrow filter__arrow_up']")
    sort.click()
    time.sleep(3)
    price = browser.find_elements_by_css_selector("[class='product-card__price']")
    time.sleep(3)
    name=browser.find_elements_by_css_selector("[class='product-card__info-block']")
    c = price.copy()
    if len(price) == 0:
        writelog("\n" +  link +"\n" "ТОВАРЫ НЕ НАЙДЕНЫ" + "\n")
        browser.quit()
    else:
        writelog(link + "\n")
        for i in range(len(price)):
            if g.lower() in name[i].text.lower():
                writelog("\n")
            else:
                writelog("NAME ERROR"+ " " + name[i].text)
            result = re.match(regexp, price[i].text)
            if result.group(1).lower()=="нет в наличии":
                writelog(name[i].text + "\n" + "нет в наличии")
                c[i]=0
            else:
                c[i] = result.group(1)
                writelog(name[i].text + "\n" + c[i][:-1]+"\n")


        for i in range(len(price)-1):
            if c[i+1]==0:
                continue
            else:
                if float(c[i][:-4]) > float(c[i + 1][:-4]):
                    writelog("\n" + "RANGE ERROR")
                    writelog(name[i].text + c[i]+ "\n" + name[i+1].text + c[i + 1]+ "\n")
        time.sleep(3)
    browser.quit()

@pytest.mark.parametrize('link', ["http://аптеканабаумана.рф/"]
                         )
def test_guest_tsen3(link):
    k = 0
    browser = webdriver.Chrome()
    browser.implicitly_wait(10)
    browser.get(link)
    poisk = browser.find_element_by_css_selector("[class='search-n']")
    poisk.send_keys(g)
    time.sleep(3)
    knopka = browser.find_element_by_css_selector("[class='search'] [class='search_button']")
    knopka.click()
    time.sleep(5)
    sort = browser.find_element_by_css_selector("[class='sort_price  DESC']")
    sort.click()
    time.sleep(3)
    price = browser.find_elements_by_css_selector(" [class='now']")
    name = browser.find_elements_by_css_selector("[class=catalog_prod_name]")
    writelog("\n" + link + "\n")
    if len(price) == 0:
        writelog("\n" +  link +"\n" "ТОВАРЫ НЕ НАЙДЕНЫ" + "\n")
        browser.quit()
    else:
        c = price.copy()
        for i in range(len(price)):
            if g.lower() in name[i].text.lower():
                writelog(name[i].text +"\n"+ price[i].text[:-1]+"\n")
            else:
                writelog("NAME ERROR"+ " " + name[i].text)
        for i in range(len(price)):
            if price[i].text.lower() == "нет в наличии":
                c[i]=0
                continue
            else:
                c[i] = float(price[i].text[:-4])


        for i in range(len(price) - 1):
            if (c[i] > c[i + 1]) and c[i]!=0 and c[i+1]!=0:
                writelog("RANGE ERROR")
                writelog(name[i].text + price[i].text)
                writelog(name[i + 1].text + price[i + 1].text)
                writelog("")
    browser.quit()