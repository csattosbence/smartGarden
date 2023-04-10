from model.sensordata import SensorData
from simulator import main

sim = main.simulator


def run_all_simulator():
    sim.run_all_simulator()

def stop_all_simulator():
    sim.stop_all_simulator()


def get_data():
    sensor_data = SensorData()

    sensor_data.currentDate = str(sim.get_time())
    sensor_data.light = str(round(sim.get_light(), 2))
    sensor_data.humidity = str(round(sim.get_humidity(), 2))
    sensor_data.temperature = str(round(sim.get_temp(), 2))
    sensor_data.totalConsumption = str(round(sim.get_total_consumption(), 2))
    sensor_data.momentaryConsumption = str(round(sim.get_momentary_consumption(), 2))
    sensor_data.soilMoisture = str(round(sim.get_soil_moisture(), 2))

    sensor_data.heaterStatus = str(sim.get_heater_satus())
    sensor_data.lightStatus = str(sim.get_light_satus())
    sensor_data.waterSysStatus = str(sim.get_water_sys_status())
    sensor_data.humidifierStatus = str(sim.get_humidifier_status())

    return sensor_data


def turn_on_heater():
    sim.turn_on_heater()
    return True


def turn_off_heater():
    sim.turn_off_heater()
    return True


def turn_on_watering_system():
    sim.turn_on_watering_system()
    return True


def turn_off_watering_system():
    sim.turn_off_watering_system()
    return True


def turn_on_humidifier():
    sim.turn_on_humidifier()
    return True


def turn_off_humidifier():
    sim.turn_off_humidifier()
    return True


def turn_on_light():
    sim.turn_on_light()
    return True


def turn_off_light():
    sim.turn_off_light()
    return True


def set_ticker_speed(ticker_speed):
    sim.set_ticker_speed(ticker_speed)
    return True


def set_sim_date(sim_date):
    sim.set_sim_date(sim_date)
    return True


def resume_ticker():
    sim.resume_ticker()
    return True


def stop_ticker():
    sim.stop_ticker()
    return True


def set_light(light):
    sim.set_light(light)
    return True