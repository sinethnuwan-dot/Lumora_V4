from app.signal_strength import signal_strength


class SignalBuilder:

    def build(
        self,
        signal: dict,
        candle: dict,
        symbol: str,
    ) -> dict:

        signal["symbol"] = symbol

        signal["price"] = candle["current"]

        signal["volume"] = candle["volume"]

        signal["volume_speed"] = round(
            candle["volume_acceleration"],
            2,
        )

        signal["trades"] = candle["trade_count"]

        signal["ai_score"] = signal.get(
            "ai_score",
            0,
        )

        signal["strength"] = signal_strength.get(
            signal["ai_score"]
        )

        return signal


signal_builder = SignalBuilder()