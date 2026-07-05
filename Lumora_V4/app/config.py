import os


class Config:

    # =====================================
    # APP
    # =====================================

    APP_NAME = "Lumora"
    VERSION = "4.1.0-STABLE"

    # =====================================
    # BINANCE
    # =====================================

    BINANCE_WS = "wss://fstream.binance.com/stream"

    BINANCE_REST = "https://fapi.binance.com"

    # Maximum symbols per websocket
    MAX_STREAMS = 10

    # =====================================
    # TELEGRAM
    # =====================================

    TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN", "")

    TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID", "")

    # =====================================
    # DETECTION
    # =====================================

    # Watch Alert
    WATCH_THRESHOLD = 5.0

    # Confirm Alert
    CONFIRM_THRESHOLD = 9.0

    # Minimum accumulated USDT volume
    MIN_VOLUME = 100000

    # Minimum trades before alert
    MIN_TRADES = 5

    # Candle length
    CANDLE_SECONDS = 900

    # Alert cooldown
    COOLDOWN_SECONDS = 900

    # Telegram timeframe text
    TIMEFRAME = "15m"

    # =====================================
    # DEBUG
    # =====================================

    DEBUG = True