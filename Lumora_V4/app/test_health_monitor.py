from app.health_monitor import health_monitor

health_monitor.set_symbols(530)
health_monitor.set_websockets(53)

health_monitor.alert_sent()
health_monitor.alert_sent()

health_monitor.error()

print(health_monitor.stats())