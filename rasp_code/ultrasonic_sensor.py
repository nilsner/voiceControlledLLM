from grove.grove_ultrasonic_ranger import GroveUltrasonicRanger

class UltrasonicSensor:
    def __init__(self, port):
        self.sensor = GroveUltrasonicRanger(port)

    def measure_distance(self):
        try:
            distance = self.sensor.get_distance()
            return distance
        except Exception as e:
            raise Exception(f"Error communicating with sensor: {e}")