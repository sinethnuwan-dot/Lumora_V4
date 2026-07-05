import asyncio

from app.symbol_loader import load_symbols


async def main():

    symbols = await load_symbols()

    print(f"\nLoaded {len(symbols)} symbols\n")

    print(symbols[:20])


asyncio.run(main())