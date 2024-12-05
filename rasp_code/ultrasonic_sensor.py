import RPi.GPIO as GPIO
import time

class UltrasonicSensor:
    def __init__(self, trig_pin=17, echo_pin=18, distance_threshold=50):
        """
        Initialize the ultrasonic sensor.
        :param trig_pin: GPIO pin connected to TRIG
        :param echo_pin: GPIO pin connected to ECHO
        :param distance_threshold: Distance in cm to trigger detection
        """
        self.trig_pin = trig_pin
        self.echo_pin = echo_pin
        self.distance_threshold = distance_threshold

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.trig_pin, GPIO.OUT)
        GPIO.setup(self.echo_pin, GPIO.IN)

    def measure_distance(self):
        """
        Measure the distance using the ultrasonic sensor.
        :return: Distance in cm
        """
        # Trigger the ultrasonic pulse
        GPIO.output(self.trig_pin, True)
        time.sleep(0.00001)  # 10 microseconds
        GPIO.output(self.trig_pin, False)

        # Wait for the echo
        start_time = time.time()
        while GPIO.input(self.echo_pin) == 0:
            start_time = time.time()

        while GPIO.input(self.echo_pin) == 1:
            stop_time = time.time()

        # Calculate the time difference and convert to distance
        time_elapsed = stop_time - start_time
        distance = (time_elapsed * 34300) / 2  # Speed of sound is 343 m/s
        return distance

    def detect_presence(self):
        """
        Check if an object/person is within the distance threshold.
        :return: True if within threshold, False otherwise
        """
        distance = self.measure_distance()
        print(f"Measured distance: {distance:.2f} cm")
        return distance < self.distance_threshold