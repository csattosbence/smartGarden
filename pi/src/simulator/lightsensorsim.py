import math
from simulator import timesim
import numpy as np



class LightSensorSimulator:

    power_consumption = 2 # a szenzor fogyasztási értéke Ws (watt/h)

    const = 1
    step = 2 * math.pi / 86400 #egy leptetes erteke. Egy teljes periodus 360, ezt osztom egy nap masodperceinek a szamaval
    current_light = 0
    simulator_active = True

    noise_current_value = 0
    noise_step = 0
    noise_limit = np.random.normal(scale=3)
    led_light_brightness = 0
    light_on = False


    def simulate_light(self):
        last_time_check = self.time_simulator.simulated_time
        while self.simulator_active:
            if self.time_simulator.simulated_time > last_time_check:
                self.current_light = 1000 * (math.sin( (self.time_simulator.simulated_time * (2 * math.pi / 86400) - math.pi / 2)) + 1) + self.led_light_brightness
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

    def turn_on_light(self, lux_amount):
        if 0 <= lux_amount:
            self.led_light_brightness = lux_amount

    def turn_off_light(self):
        self.led_light_brightness = 0


