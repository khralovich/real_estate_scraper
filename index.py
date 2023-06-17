import pandas as pd
import openpyxl
from functions import *


morizon_main_url = "https://www.morizon.pl/mieszkania/warszawa/?ps%5Bbuild_year_from%5D=1970&ps%5Bliving_area_from%5D=39&ps%5Bmarket_type%5D=2&ps%5Bnumber_of_rooms_from%5D=2&ps%5Bnumber_of_rooms_to%5D=3&ps%5Bprice_from%5D=380000&ps%5Bprice_to%5D=460000&ps%5Bwith_photo%5D=1"

offers_paths_set = get_ads_urls_set(morizon_main_url)
df_ready_for_regex = get_data_for_regex(offers_paths_set)

df_ready_for_regex.to_excel('out.xlsx')
