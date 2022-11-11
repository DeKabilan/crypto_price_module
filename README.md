# __CryptoPriceBIN__

 Python module for fetching data from binance.com

## __How this works__

 Scraps the information from the HTML of the page using `beautifulsoup4` .
 
 ## __Requirements__
 
 BeautifulSoup4 'pip install bs4'
 Requests 'pip install requests'

## __Installation__

 `pip install CryptoPriceBIN`

## __Usage__

 ```python
 from CryptoPriceBIN import CryptoPriceBIN

 print(CryptoPriceBIN.CryptoPriceBIN.CryptoPrice("ethereum"))

 ```

 Output

 ```python
  '$ 1264.64'
 ```
## __Disclaimer__

 I'm in no way related to that website / person behind it / the kind of information hosted on it. The author of this library isn't responsible for what you do with this library.
