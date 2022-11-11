import requests
from bs4 import BeautifulSoup as bs4

def _CryptoPrice(query:str):
    url = requests.get("https://www.binance.com/en/price/"+query)
    url = url.text
    soup = bs4(url, 'html.parser')
    price = soup.find('div',class_="css-12ujz79")
    price=price.text
    return price
