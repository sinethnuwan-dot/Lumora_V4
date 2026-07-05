import asyncio

from app.logger import logger
from app.websocket_manager import manager
from app.alert_queue import alert_queue


async def main():

    logger.info("=" * 40)
    logger.info("Lumora V4 Started")
    logger.info("=" * 40)

    asyncio.create_task(
        alert_queue.worker()
    )

    await manager.start()


if __name__ == "__main__":

    asyncio.run(main())