from app.scanner import scanner

prices = [
    100,
    101,
    102,
    103,
    104,
    105,
    106,
    107,
    108,
    109,
    110,
]

for price in prices:

    signal = scanner.process_trade(
        "BTCUSDT",
        price,
        10000,
    )

    if signal:
        print(signal)