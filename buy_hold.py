from config import ALPACA_CONFIG
from datetime import datetime
from lumibot.backtesting import YahooDataBacktesting
from lumibot.brokers import Alpaca
from lumibot.strategies import Strategy
from lumibot.traders import Trader


class BuyHold(Strategy):

    def initialize(self):
        # Sets sleep time for strategy
        self.sleeptime = "1D"

    def on_trading_iteration(self):
        if self.first_iteration:
            symbol = "GOOG"
            price = self.get_last_price(symbol)
            quantity = self.cash // price
            order = self.create_order(symbol, quantity, "buy")
            self.submit_order(order)


if __name__ == "__main__":
    # Choose between live trading
    trade = False

    if trade:
        broker = Alpaca(ALPACA_CONFIG)
        strategy = BuyHold(broker=broker)
        trader = Trader()
        trader.add_strategy(strategy)
        trader.run_all()
    else:
        # Backtesting
        with open("/home/gene/trading_bot/logs/BuyHold_2023-11-12_23-19-41_logs.csv", "r") as f:
            # Filter out lines starting with a timestamp and log message
            code = '\n'.join(line for line in f.readlines()
                             if not line.strip().startswith('20'))
        exec(code)
