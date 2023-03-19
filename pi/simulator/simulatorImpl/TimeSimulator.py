import threading
import time
from datetime import datetime


class TimeSimulator:
    simulated_time = 0
    last_inc = time.time()

    def __init__(self, date: datetime = datetime.now()):
        self.simulated_time = int(date.timestamp())

    def simulate_time(self):
        while True:
            if time.time() >= self.last_inc + 1:
                self.simulated_time += 1
                self.last_inc = time.time()


    def run(self):
        thread = threading.Thread(target=self.simulate_time)
        thread.start()
        thread.join()

    def set_date(self,date: datetime):
        self.unix_timestamp = int(date.timestamp())
