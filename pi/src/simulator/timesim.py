import threading
import time
from datetime import datetime


class TimeSimulator:
    simulated_time = 0      # simulate time in unix timestamp format
    last_inc = time.time()
    simulator_active = True

    def __init__(self, date: datetime = datetime.now()):
        self.simulated_time = int(date.timestamp())

    def simulate_time(self):
        while True:
            if time.time() >= self.last_inc + 1:
                self.simulated_time += 1
                self.last_inc = time.time()

    def stop_simulator(self):
        self.simulator_active = False

    def start_simulator(self):
        self.simulator_active = True

    def set_date(self, date: datetime):
        self.simulated_time = int(date.timestamp())


#TEST
# time_simulator = TimeSimulator()
# t1 = threading.Thread(target=time_simulator.simulate_time)
#
# t1.start()
#
# run_time = datetime.now().timestamp() + 5
#
# while datetime.now().timestamp() < run_time:
#     print(time_simulator.simulated_time)
#
# time_simulator.set_date(datetime(2018, 12, 25))
#
# while True:
#     print(time_simulator.simulated_time)