from app.config import Config


def format_alert(signal: dict) -> str:

    # =====================================
    # WATCH PUMP
    # =====================================

    if (
        signal["type"] == "WATCH"
        and signal["direction"] == "PUMP"
    ):

        return (
            "👀📈 <b>WATCH PUMP</b>\n\n"

            f"🪙 Coin       : <b>{signal['symbol']}</b>\n"
            f"💵 Price      : <b>{signal['price']:.8f}</b>\n"
            f"📈 Change     : <b>+{signal['change']:.2f}%</b>\n"
            f"💰 Volume     : <b>{signal['volume']:,.0f} USDT</b>\n"
            f"⚡ Vol Speed  : <b>{signal['volume_speed']:,.2f} USDT/s</b>\n"
            f"📊 Trades     : <b>{signal['trades']}</b>\n\n"

            f"🤖 AI Score   : <b>{signal['ai_score']}/100</b>\n"
            f"🔥 Strength   : <b>{signal['strength']}</b>\n\n"

            "━━━━━━━━━━━━━━━━━━━━\n\n"

            "👀 <b>Monitor this coin.</b>\n"
            "Waiting for <b>CONFIRM</b> signal...\n\n"

            "━━━━━━━━━━━━━━━━━━━━\n\n"

            f"⏱ Timeframe  : <b>{Config.TIMEFRAME}</b>\n\n"

            f"⚡ {Config.APP_NAME} v{Config.VERSION}"
        )

    # =====================================
    # WATCH DUMP
    # =====================================

    if (
        signal["type"] == "WATCH"
        and signal["direction"] == "DUMP"
    ):

        return (
            "👀📉 <b>WATCH DUMP</b>\n\n"

            f"🪙 Coin       : <b>{signal['symbol']}</b>\n"
            f"💵 Price      : <b>{signal['price']:.8f}</b>\n"
            f"📉 Change     : <b>{signal['change']:.2f}%</b>\n"
            f"💰 Volume     : <b>{signal['volume']:,.0f} USDT</b>\n"
            f"⚡ Vol Speed  : <b>{signal['volume_speed']:,.2f} USDT/s</b>\n"
            f"📊 Trades     : <b>{signal['trades']}</b>\n\n"

            f"🤖 AI Score   : <b>{signal['ai_score']}/100</b>\n"
            f"🔥 Strength   : <b>{signal['strength']}</b>\n\n"

            "━━━━━━━━━━━━━━━━━━━━\n\n"

            "👀 <b>Monitor this coin.</b>\n"
            "Waiting for <b>CONFIRM</b> signal...\n\n"

            "━━━━━━━━━━━━━━━━━━━━\n\n"

            f"⏱ Timeframe  : <b>{Config.TIMEFRAME}</b>\n\n"

            f"⚡ {Config.APP_NAME} v{Config.VERSION}"
        )

    # =====================================
    # CONFIRM PUMP
    # =====================================

    if (
        signal["type"] == "CONFIRM"
        and signal["direction"] == "PUMP"
    ):

        return (
            "🚀📈 <b>CONFIRM PUMP</b>\n\n"

            f"🪙 Coin       : <b>{signal['symbol']}</b>\n"
            f"💵 Price      : <b>{signal['price']:.8f}</b>\n"
            f"📈 Change     : <b>+{signal['change']:.2f}%</b>\n"
            f"💰 Volume     : <b>{signal['volume']:,.0f} USDT</b>\n"
            f"⚡ Vol Speed  : <b>{signal['volume_speed']:,.2f} USDT/s</b>\n"
            f"📊 Trades     : <b>{signal['trades']}</b>\n\n"

            f"🤖 AI Score   : <b>{signal['ai_score']}/100</b>\n"
            f"🔥 Strength   : <b>{signal['strength']}</b>\n\n"

            "━━━━━━━━━━━━━━━━━━━━\n\n"

            "🟢 <b>ENTER LONG TRADE NOW</b>\n\n"

            "━━━━━━━━━━━━━━━━━━━━\n\n"

            f"⏱ Timeframe  : <b>{Config.TIMEFRAME}</b>\n\n"

            f"⚡ {Config.APP_NAME} v{Config.VERSION}"
        )

    # =====================================
    # CONFIRM DUMP
    # =====================================

    return (

        "💥📉 <b>CONFIRM DUMP</b>\n\n"

        f"🪙 Coin       : <b>{signal['symbol']}</b>\n"
        f"💵 Price      : <b>{signal['price']:.8f}</b>\n"
        f"📉 Change     : <b>{signal['change']:.2f}%</b>\n"
        f"💰 Volume     : <b>{signal['volume']:,.0f} USDT</b>\n"
        f"⚡ Vol Speed  : <b>{signal['volume_speed']:,.2f} USDT/s</b>\n"
        f"📊 Trades     : <b>{signal['trades']}</b>\n\n"

        f"🤖 AI Score   : <b>{signal['ai_score']}/100</b>\n"
        f"🔥 Strength   : <b>{signal['strength']}</b>\n\n"

        "━━━━━━━━━━━━━━━━━━━━\n\n"

        "🔴 <b>ENTER SHORT TRADE NOW</b>\n\n"

        "━━━━━━━━━━━━━━━━━━━━\n\n"

        f"⏱ Timeframe  : <b>{Config.TIMEFRAME}</b>\n\n"

        f"⚡ {Config.APP_NAME} v{Config.VERSION}"
    )