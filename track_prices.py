#Import data from data_extraction
from data_extraction import LINK, df, price_format
import time
from colorama import Fore, Style, init
init(autoreset=True)

#Import selenium stuff
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument("--headless=new")
    
driver = webdriver.Chrome(options=chrome_options)

for link in LINK:
    if link != None:
        driver.get(link)
        price_elem = driver.find_element(By.CSS_SELECTOR, 'span.a-price-whole')
        price_str_raw = price_elem.get_attribute('innerText').strip()
        print(Fore.RED + "price: " + Style.RESET_ALL + price_str_raw)
        price = price_format(price_str_raw.removesuffix('.'))

        index = LINK.index(link)
        df.at[index, 'price'] = price

display_df_with_rich(df)
driver.close()

