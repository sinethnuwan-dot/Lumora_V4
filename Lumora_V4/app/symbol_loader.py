import httpx

from app.config import Config
from app.logger import logger


async def load_symbols() -> list[str]:
    """
    Load all active USDT Perpetual Futures symbols from Binance.
    """

    url = f"{Config.BINANCE_REST}/fapi/v1/exchangeInfo"

    logger.info("Loading Binance Futures symbols...")

    async with httpx.AsyncClient(timeout=15) as client:

        response = await client.get(url)
        response.raise_for_status()

        data = response.json()

    symbols = []

    for symbol in data["symbols"]:

        if (
            symbol["quoteAsset"] == "USDT"
            and symbol["contractType"] == "PERPETUAL"
            and symbol["status"] == "TRADING"
        ):
            symbols.append(symbol["symbol"])

    symbols.sort()

    logger.info(f"Loaded {len(symbols)} symbols.")

    return symbols