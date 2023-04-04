import math

from numpy import random

from simulator import timesim


class TempSimulator:
    power_consumption = 1 / 3600
    const = 18
    step = 2 * math.pi / 86400  #egy leptetes erteke. Egy teljes periodus 2pi, ezt osztom egy nap masodperceinek a szamaval
    current_temp = 0
    simulator_active = True

    noise_current_value = 0
    noise_step = 0
    noise_limit = random.normal(scale=3)

    def simulate_temp(self):
        last_time_check = self.time_simulator.simulated_time
        while self.simulator_active:
            if self.time_simulator.simulated_time > last_time_check:

                if self.noise_current_value <= self.noise_limit:
                    self.noise_step = self.noise_limit / 10000
                    self.noise_current_value = self.noise_current_value + self.noise_step
                else:
                    self.noise_limit = random.normal(scale=3)
                    self.noise_current_value = 0
                    self.noise_step = self.noise_step / 10000

                self.current_temp = -6 * math.sin(self.time_simulator.simulated_time * self.step + 1.5) + self.const + self.noise_current_value

                last_time_check = self.time_simulator.simulated_time
            elif self.time_simulator.simulated_time < last_time_check:  # ez az ag arra van ha datum modositas lenne, akkor refreshelni kell a belso valtozokat
                last_time_check = self.time_simulator.simulated_time
        return

    def __init__(self, time_simulator: timesim.TimeSimulator):
        self.time_simulator = time_simulator

    def stop_simulator(self):
        self.simulator_active = False

    def start_simulator(self):
        self.simulator_active = True

    def increase_temp(self, amount):
        self.const = self.const + float(amount)

    def decrease_temp(self, amount):
        self.const = self.const - amount