import requests
import json
from config import keys

class ConversionExeption(Exception):
    pass

class CryptoConverter:
    @staticmethod
    def convert(quote: str, base:str, amount:str):


        if quote == base:
            raise ConversionExeption(f'Ошибка - одинаковые валюты')

        try:
            quote_tiker = keys[quote]
        except KeyError:
            raise ConversionExeption(f'Не удалось обработать валюту{quote}')

        try:
            base_tiker = keys[base]
        except KeyError:
            raise ConversionExeption(f'Не удалось обработать валюту{base}')

        try:
            amount = float(amount)
        except ValueError:
            raise ConversionExeption(f'Не удалось обработать количество {amount}')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_tiker}&tsyms={base_tiker}')
        total_base = json.loads(r.content)[keys[base]]
        print(type(total_base))

        return total_base
