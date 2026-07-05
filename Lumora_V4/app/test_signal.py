import asyncio

from app.formatter import format_alert
from app.telegram_client import telegram


signals = [

    {
        "type": "WATCH",
        "direction": "PUMP",
        "symbol": "BTCUSDT",
        "price": 110250.45,
        "change": 5.34,
        "volume": 486240,
        "volume_speed": 8420.12,
        "trades": 1243,
        "ai_score": 72,
        "strength": "🟡 GOOD",
    },

    {
        "type": "CONFIRM",
        "direction": "PUMP",
        "symbol": "BTCUSDT",
        "price": 114830.15,
        "change": 9.84,
        "volume": 1680420,
        "volume_speed": 18540.82,
        "trades": 5842,
        "ai_score": 96,
        "strength": "🔴 EXTREME",
    },

    {
        "type": "CONFIRM",
        "direction": "DUMP",
        "symbol": "ETHUSDT",
        "price": 3245.80,
        "change": -10.42,
        "volume": 2120650,
        "volume_speed": 21320.66,
        "trades": 7120,
        "ai_score": 98,
        "strength": "🔴 EXTREME",
    },

]


async def main():

    for signal in signals:

        message = format_alert(signal)

        print("=" * 60)
        print(message)

        await telegram.send(message)

        await asyncio.sleep(2)


if __name__ == "__main__":

    asyncio.run(main())