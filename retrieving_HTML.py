#First we have to retrieve the html of all the products
#To store the product, we will set a list equal to the list of links of those products
#which we want to track

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time
import os
from bs4 import BeautifulSoup

from colorama import Fore, Back, Style, init #To format CLI text
init(autoreset=True)

query = input(Fore.CYAN + Style.BRIGHT + "Enter your query: ")
print(Style.RESET_ALL)
URL = f"https://www.amazon.in/s?k={query}&page=1"

driver = webdriver.Chrome()
driver.get(url=URL)

#Get the product box HTML
elems = driver.find_elements(By.CSS_SELECTOR, 'div.a-section.a-spacing-small.a-spacing-top-small')
print(f"{len(elems)} products have been retrieved.")
print(Fore.GREEN + "->" + Style.RESET_ALL + "Starting html file saving")

os.makedirs("raw_html", exist_ok=True)
product_n = 1

for elem in elems:
    html = elem.get_attribute("outerHTML")
    soup = BeautifulSoup(html, "lxml")
    html_prettified = soup.prettify()
    with open(f"raw_html/p_{product_n}.html", "w", encoding="utf-8") as f:
        f.write(html_prettified)

    product_n += 1

time.sleep(2)

print(Fore.GREEN + "->" + Style.RESET_ALL + "File saving done, check raw_html/")

driver.close()