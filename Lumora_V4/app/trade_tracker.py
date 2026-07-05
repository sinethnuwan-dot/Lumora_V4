import time

from app.config import Config
from app.logger import logger


class TradeTracker:

    def __init__(self):
        self.candles = {}

    def update(
        self,
        symbol: str,
        price: float,
        quantity: float,
    ) -> dict:

        now = int(time.time())
        usdt_volume = price * quantity

        # -------------------------
        # Ignore invalid trades
        # -------------------------

        if price <= 0 or quantity <= 0:
            return None

        # -------------------------
        # First candle
        # -------------------------

        if symbol not in self.candles:

            candle = {
                "start_time": now,
                "open": price,
                "high": price,
                "low": price,
                "current": price,
                "volume": usdt_volume,
                "trade_count": 1,
                "watch_sent": False,
                "confirm_sent": False,
            }

            self.candles[symbol] = candle

            logger.info(
                f"NEW CANDLE | {symbol} | Open={price}"
            )

            logger.info(
                f"CANDLE | "
                f"{symbol} | "
                f"Open={candle['open']} | "
                f"Current={candle['current']} | "
                f"High={candle['high']} | "
                f"Low={candle['low']} | "
                f"Volume={round(candle['volume'],2)} | "
                f"Trades={candle['trade_count']}"
            )

            return candle

        candle = self.candles[symbol]

        # -------------------------
        # New 15 minute candle
        # -------------------------

        if now - candle["start_time"] >= Config.CANDLE_SECONDS:

            candle = {
                "start_time": now,
                "open": price,
                "high": price,
                "low": price,
                "current": price,
                "volume": usdt_volume,
                "trade_count": 1,
                "watch_sent": False,
                "confirm_sent": False,
            }

            self.candles[symbol] = candle

            logger.info(
                f"RESET CANDLE | {symbol}"
            )

            logger.info(
                f"CANDLE | "
                f"{symbol} | "
                f"Open={candle['open']} | "
                f"Current={candle['current']} | "
                f"High={candle['high']} | "
                f"Low={candle['low']} | "
                f"Volume={round(candle['volume'],2)} | "
                f"Trades={candle['trade_count']}"
            )

            return candle

        # -------------------------
        # Update candle
        # -------------------------

        candle["current"] = price

        if price > candle["high"]:
            candle["high"] = price

        if price < candle["low"]:
            candle["low"] = price

        candle["volume"] += usdt_volume
        candle["trade_count"] += 1

        logger.info(
            f"CANDLE | "
            f"{symbol} | "
            f"Open={candle['open']} | "
            f"Current={candle['current']} | "
            f"High={candle['high']} | "
            f"Low={candle['low']} | "
            f"Volume={round(candle['volume'],2)} | "
            f"Trades={candle['trade_count']}"
        )

        return candle

    def get(self, symbol):

        return self.candles.get(symbol)

    def reset(self, symbol):

        if symbol in self.candles:

            del self.candles[symbol]

            logger.info(f"{symbol} tracker removed.")


trade_tracker = TradeTracker()