from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

import pandas as pd
import numpy as np
import plotly.express as px

import re
from pycountry import countries

from tqdm import tqdm


# load beer dataset
df = pd.read_csv("../repo/datascience-finalproject/beer_reviews.csv")
brewery_ids = df.brewery_id.unique()

# setup webdriver
chrome_options = Options()
chrome_options.headless=True

driver = webdriver.Chrome("L:/chromedriver_win32/chromedriver.exe", options=chrome_options)
driver.set_window_size(1700, 900)

wait = WebDriverWait(driver, 20)

df["country_plain"] = ""
#df["country_official"] = ""
df["country_alpha_2"] = ""
df["country_alpha_3"] = ""
df["country_numeric"] = ""

num_timeout = 0
num_notspecified = 0
timed_out_ids = []
not_specified_ids = []

for brewery_id in tqdm(brewery_ids):

    try:
        driver.get("https://www.beeradvocate.com/beer/profile/" + str(brewery_id))

        # TODO: check for timeout exception
        info_box = wait.until(EC.element_to_be_clickable((By.ID, 'info_box')))

        info_html = info_box.get_attribute('innerHTML')
        # now parse for eg.: /place/directory/6/IT/
        country_code_match = re.search('/place/directory/.+/[A-Z]{2}', info_html)

        if country_code_match is not None:
            country_code = country_code_match.group(0)[-2:]
        else:
            df.loc[df['brewery_id'] == brewery_id, 'country_plain'] = "Not Specified"
            continue

        # and look the country code up with pycountry (hopefully its ISO compliant)
        country = countries.get(alpha_2=country_code)
        #print(country)
        df.loc[df['brewery_id'] == brewery_id, 'country_plain'] = country.name
        #df.loc[df['brewery_id'] == brewery_id, 'country_official'] = country.official_name
        df.loc[df['brewery_id'] == brewery_id, 'country_alpha_2'] = country.alpha_2
        df.loc[df['brewery_id'] == brewery_id, 'country_alpha_3'] = country.alpha_3
        df.loc[df['brewery_id'] == brewery_id, 'country_numeric'] = country.numeric
    except TimeoutException as ex:
        num_timeout += 1
        timed_out_ids.append(brewery_id)
        df.loc[df['brewery_id'] == brewery_id, 'country_plain'] = "Timed Out"



driver.close()

# save the new dataframe with the countries of the breweries
df.to_csv('beer_reviews_countries.csv')

print("Number of timeouts = " + str(num_timeout))
print(timed_out_ids)

print("Number of not specified ids= " + str(num_notspecified))
print(not_specified_ids)