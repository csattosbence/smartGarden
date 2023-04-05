from datetime import datetime
import threading

from simulator.consumptionsensorsim import ConsumptionSensorSimulator
from simulator.heatersim import HeaterSimulator
from simulator.humidifier import HumidifierSimulator
from simulator.lightsensorsim import LightSensorSimulator
from simulator.lightsim import LightSimulator
from simulator.soilmoisturesensorsim import SoilMoistureSensorSimulator
from simulator.tempsim import TempSimulator
from simulator.timesim import TimeSimulator
from simulator.humiditysensorsim import HumiditySensorSimulator
from simulator.watersystemsim import WateringSystemSimulator


class Simulator:
    simulator_active = False

    time_simulator = TimeSimulator()
    temp_simulator = TempSimulator(time_simulator)
    heater_simulator = HeaterSimulator(temp_simulator, time_simulator)
    humidity_sens_simulator = HumiditySensorSimulator(time_simulator)
    light_sens_simulator = LightSensorSimulator(time_simulator)
    soil_moist_sens_simulator = SoilMoistureSensorSimulator(time_simulator)
    watering_system_simulator = WateringSystemSimulator(time_simulator,soil_moist_sens_simulator)
    consumption_sens_simulator = ConsumptionSensorSimulator(time_simulator,
                                                            heater_simulator,
                                                            temp_simulator,
                                                            humidity_sens_simulator)

    light_simulator = LightSimulator(time_simulator, light_sens_simulator)
    humidifier_simulator = HumidifierSimulator(time_simulator, humidity_sens_simulator)

    time_thread = None
    heater_thread = None
    temp_thread = None
    humidity_sens_thread = None
    humidifier_thread = None
    light_sens_thread = None
    light_thread = None
    soil_moist_thread = None
    watering_system_thread = None
    consumption_thread = None

    def run_all_simulator(self):
        if not self.simulator_active:

            self.time_simulator.start_simulator()
            self.temp_simulator.start_simulator()
            self.heater_simulator.start_simulator()
            self.humidity_sens_simulator.start_simulator()
            self.humidifier_simulator.start_simulator()
            self.soil_moist_sens_simulator.start_simulator()
            self.watering_system_simulator.start_simulator()
            self.light_sens_simulator.start_simulator()
            self.light_simulator.start_simulator()
            self.consumption_sens_simulator.start_simulator()

            self.time_thread = threading.Thread(target=self.time_simulator.simulate_time)
            self.heater_thread = threading.Thread(target=self.heater_simulator.simulate_heater)
            self.temp_thread = threading.Thread(target=self.temp_simulator.simulate_temp)
            self.humidity_sens_thread = threading.Thread(target=self.humidity_sens_simulator.simulate_humidity)
            self.humidifier_thread = threading.Thread(target=self.humidifier_simulator.simulate_humidifier)
            self.light_sens_thread = threading.Thread(target=self.light_sens_simulator.simulate_light)
            self.light_thread = threading.Thread(target=self.light_simulator.simulate_light_system)
            self.soil_moist_thread = threading.Thread(target=self.soil_moist_sens_simulator.simulate_soil_moisture)
            self.watering_system_thread = threading.Thread(target=self.watering_system_simulator.simulate_watering_system)
            self.consumption_thread = threading.Thread(target=self.consumption_sens_simulator.simulate_consumption)

            self.time_thread.start()
            self.heater_thread.start()
            self.temp_thread.start()
            self.humidity_sens_thread.start()
            self.humidifier_thread.start()
            self.light_sens_thread.start()
            self.light_thread.start()
            self.soil_moist_thread.start()
            self.watering_system_thread.start()
            self.consumption_thread.start()

            self.simulator_active = True

            return True
        else:
            return False

    def stop_all_simulator(self):
        if self.simulator_active:

            self.time_simulator.stop_simulator()
            self.temp_simulator.stop_simulator()
            self.heater_simulator.stop_simulator()
            self.humidity_sens_simulator.stop_simulator()
            self.humidifier_simulator.stop_simulator()
            self.soil_moist_sens_simulator.stop_simulator()
            self.watering_system_simulator.stop_simulator()
            self.light_sens_simulator.stop_simulator()
            self.light_simulator.stop_simulator()
            self.consumption_sens_simulator.stop_simulator()

            self.heater_thread.join()
            self.temp_thread.join()
            self.humidity_sens_thread.join()
            self.humidifier_thread.join()
            self.light_sens_thread.join()
            self.light_thread.join()
            self.soil_moist_thread.join()
            self.watering_system_thread.join()
            self.consumption_thread.join()

            self.simulator_active = False

            return True
        else:
            return False

    def get_temp(self):
        return self.temp_simulator.current_temp

    def get_humidity(self):
        return self.humidity_sens_simulator.current_humidity

    def get_momentary_consumption(self):
        return self.consumption_sens_simulator.momentary_consumption

    def get_total_consumption(self):
        return self.consumption_sens_simulator.total_consumption

    def get_time(self):
        return datetime.fromtimestamp(self.time_simulator.simulated_time)

    def get_light(self):
        return self.light_sens_simulator.current_light

    def get_soil_moisture(self):
        return self.soil_moist_sens_simulator.current_soil_moisture

    def turn_on_heater(self):
        self.heater_simulator.turn_on_system()
        return True

    def turn_off_heater(self):
        self.heater_simulator.turn_off_system()
        return True

    def turn_on_watering_system(self):
        self.watering_system_simulator.turn_on_system()
        return True

    def turn_off_watering_system(self):
        self.watering_system_simulator.turn_off_system()
        return True

    def turn_on_humidifier(self):
        self.humidifier_simulator.turn_on_system()
        return True

    def turn_off_humidifier(self):
        self.humidifier_simulator.turn_off_system()
        return True

    def turn_on_light(self):
        self.light_simulator.turn_on_system()
        return True

    def turn_off_light(self):
        self.light_simulator.turn_off_system()
        return True

    def set_ticker_speed(self, ticker_speed):
        self.time_simulator.ticker_speed = ticker_speed
        return True








