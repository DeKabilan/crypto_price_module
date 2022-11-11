from .scrapper import _CryptoPrice

class CryptoPriceBIN:
    def __init__(self) -> None:
        self.baseUrl = "https://www.binance.com/en/price/"

    def CryptoPrice(query: str):
        return _CryptoPrice(query)
    