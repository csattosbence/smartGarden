from datetime import datetime
import threading

from simulator.consumptionsensorsim import ConsumptionSensorSimulator
from simulator.heatersim import HeaterSimulator
from simulator.tempsim import TempSimulator
from simulator.timesim import TimeSimulator
from simulator.humiditysensorsim import HumiditySensorSimulator


class Simulator:
    simulator_active = False
    time_simulator = TimeSimulator()
    temp_simulator = TempSimulator(time_simulator)
    heater_simulator = HeaterSimulator(temp_simulator, time_simulator)
    humidity_sens_simulator = HumiditySensorSimulator(time_simulator)
    consumption_sens_simulator = ConsumptionSensorSimulator(time_simulator,
                                                            heater_simulator,
                                                            temp_simulator,
                                                            humidity_sens_simulator)

    t1 = threading.Thread(target=temp_simulator.simulate_temp)
    t2 = threading.Thread(target=heater_simulator.simulate_heater)
    t3 = threading.Thread(target=time_simulator.simulate_time)
    t4 = threading.Thread(target=humidity_sens_simulator.simulate_humidity)
    t5 = threading.Thread(target=consumption_sens_simulator.simulate_consumption)


    def run_simulator(self):
        self.t1.start()
        self.t2.start()
        self.t3.start()
        self.t4.start()
        self.t5.start()

    def stop_simulator(self):
        self.temp_simulator.stop_simulator()
        self.heater_simulator.stop_simulator()
        self.time_simulator.stop_simulator()
        self.humidity_sens_simulator.stop_simulator()
        self.consumption_sens_simulator.stop_simulator()

        self.t1.join()
        self.t2.join()
        self.t3.join()
        self.t4.join()

    def get_time(self):
        return self.time_simulator.simulated_time

    def get_temp(self):
        return str(self.temp_simulator.current_temp)

    def start_simulator(self):
        self.temp_simulator.start_simulator()
        self.time_simulator.start_simulator()
        self.humidity_sens_simulator.start_simulator()
        self.heater_simulator.start_simulator()


simulator = Simulator()




simulator.run_simulator()

run_time = datetime.now().timestamp() + 5

while datetime.now().timestamp() < run_time:
    print(" DATE -- " + str(datetime.fromtimestamp(simulator.time_simulator.simulated_time)) + "\n" +
          " CURRENT TEMP -- " + str(simulator.temp_simulator.current_temp) + "\n" +
          " CURRENT HUMIDITY -- " + str(simulator.humidity_sens_simulator.current_humidity) + "\n" +
          " POWER CONSUMPTION -- " + "TOTAL --" + str(simulator.consumption_sens_simulator.total_consumption) + "W" +
          " MOMENTARY -- " + str(simulator.consumption_sens_simulator.momentary_consumption) + "W/s" + "\n")

run_time = datetime.now().timestamp() + 5

simulator.heater_simulator.is_heater_on = False

while datetime.now().timestamp() < run_time:
    print(" DATE -- " + str(datetime.fromtimestamp(simulator.time_simulator.simulated_time)) + "\n" +
          " CURRENT TEMP -- " + str(simulator.temp_simulator.current_temp) + "\n" +
          " CURRENT HUMIDITY -- " + str(simulator.humidity_sens_simulator.current_humidity) + "\n" +
          " POWER CONSUMPTION -- " + "TOTAL --" + str(simulator.consumption_sens_simulator.total_consumption) + "W" +
          " MOMENTARY -- " + str(simulator.consumption_sens_simulator.momentary_consumption) + "W/s" + "\n")

run_time = datetime.now().timestamp() + 5

simulator.time_simulator.set_date(datetime(2012,12,12))

while datetime.now().timestamp() < run_time:
    print(" DATE -- " + str(datetime.fromtimestamp(simulator.time_simulator.simulated_time)) + "\n" +
          " CURRENT TEMP -- " + str(simulator.temp_simulator.current_temp) + "\n" +
          " CURRENT HUMIDITY -- " + str(simulator.humidity_sens_simulator.current_humidity) + "\n" +
          " POWER CONSUMPTION -- " + "TOTAL --" + str(simulator.consumption_sens_simulator.total_consumption) + "W" +
          " MOMENTARY -- " + str(simulator.consumption_sens_simulator.momentary_consumption) + "W/s" + "\n")

simulator.stop_simulator()
