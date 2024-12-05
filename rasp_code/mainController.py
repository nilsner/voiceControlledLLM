import time
from water_controller import WaterController
from speech_to_text import SpeechToText
from llmModule import LLMModule

class MainController:
    def __init__(self, ultrasonic_sensor):
        self.water_controller = WaterController()
        self.speech_to_text = SpeechToText()
        self.llm = LLMModule()
        self.ultrasonic_sensor = ultrasonic_sensor  # Simulates user detection logic
        self.listening = False

    def run(self):
        while True:
            # Continuously check for user presence
            if self.user_detected():
                print("User detected. Activating listening...")
                self.activate_listening()
            else:
                print("No user detected. Deactivating listening...")
                self.deactivate_listening()
            time.sleep(0.1)

    def user_detected(self):
        """Check if a user is within range of the ultrasonic sensor."""
        distance = self.ultrasonic_sensor.get_distance()
        return distance < self.ultrasonic_sensor.threshold  # Example threshold value

    def activate_listening(self):
        """Handle the listening and processing of user commands."""
        if not self.listening:
            self.listening = True
            print("Listening for user command...")
            command = self.speech_to_text.recognize_speech()
            self.process_command(command)
            self.listening = False

    def deactivate_listening(self):
        """Reset state when no user is detected."""
        if self.listening:
            self.listening = False

    def process_command(self, command):
        """Process the command recognized from speech."""
        print(f"Processing command: {command}")
        response = self.llm.call_gemini(command)
        
        if response["allowedWater"]:
            type_of_water = response["typeOfWater"]
            print(f"Dispensing {type_of_water} water.")
            if type_of_water == "hot":
                self.water_controller.dispense_hot_water()
            elif type_of_water == "cold":
                self.water_controller.dispense_cold_water()
        else:
            reason = response["answer"]
            print(f"Cannot dispense water. Reason: {reason}")

# Example UltrasonicSensor class for testing
class UltrasonicSensor:
    def __init__(self, threshold=50):
        self.threshold = threshold  # Example threshold in cm

    def get_distance(self):
        """Simulate getting the distance from the sensor."""
        # Replace with actual sensor reading logic
        return 30  # Simulating a user in range

if __name__ == "__main__":
    sensor = UltrasonicSensor()
    controller = MainController(sensor)

    try:
        controller.run()
    except KeyboardInterrupt:
        print("Program stopped by user.")