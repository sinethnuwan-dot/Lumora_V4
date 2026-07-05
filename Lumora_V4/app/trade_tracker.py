import time

from app.config import Config
from app.logger import logger
from app.volume_acceleration import volume_acceleration


class TradeTracker:

    def __init__(self):
        self.candles = {}

    def update(
        self,
        symbol: str,
        price: float,
        quantity: float,
    ) -> dict:

        now = time.time()
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
                "start_time": int(now),
                "open": price,
                "high": price,
                "low": price,
                "current": price,
                "volume": usdt_volume,
                "trade_count": 1,
                "watch_sent": False,
                "confirm_sent": False,
                "last_volume": usdt_volume,
                "last_volume_time": now,
                "volume_acceleration": 0.0,
            }

            self.candles[symbol] = candle

            logger.info(
                f"NEW CANDLE | {symbol} | Open={price}"
            )

            return candle

        candle = self.candles[symbol]

        # -------------------------
        # Reset every 15 minutes
        # -------------------------

        if now - candle["start_time"] >= Config.CANDLE_SECONDS:

            candle = {
                "start_time": int(now),
                "open": price,
                "high": price,
                "low": price,
                "current": price,
                "volume": usdt_volume,
                "trade_count": 1,
                "watch_sent": False,
                "confirm_sent": False,
                "last_volume": usdt_volume,
                "last_volume_time": now,
                "volume_acceleration": 0.0,
            }

            self.candles[symbol] = candle

            logger.info(
                f"RESET CANDLE | {symbol}"
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

        # -------------------------
        # Volume Acceleration
        # -------------------------

        elapsed = now - candle["last_volume_time"]

        candle["volume_acceleration"] = volume_acceleration.calculate(
            previous_volume=candle["last_volume"],
            current_volume=candle["volume"],
            elapsed_seconds=elapsed,
        )

        candle["last_volume"] = candle["volume"]
        candle["last_volume_time"] = now

        return candle

    def get(self, symbol):

        return self.candles.get(symbol)

    def reset(self, symbol):

        if symbol in self.candles:

            del self.candles[symbol]

            logger.info(
                f"{symbol} tracker removed."
            )


trade_tracker = TradeTracker()