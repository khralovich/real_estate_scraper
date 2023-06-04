import pandas as pds
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

url_search = "https://www.morizon.pl/mieszkania/warszawa/?ps%5Bbuild_year_from%5D=1970&ps%5Bliving_area_from%5D=40&ps%5Bmarket_type%5D=2&ps%5Bnumber_of_rooms_from%5D=2&ps%5Bnumber_of_rooms_to%5D=3&ps%5Bprice_m2_to%5D=10979&ps%5Bprice_to%5D=500000"
url = "https://www.morizon.pl"

path = "/usr/bin/chromedriver"

driver = webdriver.Chrome(path)
driver.get(url_search)
time.sleep(5)
html = driver.page_source
soup = bs(html, "html.parser")
time.sleep(10)


"""
if this exists
class
cmp-intro_intro
it means we have a popup (After 10 sec), to close:
class
cmp-closebutton_closeButton cmp-closebutton_hasBorder
"""


if soup.find_all("div", {"class": "cmp-intro_intro"}):
    print("popup detected")
else:
    print("no popup")


offers_set = soup.find_all("a", {"class": "offer__outer"})


for i in offers_set:
    link = i['href']
    print(link)
