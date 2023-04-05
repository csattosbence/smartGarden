from simulator.lightsensorsim import LightSensorSimulator
from simulator.timesim import TimeSimulator


class LightSimulator:
    current_brightness = 500
    max_brightness = 1500
    light_usage = current_brightness / max_brightness
    power_consumption = 40 * light_usage #W/h
    simulator_active = True
    system_on = False

    def __init__(self, time_simulator: TimeSimulator, light_sens_simulator: LightSensorSimulator):
        self.time_simulator = time_simulator
        self.light_sens_simulator = light_sens_simulator

    def simulate_light_system(self):
        last_time_check = self.time_simulator.simulated_time
        while self.simulator_active:
            if self.time_simulator.simulated_time > last_time_check:
                if self.system_on:
                    self.light_sens_simulator.turn_on_light(self.current_brightness)
                else:
                    self.light_sens_simulator.turn_off_light()

                last_time_check = self.time_simulator.simulated_time

            elif self.time_simulator.simulated_time < last_time_check: #ez az ag arra van ha datum modositas lenne, akkor refreshelni kell a belso valtozokat
                last_time_check = self.time_simulator.simulated_time
        return

    def stop_simulator(self):
        self.simulator_active = False

    def start_simulator(self):
        self.simulator_active = True

    def turn_on_system(self):
        self.system_on = True

    def turn_off_system(self):
        self.system_on = False

    def set_current_brightness(self, brightness):
        if brightness <= self.max_brightness:
            self.current_brightness = float(brightness)


    def set_max_brightness(self, max_brightness = 500):
        if 0 < max_brightness:
            self.max_brightness = self.max_brightness = max_brightness

