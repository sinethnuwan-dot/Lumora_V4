class AIScore:

    def calculate(
        self,
        change: float,
        volume: float,
        trades: int,
        volume_speed: float,
    ) -> int:

        score = 0

        # -------------------------
        # Price Change (30)
        # -------------------------

        score += min(
            abs(change) * 3,
            30,
        )

        # -------------------------
        # Volume (25)
        # -------------------------

        score += min(
            volume / 40000,
            25,
        )

        # -------------------------
        # Trades (20)
        # -------------------------

        score += min(
            trades / 100,
            20,
        )

        # -------------------------
        # Volume Speed (25)
        # -------------------------

        score += min(
            volume_speed / 400,
            25,
        )

        return min(
            round(score),
            100,
        )


ai_score = AIScore()