# Install first: pip install python-espeak
import os
from espeak import espeak

class TextToSpeech:
    def __init__(self):
        os.system('amixer cset numid=3 1')
        
        # Configure for Grove speaker
        espeak.set_parameter(espeak.Parameter.Rate, 150)
        espeak.set_parameter(espeak.Parameter.Volume, 100)

        espeak.set_parameter(espeak.Parameter.Output, espeak.AUDIO_OUTPUT_PLAYBACK)
        
    def speak(self, text):
        espeak.synth(text)
        espeak.sync()
# sudo apt-get install -y python3-dev libasound2-dev
# Test speaker
# speaker-test -t wav -c 2