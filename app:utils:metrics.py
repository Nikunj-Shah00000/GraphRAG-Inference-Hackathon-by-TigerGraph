import time


def calculate_cost(tokens, price_per_1k=0.0005):
    return (tokens / 1000) * price_per_1k


class Timer:
    def __init__(self):
        self.start_time = None
        self.end_time = None

    def start(self):
        self.start_time = time.time()

    def stop(self):
        self.end_time = time.time()

    def elapsed(self):
        return round(self.end_time - self.start_time, 2)