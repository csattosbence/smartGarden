import math
import threading
import time


class TempSimulator:
    const = 18
    step = 360 / 86400
    step_counter = 0
    current_temp = 0
    simulator_active = True

    def simulate_temp(self):
        f_second = 0
        f_last_inc = time.time()
        while self.simulator_active:
            if time.time() >= f_last_inc + 1:
                f_second += 1
                f_last_inc = time.time()
                self.step_counter = + self.step_counter + self.step
                self.current_temp = -0.5 * math.sin(self.step_counter) + self.const

    def stop_simulator(self):
        self.simulator_active = False

    def start_simulator(self):
        self.simulator_active = True

    def increase_temp(self, amount):
        self.const = self.const + float(amount)

    def decrease_temp(self, amount):
        self.const = self.const - amount