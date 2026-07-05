import aiohttp

from app.config import Config
from app.logger import logger


class TelegramClient:

    def __init__(self):

        self.session = None

    async def start(self):

        if self.session is None:

            timeout = aiohttp.ClientTimeout(total=10)

            self.session = aiohttp.ClientSession(
                timeout=timeout
            )

    async def stop(self):

        if self.session:

            await self.session.close()

            self.session = None

    async def send(
        self,
        message: str,
    ):

        if not Config.TELEGRAM_TOKEN:

            logger.warning(
                "Telegram token missing."
            )

            return

        await self.start()

        url = (
            f"https://api.telegram.org/bot"
            f"{Config.TELEGRAM_TOKEN}"
            f"/sendMessage"
        )

        payload = {
            "chat_id": Config.TELEGRAM_CHAT_ID,
            "text": message,
            "parse_mode": "HTML",
            "disable_web_page_preview": True,
        }

        try:

            async with self.session.post(
                url,
                json=payload,
            ) as response:

                if response.status == 200:

                    logger.info(
                        "Telegram Alert Sent."
                    )

                else:

                    logger.error(
                        f"Telegram Error ({response.status}) -> "
                        f"{await response.text()}"
                    )

        except Exception as e:

            logger.exception(e)


telegram = TelegramClient()