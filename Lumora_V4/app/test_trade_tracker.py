from app.trade_tracker import trade_tracker


trade_tracker.update(
    "BTCUSDT",
    100.0,
    10.0,
)

trade_tracker.update(
    "BTCUSDT",
    105.0,
    5.0,
)

trade_tracker.update(
    "BTCUSDT",
    98.0,
    3.0,
)

print(trade_tracker.get("BTCUSDT"))