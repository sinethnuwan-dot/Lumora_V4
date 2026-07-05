from app.config import Config


def format_alert(signal: dict) -> str:

    icon = {
        ("WATCH", "PUMP"): "👀📈",
        ("WATCH", "DUMP"): "👀📉",
        ("CONFIRM", "PUMP"): "🚀📈",
        ("CONFIRM", "DUMP"): "💥📉",
    }.get(
        (signal["type"], signal["direction"]),
        "📊",
    )

    message = (
        f"{icon} <b>{signal['type']} {signal['direction']}</b>\n\n"
        f"🪙 Coin : <b>{signal['symbol']}</b>\n"
        f"📈 Change : <b>{signal['change']:.2f}%</b>\n"
        f"💵 Price : <b>{signal['price']:.8f}</b>\n"
        f"💰 Volume : <b>{signal['volume']:,.0f} USDT</b>\n"
        f"📊 Trades : <b>{signal['trades']}</b>\n"
        f"⏱ Timeframe : <b>{Config.TIMEFRAME}</b>\n\n"
        f"⚡ {Config.APP_NAME} v{Config.VERSION}"
    )

    return message