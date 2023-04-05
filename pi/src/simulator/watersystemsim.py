from simulator.soilmoisturesensorsim import SoilMoistureSensorSimulator
from simulator.timesim import TimeSimulator


class WateringSystemSimulator:
    power_consumption = 30
    simulator_active = True
    system_on = False

    def __init__(self,time_simulator: TimeSimulator, soil_moist_sens_simulator: SoilMoistureSensorSimulator):
        self.time_simulator = time_simulator
        self.soil_moist_sens_simulator = soil_moist_sens_simulator

    def simulate_watering_system(self):
        last_time_check = self.time_simulator.simulated_time
        while self.simulator_active:
            if self.time_simulator.simulated_time > last_time_check + 1:
                if self.system_on:
                    if self.soil_moist_sens_simulator.current_soil_moisture < 80:
                        if self.soil_moist_sens_simulator.ticker > 20000:
                            self.soil_moist_sens_simulator.ticker = self.soil_moist_sens_simulator.ticker - 20000
                        else:
                            self.soil_moist_sens_simulator.ticker = self.soil_moist_sens_simulator.ticker - self.soil_moist_sens_simulator.ticker
                last_time_check = self.time_simulator.simulated_time
            elif self.time_simulator.simulated_time < last_time_check:  # ez az ag arra van ha datum modositas lenne, akkor refreshelni kell a belso valtozokat
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


