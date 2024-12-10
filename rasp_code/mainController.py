import time
from water_controller import WaterController
from speech_to_text import SpeechToText
from llmModule import LLMModule
from ultrasonic_sensor import UltrasonicSensor
from text_to_speech import TextToSpeech
servo_pin = 5
ultrasonic_pin = 16

class BackupController:
    def __init__(self):
        self.water_controller = WaterController(servo_pin)
        self.water_controller._reset_servo()
        self.speech_to_text = SpeechToText()
        self.llm = LLMModule()
        self.tts = TextToSpeech()
        print('initialized')
    
    def exit(self):
        print('Resetting servo')
        self.water_controller._reset_servo()

    def run(self):
        self.tts.speak("Hello, what do you want?")
        time.sleep(2)
        command = self.speech_to_text.recognize_speech()

        self.process_command(command)
        """  if not should_continue:
            self.working = False
        time.sleep(10) """

    def process_command(self, command):
        #Process user commands and return False if program should stop.
        """        if self.water_controller.is_dispensing:
            if "stop" in command or "cancel" in command:
                self.water_controller.stop_dispensing()
                return False
            print("Currently dispensing. Say 'stop' or 'cancel' to stop.")
        """
        # Handle commands when not dispensing
        response = self.llm.call_gemini(command)
        
        if response["niceUserRequest"]:
            type = response["typeOfWater"]
            #print(f"{type}")
            if "hot" in type:
                self.tts.speak(response["answer"])
                self.water_controller.dispense_hot_water(response["waterAmount"])
                #time.sleep(2)
                #self.tts.speak(response["finalResponse"])
            elif "cold" in type:
                self.tts.speak(response["answer"])
                self.water_controller.dispense_cold_water(response["waterAmount"])
                #time.sleep(2)
                #self.tts.speak(response["finalResponse"])
            elif "none" in type:
                self.tts.speak(response["answer"])
            else:
                self.tts.speak("Unknown command. Please specify if its either 'hot water' or 'cold water'.")
        else:
            reason = response["answer"]
            self.tts.speak(reason)
        return True
 
if __name__ == "__main__":
    controller = BackupController()
    ultrasonic_sensor = UltrasonicSensor(port=ultrasonic_pin) 
    looping = True
    while looping:
        try:
            distance = ultrasonic_sensor.measure_distance()
            print(f"Measured Distance: {distance} cm")
            if distance < 50:
                controller.run()
            else:
                print("Distance is greater than or equal to 50 cm. Idling...")
            time.sleep(5)
        except KeyboardInterrupt:
            print("Program interrupted. Exiting.")
            looping = False
            controller.exit()
            break