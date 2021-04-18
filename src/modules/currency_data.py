import threading
import dotenv
import time
from src.modules.data_fetching import DataFetching


class DataCurrency(threading.Thread):

    def __init__(self):

        self.money_price = []
        self.profit = []

        self.money_price_isUpgradable = True
        self.profit_price_isUpgradable = True

        api_url = dotenv.get_key(dotenv.find_dotenv('./src/config/.env'), 'api_url')
        self.data_fetching = DataFetching(api_url)

    def insert_price(self, value):

        if self.money_price_isUpgradable:

            if len(self.money_price) <= 20:
                self.money_price.insert(len(self.money_price), value)
                self.money_price_isUpgradable = False

            if len(self.money_price) == 20:
                self.money_price.pop(0)
                self.money_price.insert(len(self.money_price), value)
                self.money_price_isUpgradable = False

    def insert_profit(self, value):

        if self.profit_price_isUpgradable:

            if len(self.profit) <= 20:
                self.profit.insert(len(self.money_price), value)
                self.profit_price_isUpgradable = False

            if len(self.profit) == 20:
                self.profit.pop(0)
                self.profit.insert(len(self.money_price), value)
                self.profit_price_isUpgradable = False

    def run(self):

        while 1:
            self.profit_price_isUpgradable = True
            self.money_price_isUpgradable = True
            time.sleep(60)


data_currency: DataCurrency = DataCurrency()
