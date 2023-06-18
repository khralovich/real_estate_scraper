
import pandas as pd
from bs4 import BeautifulSoup as bs
from selenium import webdriver
import time

chromedriver_path = "/usr/bin/chromedriver"
domain = "https://www.morizon.pl"

"""
Create a general class for scraping a page.
Returns: a soup object (an entire html)
"""

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

"""
Get urls of all ads we would like to scrape.
Arguments to pass: a path with a query (filters)
Returns: a set of links with ads of interest.
"""

"""
def get_ads_urls_set(path_with_filters):
    main_page_html = get_html(path_with_filters)
    all_offers_html = main_page_html.find_all("a", {"class": "offer__outer"})
    offers_paths_set = set()
    for i in all_offers_html:
        link = i['href']
        full_url = domain + link
        offers_paths_set.add(full_url)
    return offers_paths_set
"""

"""
A function for a single ad. Should be in a loop.
"""


def get_single_offer(offer):
    adv_html = get_html(offer)
    description_html = adv_html.find_all("div", {"class": "basic-info"})
    detailed_info_html = adv_html.find_all(
        "div", {"class": "detailed-information"})
    new_df = pd.DataFrame({'link': [offer], 'description': [
                          description_html[0]], 'detailed_info': [detailed_info_html[0]]})
    return new_df
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
        new_df = get_single_offer(i)
        ads_df = ads_df.append(new_df, ignore_index=True)
    return ads_df
