import pandas as pd
import openpyxl
from functions import *
from classes import *


morizon = Website("https://www.morizon.pl", "https://www.morizon.pl/mieszkania/warszawa/?ps%5Bbuild_year_from%5D=1970&ps%5Bliving_area_from%5D=39&ps%5Bmarket_type%5D=2&ps%5Bnumber_of_rooms_from%5D=2&ps%5Bnumber_of_rooms_to%5D=3&ps%5Bprice_from%5D=380000&ps%5Bprice_to%5D=400000&ps%5Bwith_photo%5D=1")
otodom = Website("https://www.otodom.pl", "https://www.otodom.pl/pl/oferty/sprzedaz/mieszkanie,rynek-wtorny/warszawa?distanceRadius=0&page=1&limit=36&priceMax=450000&areaMin=39&ownerTypeSingleSelect=ALL&buildYearMin=1970&roomsNumber=%5BTWO%2CTHREE%5D&locations=%5Bcities_6-26%5D&by=DEFAULT&direction=DESC&viewType=listing")
nieruchomosci_pl = Website("https://warszawa.nieruchomosci-online.pl",
                           "https://warszawa.nieruchomosci-online.pl/szukaj.html?3,mieszkanie,sprzedaz,,Warszawa:20571,,,,-450000,39,,,,,,2,,,,,,,,,,,,,,,,,,,,,,,1")


nieruchomosci_pl.get_html()
urls_set_nieruchomosci_pl = nieruchomosci_pl.get_ads_urls_set("tabCtrl")
print(urls_set_nieruchomosci_pl)

morizon.get_html()
urls_set_morizon = morizon.get_ads_urls_set("offer__outer")
print(urls_set_morizon)

otodom.get_html()
urls_set_otodom = otodom.get_ads_urls_set("e1n6ljqa3")
print(urls_set_otodom)
# df_ready_for_regex.to_excel('out.xlsx')
