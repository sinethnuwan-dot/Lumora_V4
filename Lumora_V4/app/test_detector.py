from app.detector import detector

candle = {
    "open": 100,
    "close": 110,
    "volume": 200000,
    "trade_count": 150,
    "watch_sent": False,
    "confirm_sent": False,
}

print(detector.check(candle))