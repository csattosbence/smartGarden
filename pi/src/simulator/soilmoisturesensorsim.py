from simulator.timesim import TimeSimulator


class SoilMoistureSensorSimulator:
    system_on = True
    max_soil_moisture = 80
    power_consumption = 3

    drying_time = 259200 # az idő amely alatt a talaj teljesen kiszárad másodpercben. Jelen pillanatban 3 nap
    current_soil_moisture = max_soil_moisture #Kezdő talaj nedvesség érték 80, ez a maximális érték
    slope = max_soil_moisture / drying_time #Függvény meredekség, amely megadja, hogy mennyivel kell csőkkenteni a talajnedvességet másodpercenkét
    simulator_active = True
    ticker = 200000

    def __init__(self, time_simulator: TimeSimulator):
        self.time_simulator = time_simulator


    def simulate_soil_moisture(self):
        last_time_check = self.time_simulator.simulated_time
        while self.simulator_active:
            if self.time_simulator.simulated_time > last_time_check + 1:
                if self.system_on:
                    self.ticker = self.ticker + 1
                    self.current_soil_moisture = -1 * self.slope * self.ticker + self.max_soil_moisture

                last_time_check = self.time_simulator.simulated_time

            elif self.time_simulator.simulated_time < last_time_check:
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


