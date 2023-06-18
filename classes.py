
import pandas as pd
from bs4 import BeautifulSoup as bs
from selenium import webdriver
import time

"""
Create a general class for scraping a page.

"""


class Website:
    CHROMEDRIVER_PATH = "/usr/bin/chromedriver"

    def __init__(self, domain, webpage_filter):
        self.domain = domain
        self.webpage_filter = webpage_filter
        self.soup = None
        self.offers_paths_set = set()

        """
        Get a webpage with filtered results, scrape it as a soup object
        Returns: a soup object (an entire html)
        """

    def get_html(self):
        driver = webdriver.Chrome(Website.CHROMEDRIVER_PATH)
        driver.get(self.webpage_filter)
        time.sleep(5)
        html = driver.page_source
        time.sleep(10)
        self.soup = bs(html, "html.parser")

        """
        Get urls of all ads we would like to scrape.
        Returns: a set of links with ads of interest.
        """

    def get_ads_urls_set(self, class_to_search):
        main_page_html = self.soup
        self.class_to_search = class_to_search
        all_offers_html = main_page_html.find_all(
            "a", {"class":  self.class_to_search})
        for i in all_offers_html:
            link = i['href']
            full_url = self.domain + link
            self.offers_paths_set.add(full_url)
        return self.offers_paths_set


morizon = Website("https://www.morizon.pl", "https://www.morizon.pl/mieszkania/warszawa/?ps%5Bbuild_year_from%5D=1970&ps%5Bliving_area_from%5D=39&ps%5Bmarket_type%5D=2&ps%5Bnumber_of_rooms_from%5D=2&ps%5Bnumber_of_rooms_to%5D=3&ps%5Bprice_from%5D=380000&ps%5Bprice_to%5D=400000&ps%5Bwith_photo%5D=1")
morizon.get_html()
urls_set_morizon = morizon.get_ads_urls_set("offer__outer")
print(urls_set_morizon)


otodom = Website("https://www.otodom.pl", "https://www.otodom.pl/pl/oferty/sprzedaz/mieszkanie,rynek-wtorny/warszawa?distanceRadius=0&page=1&limit=36&priceMax=450000&areaMin=39&ownerTypeSingleSelect=ALL&buildYearMin=1970&roomsNumber=%5BTWO%2CTHREE%5D&locations=%5Bcities_6-26%5D&by=DEFAULT&direction=DESC&viewType=listing")
otodom.get_html()
urls_set_otodom = otodom.get_ads_urls_set("e1n6ljqa3")
print(urls_set_otodom)

nieruchomosci_pl = Website("https://warszawa.nieruchomosci-online.pl",
                           "https://warszawa.nieruchomosci-online.pl/szukaj.html?3,mieszkanie,sprzedaz,,Warszawa:20571,,,,-450000,39,,,,,,2,,,,,,,,,,,,,,,,,,,,,,,1")
nieruchomosci_pl.get_html()
urls_set_nieruchomosci_pl = nieruchomosci_pl.get_ads_urls_set("tabCtrl")
print(urls_set_nieruchomosci_pl)


# pagination???
