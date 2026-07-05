from app.ai_score import ai_score


tests = [

    {
        "change": 5.2,
        "volume": 120000,
        "trades": 150,
        "speed": 800,
    },

    {
        "change": 6.8,
        "volume": 350000,
        "trades": 620,
        "speed": 4500,
    },

    {
        "change": 9.5,
        "volume": 1500000,
        "trades": 2400,
        "speed": 18000,
    },

    {
        "change": -8.1,
        "volume": 750000,
        "trades": 980,
        "speed": 9500,
    },

]


print("=" * 60)

for test in tests:

    score = ai_score.calculate(
        change=test["change"],
        volume=test["volume"],
        trades=test["trades"],
        volume_speed=test["speed"],
    )

    print(
        f"Change={test['change']}% | "
        f"Volume={test['volume']:,.0f} | "
        f"Trades={test['trades']} | "
        f"Speed={test['speed']:,.0f} | "
        f"AI={score}/100"
    )

print("=" * 60)