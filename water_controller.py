import threading
import time

class WaterController:
    def __init__(self):
        self.is_dispensing = False
        self.dispense_start_time = 0
        self.dispense_timer = None

    def dispense_hot_water(self):
        """Dispense hot water."""
        self._start_dispensing("hot")

    def dispense_cold_water(self):
        """Dispense cold water."""
        self._start_dispensing("cold")

    def stop_dispensing(self):
        """Stop dispensing water."""
        if self.is_dispensing:
            print("Simulating: Stopped dispensing.")
            self.is_dispensing = False

            # Cancel the timer if it's still active
            if self.dispense_timer is not None:
                self.dispense_timer.cancel()
                self.dispense_timer = None

    def _start_dispensing(self, water_type):
        """Start dispensing the specified water type."""
        if self.is_dispensing:
            print(f"Already dispensing {water_type} water.")
            return

        print(f"Simulating: Dispensing {water_type} water...")
        self.is_dispensing = True
        self.dispense_start_time = time.time()

        # Start a timer to stop dispensing after 7 seconds (failsafe)
        self.dispense_timer = threading.Timer(7, self.stop_dispensing)
        self.dispense_timer.start()