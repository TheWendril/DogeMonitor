import terminalplot


class DataCurrency:

    def __init__(self):

        self.money_price = []
        self.profit = []

    def insert_price(self, value):

        if len(self.money_price) <= 20:
            self.money_price.insert(len(self.money_price), value)

        if len(self.money_price) == 20:
            self.money_price.pop(0)
            self.money_price.insert(len(self.money_price), value)

    def insert_profit(self, value):

        if len(self.profit) <= 20:
            self.profit.insert(len(self.money_price), value)

        if len(self.profit) == 20:
            self.profit.pop(0)
            self.profit.insert(len(self.money_price), value)


data_currency = DataCurrency()