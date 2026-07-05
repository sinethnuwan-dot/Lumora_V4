from app.detector import detector


tests = [

    {
        "name": "WATCH PASS",
        "open": 100,
        "current": 105.5,
        "volume": 300000,
        "trade_count": 350,
        "watch_sent": False,
        "confirm_sent": False,
    },

    {
        "name": "WATCH FAIL (AI)",
        "open": 100,
        "current": 105.0,
        "volume": 100000,
        "trade_count": 10,
        "watch_sent": False,
        "confirm_sent": False,
    },

    {
        "name": "CONFIRM PASS",
        "open": 100,
        "current": 110,
        "volume": 900000,
        "trade_count": 2500,
        "watch_sent": False,
        "confirm_sent": False,
    },

    {
        "name": "LOW VOLUME",
        "open": 100,
        "current": 110,
        "volume": 20000,
        "trade_count": 300,
        "watch_sent": False,
        "confirm_sent": False,
    },

    {
        "name": "LOW TRADES",
        "open": 100,
        "current": 110,
        "volume": 500000,
        "trade_count": 2,
        "watch_sent": False,
        "confirm_sent": False,
    },

]

print("=" * 70)

for candle in tests:

    print(f"\nTEST : {candle['name']}")

    result = detector.check(candle)

    print("RESULT :", result)

print("\n" + "=" * 70)