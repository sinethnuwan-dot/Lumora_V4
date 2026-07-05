from app.volume_acceleration import volume_acceleration


tests = [

    (100000, 150000, 60),

    (200000, 700000, 30),

    (500000, 510000, 120),

]


print("=" * 50)

for previous, current, seconds in tests:

    value = volume_acceleration.calculate(
        previous,
        current,
        seconds,
    )

    print(
        previous,
        "->",
        current,
        "|",
        seconds,
        "sec",
        "=",
        round(value, 2),
        "USDT/sec",
    )

print("=" * 50)