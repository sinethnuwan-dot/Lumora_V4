from app.alert_queue import alert_queue
from app.detector import detector
from app.logger import logger
from app.trade_tracker import trade_tracker


class Scanner:

    async def process_trade(
        self,
        symbol: str,
        price: float,
        quantity: float,
    ) -> None:

        # -------------------------
        # Update live candle
        # -------------------------

        candle = trade_tracker.update(
            symbol=symbol,
            price=price,
            quantity=quantity,
        )

        # Ignore invalid trades
        if candle is None:
            return

        # -------------------------
        # DEBUG CANDLE
        # -------------------------

        logger.info(
            f"CANDLE -> "
            f"{symbol} | "
            f"Open={candle['open']} | "
            f"Current={candle['current']} | "
            f"High={candle['high']} | "
            f"Low={candle['low']} | "
            f"Volume={round(candle['volume'],2)} | "
            f"Trades={candle['trade_count']}"
        )

        # -------------------------
        # Detect signal
        # -------------------------

        signal = detector.check(candle)

        if signal is None:
            return

        # -------------------------
        # Add extra data
        # -------------------------

        signal["symbol"] = symbol
        signal["price"] = candle["current"]
        signal["volume"] = candle["volume"]
        signal["trades"] = candle["trade_count"]

        # -------------------------
        # Prevent duplicate alerts
        # -------------------------

        if signal["type"] == "WATCH":
            candle["watch_sent"] = True

        elif signal["type"] == "CONFIRM":
            candle["confirm_sent"] = True

        logger.info(
            f"{signal['type']} | "
            f"{signal['direction']} | "
            f"{symbol} | "
            f"{signal['change']}%"
        )

        # -------------------------
        # Send to Telegram queue
        # -------------------------

        await alert_queue.put(signal)


scanner = Scanner()