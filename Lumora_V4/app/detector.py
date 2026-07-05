from app.ai_score import ai_score
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

        # -------------------------
        # AI Score V2
        # -------------------------

        score = ai_score.calculate(
            change=change,
            volume=candle["volume"],
            trades=candle["trade_count"],
            volume_speed=candle["volume_acceleration"],
        )

        # -------------------------
        # Volume Filter
        # -------------------------

        if candle["volume"] < Config.MIN_VOLUME:
            return None

        # -------------------------
        # Trade Filter
        # -------------------------

        if candle["trade_count"] < Config.MIN_TRADES:
            return None

        # ==================================================
        # CONFIRM (Higher Priority)
        # ==================================================

        if (
            not candle["confirm_sent"]
            and abs(change) >= Config.CONFIRM_THRESHOLD
        ):

            if score < 80:

                logger.info(
                    f"CONFIRM Rejected (AI={score})"
                )

                return None

            logger.info(
                f"CONFIRM {change:.2f}% | "
                f"AI={score}"
            )

            return {
                "type": "CONFIRM",
                "direction": (
                    "PUMP"
                    if change > 0
                    else "DUMP"
                ),
                "change": round(change, 2),
                "ai_score": score,
                "volume_speed": round(
                    candle["volume_acceleration"],
                    2,
                ),
            }

        # ==================================================
        # WATCH
        # ==================================================

        if (
            not candle["watch_sent"]
            and abs(change) >= Config.WATCH_THRESHOLD
        ):

            if score < 50:

                logger.info(
                    f"WATCH Rejected (AI={score})"
                )

                return None

            logger.info(
                f"WATCH {change:.2f}% | "
                f"AI={score}"
            )

            return {
                "type": "WATCH",
                "direction": (
                    "PUMP"
                    if change > 0
                    else "DUMP"
                ),
                "change": round(change, 2),
                "ai_score": score,
                "volume_speed": round(
                    candle["volume_acceleration"],
                    2,
                ),
            }

        return None


detector = Detector()