from datetime import datetime
import threading

from simulator.heatersim import HeaterSimulator
from simulator.humidifier import HumidifierSimulator
from simulator.humiditysensorsim import HumiditySensorSimulator
from simulator.lightsensorsim import LightSensorSimulator
from simulator.lightsim import LightSimulator
from simulator.soilmoisturesensorsim import SoilMoistureSensorSimulator
from simulator.tempsim import TempSimulator
from simulator.timesim import TimeSimulator
from simulator.watersystemsim import WateringSystemSimulator


class ConsumptionSensorSimulator:
    simulator_active = True
    total_consumption = 0
    momentary_consumption = 0

    def __init__(self,
                 time_simulator: TimeSimulator,
                 heater_simulator: HeaterSimulator,
                 temp_simulator: TempSimulator,
                 humidity_sens_simulator: HumiditySensorSimulator,
                 humidifier_simulator: HumidifierSimulator,
                 light_sens_simulator: LightSensorSimulator,
                 light_simulator: LightSimulator,
                 soil_moist_sens_simulator: SoilMoistureSensorSimulator,
                 watering_system_simulator: WateringSystemSimulator):

        self.time_simulator = time_simulator
        self.heater_simulator = heater_simulator
        self.temp_simulator = temp_simulator
        self.humidity_sens_simulator = humidity_sens_simulator
        self.humidifier_simulator = humidifier_simulator
        self.light_sens_simulator = light_sens_simulator
        self.light_simulator = light_simulator
        self.soil_moist_sens_simulator = soil_moist_sens_simulator
        self.watering_system_simulator = watering_system_simulator

    def simulate_consumption(self):
        last_time_check = self.time_simulator.simulated_time
        while self.simulator_active:
            temp_momentary_consumption = 0
            if self.time_simulator.simulated_time >= last_time_check + 1:
                #HEATER
                if self.heater_simulator.system_on:
                    self.total_consumption = self.total_consumption + self.heater_simulator.power_consumption / 3600
                    temp_momentary_consumption = temp_momentary_consumption + self.heater_simulator.power_consumption
                #TEMP SENSOR
                if self.temp_simulator.system_on:
                    self.total_consumption = self.total_consumption + self.temp_simulator.power_consumption / 3600
                    temp_momentary_consumption = temp_momentary_consumption + self.temp_simulator.power_consumption
                #HUMIDITY SENSOR
                if self.humidity_sens_simulator.system_on:
                    self.total_consumption = self.total_consumption + self.humidity_sens_simulator.power_consumption / 3600
                    temp_momentary_consumption = temp_momentary_consumption + self.humidity_sens_simulator.power_consumption
                #HUMIDIFIER
                if self.humidifier_simulator.system_on:
                    self.total_consumption = self.total_consumption + self.humidifier_simulator.power_consumption / 3600
                    temp_momentary_consumption = temp_momentary_consumption + self.humidifier_simulator.power_consumption
                #SOIL MOIST SENSOR
                if self.soil_moist_sens_simulator.system_on:
                    self.total_consumption = self.total_consumption + self.soil_moist_sens_simulator.power_consumption / 3600
                    temp_momentary_consumption = temp_momentary_consumption + self.soil_moist_sens_simulator.power_consumption
                #WATERING SYSTEM
                if self.watering_system_simulator.system_on:
                    self.total_consumption = self.total_consumption + self.watering_system_simulator.power_consumption / 3600
                    temp_momentary_consumption = temp_momentary_consumption + self.watering_system_simulator.power_consumption
                #LIGHT SENS SIMULATOR
                if self.light_sens_simulator.system_on:
                    self.total_consumption = self.total_consumption + self.light_sens_simulator.power_consumption / 3600
                    temp_momentary_consumption = temp_momentary_consumption + self.light_sens_simulator.power_consumption
                #LIGHT SYSTEM
                if self.light_simulator:
                    self.total_consumption = self.total_consumption + self.light_simulator.power_consumption / 3600
                    temp_momentary_consumption = temp_momentary_consumption + self.light_simulator.power_consumption

                last_time_check = self.time_simulator.simulated_time
                self.momentary_consumption = temp_momentary_consumption

            elif self.time_simulator.simulated_time < last_time_check:
                last_time_check = self.time_simulator.simulated_time
        return

    def stop_simulator(self):
        self.simulator_active = False

    def start_simulator(self):
        self.simulator_active = True