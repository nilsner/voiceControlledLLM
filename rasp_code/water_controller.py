import threading
import time
from grove.grove_servo import GroveServo  # Import the Grove Servo library

class WaterController:
    def __init__(self, servo_pin):
        self.is_dispensing = False
        self.dispense_start_time = 0
        self.dispense_timer = None
        self.servo = GroveServo(servo_pin)  # Initialize the servo on the specified pin

    def dispense_hot_water(self, waterAmount):
        """Dispense hot water."""
        self._start_dispensing("hot", waterAmount)

    def dispense_cold_water(self, waterAmount):
        """Dispense cold water."""
        self._start_dispensing("cold", waterAmount)

    def stop_dispensing(self):
        """Stop dispensing water."""
        if self.is_dispensing:
            #print("Simulating: Stopped dispensing.")
            self.is_dispensing = False

            # Cancel the timer if it's still active
            if self.dispense_timer is not None:
                self.dispense_timer.cancel()
                self.dispense_timer = None

            # Move the servo back to its initial position
            #print("Simulating: Moving servo back to 0 degrees.")
            self.servo.setAngle(0)  # Reset the servo to its initial position

    def _start_dispensing(self, water_type, waterAmount):
        """Start dispensing the specified water type."""
        """  if self.is_dispensing:
            print(f"Already dispensing {water_type} water.")
            return
            """
        print("wateramount:", waterAmount)
        dispenseDuration = int(waterAmount/25)
        print("dispenseDuration: ", dispenseDuration)

        self.is_dispensing = True
        self.dispense_start_time = time.time()

        # Move the servo to 10 degrees to start the "dispensing" process
        #print("Simulating: Moving servo to 90 degrees.")
        self.servo.setAngle(24)
        #print(f"Simulating: Dispensing {water_type} water...")
        # Start a timer to move back after dispenseDuration(seconds)
        time.sleep(dispenseDuration)
        self._reset_servo() 
        
        #threading.Timer(dispenseDuration, self._reset_servo).start()

        # Start a failsafe timer to stop dispensing after 25 seconds
        # self.dispense_timer = threading.Timer(25, self.stop_dispensing)
        # self.dispense_timer.start()

    def _reset_servo(self):
        """Move the servo back to its initial position after 6 seconds."""
        #print("Simulating: Moving servo back to 0 degrees after 6 seconds.")
        self.servo.setAngle(0)

# Example usage
if __name__ == "__main__":
    # Specify the pin connected to the servo
    servo_pin = 5  # Replace with the actual pin number
    controller = WaterController(servo_pin)

    # Simulate dispensing hot and cold water
    controller.dispense_hot_water(200)
    time.sleep(5)  # Wait to observe the dispensing process
    controller._reset_servo()