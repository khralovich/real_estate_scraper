import pandas as pd
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


path = "/usr/bin/chromedriver"
domain = "https://www.morizon.pl"
morizon_main_url = "https://www.morizon.pl/mieszkania/warszawa/?ps%5Bbuild_year_from%5D=1970&ps%5Bliving_area_from%5D=40&ps%5Bmarket_type%5D=2&ps%5Bnumber_of_rooms_from%5D=2&ps%5Bnumber_of_rooms_to%5D=3&ps%5Bprice_m2_to%5D=10979&ps%5Bprice_to%5D=500000"


def get_html(url):
    driver = webdriver.Chrome(path)
    driver.get(url)
    time.sleep(5)
    html = driver.page_source
    time.sleep(10)
    return bs(html, "html.parser")


def get_ads_urls_set(url_search):
    main_page_html = get_html(url_search)
    all_offers_html = main_page_html.find_all("a", {"class": "offer__outer"})
    offers_set = set()
    for i in all_offers_html:
        link = i['href']
        full_url = domain + link
        offers_set.add(full_url)
    return offers_set


def get_single_offer(ad_url):
    html_adv = get_html(ad_url)


offers_set = get_ads_urls_set(morizon_main_url)


print(offers_set)


"""
if this exists
class
cmp-intro_intro
it means we have a popup (After 10 sec), to close:
class
cmp-closebutton_closeButton cmp-closebutton_hasBorder
if soup.find_all("div", {"class": "cmp-intro_intro"}):
    print("popup detected")
else:
    print("no popup")
"""
