import asyncio

from app.formatter import format_alert
from app.telegram_client import telegram


class AlertQueue:

    def __init__(self):

        self.queue = asyncio.Queue()

    async def put(self, signal: dict):

        await self.queue.put(signal)

    async def worker(self):

        while True:

            signal = await self.queue.get()

            try:

                message = format_alert(signal)

                await telegram.send(message)

            except Exception as e:

                print(e)

            self.queue.task_done()


alert_queue = AlertQueue()