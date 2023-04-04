from simulator.tempsim import TempSimulator
from simulator.timesim import TimeSimulator


class HeaterSimulator:
    power_consumption = 60
    simulator_active = True

    heating_rate = 0.2 #ez adja meg hogy egy m'sodperc alatt hány fokot melegit a melegitő
    heater_consumption = 10 #ez adja meg a melegitő fogyasztását Ws-ben (watt/mp)
    degree_counter = 0 # ez adja meg hogy hány fokot melegitett a melegitő, ha ki van kapcsolva a melegitő ennyivel kell csökkenteni a hőfokot
    cooling_rate = 0.3
    system_on = False


    def __init__(self, temp_simulator: TempSimulator, time_simulator: TimeSimulator()):
        self.temp_simulator = temp_simulator
        self.time_simulator = time_simulator

    def simulate_heater(self):
        last_time_check = self.time_simulator.simulated_time
        while self.simulator_active:
            if self.time_simulator.simulated_time > last_time_check:

                if self.system_on:
                    self.temp_simulator.increase_temp(self.heating_rate)
                    self.degree_counter = self.heating_rate + self.degree_counter

                elif not self.system_on and self.degree_counter > 0:
                    self.degree_counter = self.degree_counter - self.cooling_rate
                    self.temp_simulator.decrease_temp(self.cooling_rate)

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


