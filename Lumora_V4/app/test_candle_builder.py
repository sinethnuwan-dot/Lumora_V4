from app.candle_builder import candle_builder


prices = [100, 102, 99, 105, 103]

for price in prices:

    candle = candle_builder.update(
        "BTCUSDT",
        price,
        10,
    )

print(candle)