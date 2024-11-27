import speech_recognition as sr
import pyaudio

class SpeechToText:
    # def __init__(self):
    #     # Initialize recognizer once
    #     self.recognizer = sr.Recognizer()
        
    #     # Find Grove microphone
    #     p = pyaudio.PyAudio()
    #     device_index = None
        
    #     # List and find Grove mic device
    #     for i in range(p.get_device_count()):
    #         info = p.get_device_info_by_index(i)
    #         if "USB" in info["name"]:  # Grove mic usually shows as USB device
    #             device_index = i
    #             break
    #     p.terminate()
        
    #     if device_index is None:
    #         raise Exception("Grove microphone not found")
            
    #     # Store mic device
    #     self.mic = sr.Microphone(device_index=device_index)
        
    #     # Adjust for ambient noise
    #     with self.mic as source:
    #         print("Adjusting for ambient noise...")
      
    def recognize_speech(self):
        """Recognize speech using Google Speech Recognition."""
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio).lower()
            print("You said:", command)
            return command
        except sr.UnknownValueError:
            print("Sorry, I did not understand.")
            return ""
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service: {e}")
            return ""