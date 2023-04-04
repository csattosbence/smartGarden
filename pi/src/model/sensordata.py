from datetime import datetime
class SensorData:
    def __init__(self):
        self.temperature = 0
        self.humidity = 0
        self.totalConsumption = 0
        self.momentaryConsumption = 0
        self.currentDate = datetime.now()
        self.light = 0
        self.soilMoisture = 0

