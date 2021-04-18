import os
import terminalplot
from src.modules import data_fetching
from termcolor import colored
from src.modules.currency_data import data_currency


class ScreenRender:

    def __init__(self):
        self.dataFetchingInstance = data_fetching.DataFetching("https://economia.awesomeapi.com.br/json/last/DOGE-BRL")

    def render_balance(self, user_data):

        os.system('clear')

        self.render_plots(False, True)

        for user in user_data:

            print('=================================================================')

            print('Nome: ' + user['User'])
            print('Investimento: ' + str(user['investedMoney']))
            print('Doges: ' + str(user['PurchasedDoges']))
            print('Preço do Doge: ' + str(user['CurrentPrice']))
            print(colored('Lucro: ' + str(user['profit']), 'red' if user['profit'] < 0 else 'green'))

    @staticmethod
    def render_plots(profit, prices):

        if profit:
            terminalplot.plot(data_currency.profit, range(len(data_currency.profit)))

        if prices:
            y = data_currency.money_price
            x = range(len(data_currency.money_price) - 1)
            terminalplot.plot(x, y)