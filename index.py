import pandas as pd
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


chromedriver_path = "/usr/bin/chromedriver"
domain = "https://www.morizon.pl"
# morizon_main_url = "https://www.morizon.pl/mieszkania/warszawa/?ps%5Bbuild_year_from%5D=1970&ps%5Bliving_area_from%5D=39&ps%5Bmarket_type%5D=2&ps%5Bnumber_of_rooms_from%5D=2&ps%5Bnumber_of_rooms_to%5D=3&ps%5Bprice_from%5D=380000&ps%5Bprice_to%5D=460000&ps%5Bwith_photo%5D=1"


morizon_main_url = "https://www.morizon.pl/mieszkania/warszawa/?ps%5Bbuild_year_from%5D=1970&ps%5Bliving_area_from%5D=39&ps%5Bmarket_type%5D=2&ps%5Bnumber_of_rooms_from%5D=2&ps%5Bnumber_of_rooms_to%5D=3&ps%5Bprice_from%5D=380000&ps%5Bprice_to%5D=400000&ps%5Bwith_photo%5D=1"
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
    description_html = adv_html.find_all("div", {"class": "basic-info"})
    detailed_info_html = adv_html.find_all(
        "div", {"class": "detailed-information"})
    row = [offer, description_html[0], detailed_info_html[0]]
    print(row)
    return row
    # do smth to get all needed data
    # put it into a df
    # get next ad


"""
Loop through ads of interest, scrape each one of them.
Arguments to pass: a set of urls.
Returns: a df with info.
"""


def get_data_for_regex(offers_paths_set):
    # ads_df = pd.DataFrame(columns=['link', 'price', 'location', 'rooms_meters', 'description', 'detailed_info'])
    ads_df = pd.DataFrame(columns=['link', 'description', 'detailed_info'])
    for i in offers_paths_set:
        single_offer_row = get_single_offer(i)
        print(single_offer_row)
        ads_df = ads_df.append(single_offer_row, ignore_index=True)
        print(ads_df)
    return ads_df


offers_paths_set = get_ads_urls_set(morizon_main_url)
df_ready_for_regex = get_data_for_regex(offers_paths_set)
print(df_ready_for_regex)

# DEPRECATED


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
