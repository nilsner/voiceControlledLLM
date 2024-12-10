import speech_recognition as sr

class SpeechToText:
    def __init__(self):
        # Initialize recognizer
        self.recognizer = sr.Recognizer()
        self.recognizer.pause_threshold = 1
        # Use the default microphone set by the OS
        self.mic = sr.Microphone()
        
        #Adjust for ambient noise
        with self.mic as source:
            #print("Adjusting for ambient noise, please wait...")
            self.recognizer.adjust_for_ambient_noise(source, duration=1)
      
    def recognize_speech(self, timeout=5, phrase_time_limit=30):
        with self.mic as source:
            print("Listening...")
            try:
                # Listen with a timeout of 4 seconds and phrase time limit of 30 seconds
                audio = self.recognizer.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)
            except sr.WaitTimeoutError:
                print("Listening timed out while waiting for speech.")
                return ""
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

#Example usage
if __name__ == "__main__":
    try:
        stt = SpeechToText()
        print("Say something:")
        command = stt.recognize_speech()
        print("Recognized:", command)
    except Exception as e:
        print(e)