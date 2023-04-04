from datetime import datetime
import threading

from simulator.heatersim import HeaterSimulator
from simulator.humiditysensorsim import HumiditySensorSimulator
from simulator.tempsim import TempSimulator
from simulator.timesim import TimeSimulator


class ConsumptionSensorSimulator:
    simulator_active = True
    total_consumption = 0
    momentary_consumption = 0

    def __init__(self,
                 time_simulator: TimeSimulator,
                 heater_simulator: HeaterSimulator,
                 temp_simulator: TempSimulator,
                 humidity_sens_simulator: HumiditySensorSimulator):

        self.time_simulator = time_simulator
        self.heater_simulator = heater_simulator
        self.temp_simulator = temp_simulator
        self.humidity_sens_simulator = humidity_sens_simulator

    def simulate_consumption(self):
        last_time_check = self.time_simulator.simulated_time
        while self.simulator_active:
            temp_momentary_consumption = 0
            if self.time_simulator.simulated_time >= last_time_check + 1:
                #HEATER
                if self.heater_simulator.simulator_active:
                    self.total_consumption = self.total_consumption + self.heater_simulator.power_consumption
                    temp_momentary_consumption = temp_momentary_consumption + self.heater_simulator.power_consumption
                #TEMP SENSOR
                if self.temp_simulator.simulator_active:
                    self.total_consumption = self.total_consumption + self.temp_simulator.power_consumption
                    temp_momentary_consumption = temp_momentary_consumption + self.temp_simulator.power_consumption
                #HUMIDITY SENSOR
                if self.humidity_sens_simulator:
                    self.total_consumption = self.total_consumption + self.humidity_sens_simulator.power_consumption
                    temp_momentary_consumption = temp_momentary_consumption + self.humidity_sens_simulator.power_consumption


                last_time_check = self.time_simulator.simulated_time
                self.momentary_consumption = temp_momentary_consumption

            elif self.time_simulator.simulated_time < last_time_check:  # ez az ag arra van ha datum modositas lenne, akkor refreshelni kell a belso valtozokat
                last_time_check = self.time_simulator.simulated_time
        return

    def stop_simulator(self):
        self.simulator_active = False

    def start_simulator(self):
        self.simulator_active = True