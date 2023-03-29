from simulator import main

sim = main.simulator


def run_simulator():
    sim.run_simulator()


def get_temp():
    return sim.get_temp()


def get_data():
    return [
        sim.get_temp(),
        sim.get_humidity(),
        sim.get_time(),
        sim.get_total_consumption(),
        sim.get_momentary_consumption()
    ]
