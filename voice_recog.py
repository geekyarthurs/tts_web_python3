from gtts import gTTS
import os
import random,string

class TTS:

    def randomString(self, stringLength=10):
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for i in range(stringLength))

    def __init__(self, msg, slow=False, language='en'):
        self.msg = msg
        self.language = language
        self.speed = slow
        self.audioObj = gTTS(
            text=self.msg, lang=self.language, slow=self.speed)

    def sendAudio(self):
        self.path = "audios/" + self.randomString(10) + ".mp3"
        self.audioObj.save(self.path)
        return self.path
    





