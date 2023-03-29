import math
import timesim
import numpy as np


class HumiditySensorSimulator:
    power_consumption = 1 # a szenzor fogyasztási értéke Ws (watt/sec)

    const = 35
    step = 360 / 86400 #egy leptetes erteke. Egy teljes periodus 360, ezt osztom egy nap masodperceinek a szamaval
    current_humidity = 0
    simulator_active = True

    noise_current_value = 0
    noise_step = 0
    noise_limit = np.random.normal(scale=3)

    def simulate_humidity(self):
        last_time_check = self.time_simulator.simulated_time
        while self.simulator_active:
            if self.time_simulator.simulated_time > last_time_check:
                last_time_check = self.time_simulator.simulated_time
                if self.noise_current_value <= self.noise_limit:
                    self.noise_step = self.noise_limit / 10000
                    self.noise_current_value = self.noise_current_value + self.noise_step
                else:
                    self.noise_limit = np.random.normal(scale=3)
                    self.noise_current_value = 0
                    self.noise_step = self.noise_step / 10000

                self.current_humidity = 10 * math.sin(self.time_simulator.simulated_time * self.step) + self.const + self.noise_current_value

            elif self.time_simulator.simulated_time < last_time_check:  # ez az ag arra van ha datum modositas lenne, akkor refreshelni kell a belso valtozokat
                last_time_check = self.time_simulator.simulated_time
    def __init__(self, time_simulator: timesim.TimeSimulator):
        self.time_simulator = time_simulator

    def stop_simulator(self):
        self.simulator_active = False

    def start_simulator(self):
        self.simulator_active = True

    def increase_humidity(self, amount):
        self.const = self.const + float(amount)

    def decrease_humidity(self, amount):
        self.const = self.const - amount