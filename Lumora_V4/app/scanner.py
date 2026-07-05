from app.alert_queue import alert_queue
from app.detector import detector
from app.logger import logger
from app.signal_builder import signal_builder
from app.trade_tracker import trade_tracker


class Scanner:

    async def process_trade(
        self,
        symbol: str,
        price: float,
        quantity: float,
    ) -> None:

        # -------------------------
        # Update Live Candle
        # -------------------------

        candle = trade_tracker.update(
            symbol=symbol,
            price=price,
            quantity=quantity,
        )

        if candle is None:
            return

        # -------------------------
        # Detect Signal
        # -------------------------

        signal = detector.check(candle)

        if signal is None:
            return

        # -------------------------
        # Build Signal
        # -------------------------

        signal = signal_builder.build(
            signal=signal,
            candle=candle,
            symbol=symbol,
        )

        # -------------------------
        # Prevent Duplicate Alerts
        # -------------------------

        if signal["type"] == "WATCH":

            candle["watch_sent"] = True

        elif signal["type"] == "CONFIRM":

            candle["confirm_sent"] = True

        # -------------------------
        # Signal Log
        # -------------------------

        logger.info(
            f"{signal['type']} | "
            f"{signal['direction']} | "
            f"{signal['symbol']} | "
            f"{signal['change']}% | "
            f"AI={signal['ai_score']} | "
            f"Strength={signal['strength']}"
        )

        # -------------------------
        # Queue Telegram Alert
        # -------------------------

        await alert_queue.put(signal)

        logger.info(
            f"Telegram Queue -> "
            f"{signal['symbol']}"
        )


scanner = Scanner()