import time

from app.logger import logger


class CandleBuilder:

    def __init__(self):

        self.candles = {}

    def update(
        self,
        symbol: str,
        price: float,
        quantity: float,
    ):

        now = int(time.time())

        # USDT Notional Volume
        usdt_volume = price * quantity

        # New candle
        if symbol not in self.candles:

            self.candles[symbol] = {
                "start": now,
                "open": price,
                "high": price,
                "low": price,
                "close": price,
                "volume": usdt_volume,
            }

            return self.candles[symbol]

        candle = self.candles[symbol]

        # Update OHLC
        candle["close"] = price

        if price > candle["high"]:
            candle["high"] = price

        if price < candle["low"]:
            candle["low"] = price

        # Add USDT volume
        candle["volume"] += usdt_volume

        return candle

    def get(self, symbol):

        return self.candles.get(symbol)

    def reset(self, symbol):

        if symbol in self.candles:
            del self.candles[symbol]
            logger.info(f"{symbol} candle reset.")


candle_builder = CandleBuilder()


if __name__ == "__main__":

    builder = CandleBuilder()

    prices = [100, 102, 99, 105, 103]

    for p in prices:

        candle = builder.update(
            symbol="BTCUSDT",
            price=p,
            quantity=10,
        )

    print(candle)