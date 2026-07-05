import asyncio

from app.alert_queue import alert_queue
from app.formatter import format_alert


async def main():

    # Start queue worker
    asyncio.create_task(
        alert_queue.worker()
    )

    # WATCH Signal Test
    watch_signal = {
        "type": "WATCH",
        "direction": "PUMP",
        "symbol": "BTCUSDT",
        "change": 5.23,
        "price": 110250.75,
        "volume": 250000,
        "trades": 126,
    }

    # CONFIRM Signal Test
    confirm_signal = {
        "type": "CONFIRM",
        "direction": "PUMP",
        "symbol": "BTCUSDT",
        "change": 9.84,
        "price": 114830.15,
        "volume": 680000,
        "trades": 482,
    }

    print("=" * 60)
    print(format_alert(watch_signal))

    await alert_queue.put(watch_signal)

    await asyncio.sleep(2)

    print("=" * 60)
    print(format_alert(confirm_signal))

    await alert_queue.put(confirm_signal)

    await asyncio.sleep(5)


if __name__ == "__main__":
    asyncio.run(main())