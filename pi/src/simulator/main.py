
import threading

from simulator.heater import HeaterSimulator
from simulator.temp import TempSimulator
from simulator.time import TimeSimulator


class Simulator:
    simulator_active = False
    temp_simulator = TempSimulator()
    heater_simulator = HeaterSimulator(temp_simulator)
    time_simulator = TimeSimulator()

    t1 = threading.Thread(target=temp_simulator.simulate_temp)
    t2 = threading.Thread(target=heater_simulator.simulate_heater)
    t3 = threading.Thread(target=time_simulator.simulate_time)

    def run_simulator(self):
        self.t1.start()
        self.t2.start()
        self.t3.start()

    def get_time(self):
        return self.time_simulator.simulated_time

    def get_temp(self):
        return str(self.temp_simulator.current_temp)

    def stop_simulator(self):
        self.temp_simulator.stop_simulator()
        self.time_simulator.stop_simulator()

    def start_simulator(self):
        self.temp_simulator.start_simulator()
        self.time_simulator.start_simulator()


simulator = Simulator()
