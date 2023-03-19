from datetime import datetime
import math
import threading
import time


class TempSimulator:
    const = 18
    step = 360 / 86400
    step_counter = 0
    current_temp = 0

    def run(self):
        t1 = threading.Thread(target=self.simulate_temp())
        t1.start()
        t1.join()

    def simulate_temp(self):
        f_second = 0
        f_last_inc = time.time()
        while True:
            if time.time() >= f_last_inc + 1:
                f_second += 1
                f_last_inc = time.time()
                self.step_counter = + self.step_counter + self.step
                self.current_temp = -0.5 * math.sin(self.step_counter) + self.const

    def increase_temp(self, amount):
        self.const = self.const + float(amount)

    def decrease_temp(self, amount):
        self.const = self.const - amount


class TimeSimulator:
    simulated_time = 0
    last_inc = time.time()

    def __init__(self, date: datetime = datetime.now()):
        self.simulated_time = int(date.timestamp())

    def simulate_time(self):
        while True:
            if time.time() >= self.last_inc + 1:
                self.simulated_time += 1
                self.last_inc = time.time()

    def run(self):
        thread = threading.Thread(target=self.simulate_time)
        thread.start()
        thread.join()

    def set_date(self, date: datetime):
        self.unix_timestamp = int(date.timestamp())


class HeaterSimulator:
    heatCounter = 0

    def __init__(self, temp_simulator: TempSimulator):
        self.temp_simulator = temp_simulator

    def simulate_heater(self):
        f_second = 0
        f_last_inc = time.time()
        while True:
            if time.time() >= f_last_inc + 1:
                f_second += 1
                f_last_inc = time.time()
                self.heatCounter = self.heatCounter + 0.03

    def run(self):
        thread = threading.Thread(target=self.simulate_heater())
        thread.start()
        thread.join()


class Simulator:

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
        return self.temp_simulator.current_temp










# tempSimulator = TempSimulator()
# heaterSimulator = HeaterSimulator(tempSimulator)
# t1 = threading.Thread(target=tempSimulator.simulate_temp)
# t2 = threading.Thread(target=heaterSimulator.simulate_heater)
# t1.start()
# t2.start()
#
# while True:
#     time.sleep(1)
#     main_temp = tempSimulator.current_temp + heaterSimulator.heatCounter
#     print(' Current temp: ' + str(main_temp))
# def control_temperature(min_t, max_t, temp, heater, is_automatic):
#     if is_automatic:
#         if temp < min_t:
#             heater = True
#
#         if heater:
#             temp = temp + 0.08
#             if temp > max_t:
#                 heater = False
#         else:
#             temp = temp - 0.02

# f_min_temp = 20
# f_ideal_temp = 23
# f_max_temp = 25
# f_heater = True
# f_is_automatic = True

# f_second = 0
# f_last_inc = time.time()
#
#
# while True:
#     if time.time() >= f_last_inc + 1:
#         f_second += 1
#         f_last_inc = time.time()
#         print(f_second)
def run_simulator():
    return None