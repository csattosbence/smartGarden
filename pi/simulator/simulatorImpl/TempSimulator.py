import math
import threading
import time


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