import pandas as pd
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


chromedriver_path = "/usr/bin/chromedriver"
domain = "https://www.morizon.pl"
morizon_main_url = "https://www.morizon.pl/mieszkania/warszawa/?ps%5Bbuild_year_from%5D=1970&ps%5Bliving_area_from%5D=40&ps%5Bmarket_type%5D=2&ps%5Bnumber_of_rooms_from%5D=2&ps%5Bnumber_of_rooms_to%5D=3&ps%5Bprice_m2_to%5D=10979&ps%5Bprice_to%5D=500000"

"""
Create a general class for scraping a page.
Returns: a soup object (an entire html)
"""


def get_html(url):
    driver = webdriver.Chrome(chromedriver_path)
    driver.get(url)
    time.sleep(5)
    html = driver.page_source
    time.sleep(10)
    soup = bs(html, "html.parser")
    return soup


"""
Get urls of all ads we would like to scrape.
Arguments to pass: a path with a query (filters)
Returns: a set of links with ads of interest.
"""


def get_ads_urls_set(path_with_filters):
    main_page_html = get_html(path_with_filters)
    all_offers_html = main_page_html.find_all("a", {"class": "offer__outer"})
    offers_paths_set = set()
    for i in all_offers_html:
        link = i['href']
        full_url = domain + link
        offers_paths_set.add(full_url)
    print(offers_paths_set)
    return offers_paths_set


"""
A function for a single ad. Should be in a loop.
"""


def get_single_offer(offer):
    adv_html = get_html(offer)
    product_card = adv_html.find_all("div", {"class": "basic-info"})
    # do smth to get all needed data
    # put it into a df
    # get next ad


"""
Loop through ads of interest, scrape each one of them.
Arguments to pass: a set of urls.
Returns: a df with info for each ad.
"""


def get_data_for_regex(offers_paths_set):
    ads_df = pd.DataFrame()
    for i in offers_paths_set:
        single_offer_row = get_single_offer(i)
        ads_df = ads_df.append(single_offer_row, ignore_index=True)
    return ads_df


offers_paths_set = get_ads_urls_set(morizon_main_url)


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
