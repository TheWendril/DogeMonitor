import time
from src.modules.render import ScreenRender
from src.modules.money_balance import MoneyBalance

if __name__ == '__main__':

    screen_render = ScreenRender()
    money_balance = MoneyBalance()

    while 1:
        screen_render.render_balance(money_balance.get_balance())
        time.sleep(2)
