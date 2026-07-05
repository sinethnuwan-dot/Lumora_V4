import time


class HealthMonitor:

    def __init__(self):

        self.started = time.time()

        self.symbols = 0
        self.websockets = 0
        self.alerts = 0
        self.errors = 0

    def set_symbols(self, count: int):

        self.symbols = count

    def set_websockets(self, count: int):

        self.websockets = count

    def alert_sent(self):

        self.alerts += 1

    def error(self):

        self.errors += 1

    def uptime(self):

        return int(time.time() - self.started)

    def stats(self):

        return {
            "uptime": self.uptime(),
            "symbols": self.symbols,
            "websockets": self.websockets,
            "alerts": self.alerts,
            "errors": self.errors,
        }


health_monitor = HealthMonitor()