from app.config import Config
from app.logger import logger


class Detector:

    def check(self, candle: dict):

        # -------------------------
        # Safety
        # -------------------------

        if candle["open"] <= 0:
            logger.warning("Invalid open price.")
            return None

        # -------------------------
        # Price Change %
        # -------------------------

        change = (
            (candle["current"] - candle["open"])
            / candle["open"]
        ) * 100

        logger.info(
            f"CHANGE -> "
            f"{change:.2f}% | "
            f"Volume={candle['volume']:.2f} | "
            f"Trades={candle['trade_count']}"
        )

        # -------------------------
        # Volume Filter
        # -------------------------

        if candle["volume"] < Config.MIN_VOLUME:

            logger.info(
                f"Volume Filter -> "
                f"{candle['volume']:.2f} / "
                f"{Config.MIN_VOLUME}"
            )

            return None

        # -------------------------
        # Trade Filter
        # -------------------------

        if candle["trade_count"] < Config.MIN_TRADES:

            logger.info(
                f"Trade Filter -> "
                f"{candle['trade_count']} / "
                f"{Config.MIN_TRADES}"
            )

            return None

        # -------------------------
        # WATCH
        # -------------------------

        if (
            not candle["watch_sent"]
            and abs(change) >= Config.WATCH_THRESHOLD
        ):

            logger.info(
                f"WATCH {change:.2f}%"
            )

            return {
                "type": "WATCH",
                "direction": (
                    "PUMP"
                    if change > 0
                    else "DUMP"
                ),
                "change": round(change, 2),
            }

        # -------------------------
        # CONFIRM
        # -------------------------

        if (
            not candle["confirm_sent"]
            and abs(change) >= Config.CONFIRM_THRESHOLD
        ):

            logger.info(
                f"CONFIRM {change:.2f}%"
            )

            return {
                "type": "CONFIRM",
                "direction": (
                    "PUMP"
                    if change > 0
                    else "DUMP"
                ),
                "change": round(change, 2),
            }

        # -------------------------
        # No Signal
        # -------------------------

        logger.info("No Signal")

        return None


detector = Detector()