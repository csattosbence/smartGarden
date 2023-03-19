import threading
import time

from simulator.simulatorImpl.TempSimulator import TempSimulator


class HeaterSimulator:
    heatCounter = 0

    def __init__(self, temp_simulator: TempSimulator):
        self.temp_simulator = temp_simulator

    def simulate_heater(self):
        f_second = 0
        f_last_inc = time.time()
        while True:
            if time.time() >= f_last_inc + 1:
                f_second += 1
                f_last_inc = time.time()
                self.heatCounter = self.heatCounter + 0.03

    def run(self):
        thread = threading.Thread(target=self.simulate_heater())
        thread.start()
        thread.join()
