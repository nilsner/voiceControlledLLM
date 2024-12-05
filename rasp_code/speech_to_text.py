import speech_recognition as sr
import pyaudio


class SpeechToText:
    def __init__(self, device_index=None):
        """
        Initialize the recognizer and microphone.
        If no device_index is provided, it tries to automatically find the Grove microphone.
        """
        self.recognizer = sr.Recognizer()
        
        if device_index is None:
            # Attempt to find the Grove USB microphone automatically
            print("Searching for Grove USB microphone...")
            p = pyaudio.PyAudio()
            for i in range(p.get_device_count()):
                info = p.get_device_info_by_index(i)
                if "USB" in info["name"]:  # Grove mic is usually a USB device
                    device_index = i
                    print(f"Found Grove microphone at device index {device_index}.")
                    break
            p.terminate()
            
            if device_index is None:
                raise Exception("Grove microphone not found. Please specify the device index manually.")
        
        self.device_index = device_index
        self.mic = sr.Microphone(device_index=self.device_index)
        
        # Adjust for ambient noise
        print("Adjusting for ambient noise... Please wait.")
        with self.mic as source:
            self.recognizer.adjust_for_ambient_noise(source)
        print("Ambient noise adjustment complete.")

    def recognize_speech(self):
        """Recognize speech using Google Speech Recognition."""
        print("Listening for speech...")
        with self.mic as source:
            audio = self.recognizer.listen(source)
        try:
            command = self.recognizer.recognize_google(audio).lower()
            print("You said:", command)
            return command
        except sr.UnknownValueError:
            print("Sorry, I did not understand.")
            return ""
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service: {e}")
            return ""


# Example usage
if __name__ == "__main__":
    try:
        # Initialize with automatic device discovery (or specify the device index manually)
        stt = SpeechToText()  # Replace with SpeechToText(device_index=2) to set manually
        
        # Start listening
        while True:
            command = stt.recognize_speech()
            if command:
                print(f"Recognized command: {command}")
                if "stop" in command:  # Example to break the loop
                    print("Stopping...")
                    break
    except Exception as e:
        print(f"Error: {e}")