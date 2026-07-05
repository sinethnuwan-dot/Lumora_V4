import asyncio

from app.chunker import chunk_symbols
from app.config import Config
from app.logger import logger
from app.symbol_loader import load_symbols
from app.websocket_client import BinanceWebSocket


class WebSocketManager:

    async def start(self):

        logger.info("Loading symbols...")

        symbols = await load_symbols()

        logger.info(
            f"Loaded {len(symbols)} symbols."
        )

        chunks = chunk_symbols(
            symbols,
            Config.MAX_STREAMS,
        )

        logger.info(
            f"Creating {len(chunks)} websocket connections..."
        )

        tasks = []

        for index, chunk in enumerate(chunks, start=1):

            logger.info(
                f"WS-{index} -> {len(chunk)} symbols"
            )

            streams = [
                f"{symbol.lower()}@trade"
                for symbol in chunk
            ]

            stream_url = (
                Config.BINANCE_WS
                + "?streams="
                + "/".join(streams)
            )

            websocket = BinanceWebSocket(
                stream_url
            )

            tasks.append(
                asyncio.create_task(
                    websocket.start()
                )
            )

        await asyncio.gather(*tasks)


manager = WebSocketManager()


async def test():

    await manager.start()


if __name__ == "__main__":

    asyncio.run(test())