simulator = Simulator()

# simulator.run_all_simulator()
#
# run_time = datetime.now().timestamp() + 5
#
# # while datetime.now().timestamp() < run_time:
# #     print(" DATE -- " + str(datetime.fromtimestamp(simulator.time_simulator.simulated_time)) + "\n" +
# #           " CURRENT TEMP -- " + str(simulator.temp_simulator.current_temp) + "\n" +
# #           " CURRENT HUMIDITY -- " + str(simulator.humidity_sens_simulator.current_humidity) + "\n" +
# #           " POWER CONSUMPTION -- " + "TOTAL --" + str(simulator.consumption_sens_simulator.total_consumption) + "W" +
# #           " MOMENTARY -- " + str(simulator.consumption_sens_simulator.momentary_consumption) + "W/s" + "\n" +
# #           "LIGHT -- " + str(simulator.light_sens_simulator.current_light) + "LUX" + "\n")
# #
# # run_time = datetime.now().timestamp() + 5
#
# simulator.heater_simulator.is_heater_on = False
#
# while datetime.now().timestamp() < run_time:
#     print(" DATE -- " + str(datetime.fromtimestamp(simulator.time_simulator.simulated_time)) + "\n" +
#           " CURRENT TEMP -- " + str(simulator.temp_simulator.current_temp) + "\n" +
#           " CURRENT HUMIDITY -- " + str(simulator.humidity_sens_simulator.current_humidity) + "\n" +
#           " POWER CONSUMPTION -- " + "TOTAL --" + str(simulator.consumption_sens_simulator.total_consumption) + "W" +
#           " MOMENTARY -- " + str(simulator.consumption_sens_simulator.momentary_consumption) + "W/s" + "\n" +
#           "LIGHT -- " + str(simulator.light_sens_simulator.current_light) + "LUX" + "\n" +
#           "SOIL MOISTURE -- " + str(simulator.soil_moist_sens_simulator.current_soil_moisture) + " % " + "\n")
#
# run_time = datetime.now().timestamp() + 5
#
# simulator.watering_system_simulator.turn_on_system()
#
#
#
# while datetime.now().timestamp() < run_time:
#     print(" DATE -- " + str(datetime.fromtimestamp(simulator.time_simulator.simulated_time)) + "\n" +
#           " CURRENT TEMP -- " + str(simulator.temp_simulator.current_temp) + "\n" +
#           " CURRENT HUMIDITY -- " + str(simulator.humidity_sens_simulator.current_humidity) + "\n" +
#           " POWER CONSUMPTION -- " + "TOTAL --" + str(simulator.consumption_sens_simulator.total_consumption) + "W" +
#           " MOMENTARY -- " + str(simulator.consumption_sens_simulator.momentary_consumption) + "W/s" + "\n" +
#           "LIGHT -- " + str(simulator.light_sens_simulator.current_light) + "LUX" + "\n" +
#           "SOIL MOISTURE -- " + str(simulator.soil_moist_sens_simulator.current_soil_moisture) + " % " + "\n")
#
# simulator.stop_all_simulator()
