from time import sleep
from celery import shared_task
import requests
from .models import BitcoinTracking
import datetime

@shared_task
def crawl_currency():
    print('Crawling data and creating objects in database ..')
    key = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"

    # requesting data from url
    data = requests.get(key)  
    data = data.json()
    print(f"{data['symbol']} price is {data['price']}")


    # # Create object in database from crawled data 
    price = data['price']
    bitcoin_obj = BitcoinTracking(
        price = round(float(price), 2),
        mytimestamp = datetime.datetime.now()
    )
    bitcoin_obj.save()


while True:
    sleep(1)
    crawl_currency()


