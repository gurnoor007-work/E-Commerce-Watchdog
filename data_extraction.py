#Lets import bs4
from bs4 import BeautifulSoup
import os
import re
from urllib.parse import urljoin
import pandas as pd
import retrieving_HTML
import time
from colorama import Fore, init, Style
init(autoreset=True)
time.sleep(2)

#make a function to formate price_str
def price_format(price_str: str):
    cleaned_string = re.sub(r'[^0-9.]', '', price_str)
    return int(cleaned_string)

NAME = []
PRICE = []
RATING = []
LINK = []

for product_n in range(1, len(os.listdir('raw_html')) + 1):
    with open(f'raw_html/p_{product_n}.html', 'r') as f:
        html = f.read()
        soup = BeautifulSoup(html, 'lxml')

        #get the names
        try:
            name = soup.select_one('a.a-link-normal.s-line-clamp-2.s-line-clamp-3-for-col-12.s-link-style.a-text-normal h2.a-size-medium.a-spacing-none.a-color-base.a-text-normal')
            name_str = name.text
            NAME.append(name_str.strip())
        except:
            NAME.append(None)
        
        #get the prices
        try:
            price_str = soup.select_one('span.a-price-whole')
            PRICE.append(price_format(price_str.text))
        except:
           PRICE.append(None)

        #get the rating
        try:
            rating_str = soup.select_one('div[data-cy="reviews-block"] span.a-size-small.a-color-base')
            RATING.append(float(rating_str.text.strip()))
        except:
            RATING.append(None)

        #get the link
        try:
            link_elem = soup.select_one('a.a-link-normal.s-line-clamp-2.s-line-clamp-3-for-col-12.s-link-style.a-text-normal')
            link_href = link_elem['href']
            base_url = "https://amazon.in"
            final_url = urljoin(base=base_url, url=link_href)
            LINK.append(final_url)
        except:
            LINK.append(None)
            
print(Fore.GREEN + "->" + Style.RESET_ALL + "Names Retrieved")
time.sleep(1)
print(Fore.GREEN + "->" + Style.RESET_ALL + "Prices Retrieved")
time.sleep(1)
print(Fore.GREEN + "->" + Style.RESET_ALL + "Ratings Retrieved")
time.sleep(1)
print(Fore.GREEN + "->" + Style.RESET_ALL + "Links Retrieved")
time.sleep(1)
print("Data retrieved, check result.csv")
time.sleep(2)


data = {
    'name': NAME,
    'price': PRICE,
    'rating': RATING,
    'link': LINK
}

df = pd.DataFrame(data=data)
df = df.dropna(subset=[df.columns[0]])
df.to_csv('result.csv')