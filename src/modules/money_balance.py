import json
import dotenv
from src.modules.data_fetching import DataFetching
from src.modules.currency_data import data_currency


class MoneyBalance:

    def __init__(self):

        api_url = dotenv.get_key(dotenv.find_dotenv('./src/config/.env'), 'api_url')
        self.data_fetching = DataFetching(api_url)
        self.users_data = None

        with open('./src/config/users.json', 'r') as UsersFile:
            self.users_data = json.load(UsersFile)

    def get_balance(self):

        balance = []
        for user in self.users_data:

            self.data_fetching.refresh()

            current_price = float(self.data_fetching.get_data()['DOGEBRL']['bid'])
            user['CurrentPrice'] = current_price
            user['profit'] = user['PurchasedDoges'] * current_price - user['investedMoney']

            # Save CurrencyData
            data_currency.insert_price(current_price)
            data_currency.insert_profit({'Name': user['User'], 'profit': user['profit']})

            # Insert the Balance on List
            balance.insert(len(balance), user)

        return balance
