import time
from water_controller import WaterController
from speech_to_text import SpeechToText
from llmModule import LLMModule

class MainController:
    def __init__(self):
        self.water_controller = WaterController()
        self.speech_to_text = SpeechToText()
        self.llm = LLMModule()

    def run(self):
        self.working = True
        while self.working:
            # command = self.speech_to_text.recognize_speech()
            command = "Could i have a soda"
            should_continue = self.process_command(command)
            if not should_continue:
                self.working = False
            time.sleep(10)

    def process_command(self, command):
        """Process user commands and return False if program should stop."""
        if self.water_controller.is_dispensing:
            if "stop" in command or "cancel" in command:
                self.water_controller.stop_dispensing()
                return False
            print("Currently dispensing. Say 'stop' or 'cancel' to stop.")

        # Handle commands when not dispensing
        response = self.llm.call_gemini(command)
        
        if response["allowedWater"]:
            type = response["typeOfWater"]
            #print(f"{type}")
            if "hot" in type:
                self.water_controller.dispense_hot_water()
            elif "cold" in type:
                self.water_controller.dispense_cold_water()
            else:
                print("Unknown command. Please say 'hot water' or 'cold water'.")
        else:
            reason = response["answer"]
            print(f"{reason}")
        return True

if __name__ == "__main__":
    controller = MainController()
    def wait_for_enter():
        input("Press Enter to start/stop...")

    while True:
        wait_for_enter()
        try:
            controller.run()
        except KeyboardInterrupt:
            continue