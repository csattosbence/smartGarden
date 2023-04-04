from simulator.humiditysensorsim import HumiditySensorSimulator
from simulator.timesim import TimeSimulator


class HumidifierSimulator:
    power_consumption = 60
    simulator_active = True

    humidifying_rate = 0.3 #ez adja meg hogy egy m'sodperc alatt hány fokot melegit a melegitő
    humidity_counter = 0 # ez adja meg hogy hány fokot melegitett a melegitő, ha ki van kapcsolva a melegitő ennyivel kell csökkenteni a hőfokot
    cooling_rate = 0.3
    system_on = False


    def __init__(self, time_simulator: TimeSimulator, humidity_sens_simulator: HumiditySensorSimulator):
        self.humidity_sens_simulator = humidity_sens_simulator
        self.time_simulator = time_simulator

    def simulate_humidifier(self):
        last_time_check = self.time_simulator.simulated_time
        while self.simulator_active:
            if self.time_simulator.simulated_time > last_time_check:

                if self.system_on:
                    self.humidity_sens_simulator.increase_humidity(self.humidifying_rate)
                    self.humidity_counter = self.humidifying_rate + self.humidity_counter

                elif not self.system_on and self.humidity_counter > 0:
                    self.humidity_counter = self.humidity_counter - self.cooling_rate
                    self.humidity_sens_simulator.decrease_humidity(self.cooling_rate)

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




