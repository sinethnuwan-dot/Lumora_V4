class SignalStrength:

    def get(self, score: int):

        if score >= 95:
            return "🔴 EXTREME"

        if score >= 80:
            return "🟠 STRONG"

        if score >= 60:
            return "🟡 GOOD"

        if score >= 40:
            return "🟢 WEAK"

        return "⚪ VERY WEAK"


signal_strength = SignalStrength()