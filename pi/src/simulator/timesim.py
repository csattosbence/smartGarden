import threading
import time
from datetime import datetime


class TimeSimulator:
    ticker_on = True
    simulated_time = 0      # simulate time in unix timestamp format
    last_inc = time.time()
    simulator_active = True
    ticker_speed = 1

    def __init__(self, date: datetime = datetime.now()):
        self.simulated_time = int(date.timestamp())

    def simulate_time(self):
        while self.simulator_active:
            if self.ticker_on:
                if time.time() >= self.last_inc + self.ticker_speed:
                    self.simulated_time += 1
                    self.last_inc = time.time()
        return

    def stop_simulator(self):
        self.simulator_active = False

    def resume_ticker(self):
        self.ticker_on = True

    def stop_ticker(self):
        self.ticker_on = False

    def start_simulator(self):
        self.simulator_active = True

    def set_date(self, date: datetime):
        self.simulated_time = int(date.timestamp())