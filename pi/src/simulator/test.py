import random


class SoilPHSensor:
    def __init__(self, min_ph=4.0, max_ph=9.0):
        self.min_ph = min_ph
        self.max_ph = max_ph

    def get_ph(self):
        # simulate sensor reading with random value within range
        return round(random.uniform(self.min_ph, self.max_ph), 2)


# # Example usage
# sensor = SoilPHSensor()
# for i in range(10):
#     ph = sensor.get_ph()
#     print(f"Soil pH: {ph}")