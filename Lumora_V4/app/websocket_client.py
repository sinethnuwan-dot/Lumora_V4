import asyncio

import aiohttp
import orjson

from app.logger import logger
from app.scanner import scanner


class BinanceWebSocket:

    def __init__(self, stream_url: str):

        self.stream_url = stream_url

    async def start(self):

        while True:

            try:

                logger.info(
                    f"Connecting -> {self.stream_url}"
                )

                async with aiohttp.ClientSession() as session:

                    async with session.ws_connect(
                        self.stream_url,
                        heartbeat=30,
                    ) as ws:

                        logger.info(
                            "WebSocket Connected."
                        )

                        async for msg in ws:

                            if msg.type != aiohttp.WSMsgType.TEXT:
                                continue

                            try:

                                payload = orjson.loads(
                                    msg.data
                                )

                                # Combined stream payload
                                trade = payload["data"]

                                symbol = trade["s"]
                                price = float(trade["p"])
                                quantity = float(trade["q"])

                                await scanner.process_trade(
                                    symbol=symbol,
                                    price=price,
                                    quantity=quantity,
                                )

                            except Exception as e:

                                logger.exception(e)

            except Exception as e:

                logger.exception(e)

            logger.warning(
                "Reconnecting in 5 seconds..."
            )

            await asyncio.sleep(5)