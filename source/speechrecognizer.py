import numpy as np
import wave, os
class SpeechRecognition:
    def __init__(self,model):
        self.model = model

    def convert_speech_to_text(self,audio_dir,script_dir):
        result = self.transcribe(audio_dir)
        text_file = open(script_dir, 'w+')
        text_file.write(result)
        text_file.close()

    def transcribe(self,file_wav):
        buffer, rate = self.read_wav_file(file_wav)
        data16 = np.frombuffer(buffer, dtype=np.int16)
        return self.model.stt(data16)
        
    # read the wav file
    def read_wav_file(self,file):
        with wave.open(file, 'rb') as w:
            rate = w.getframerate()
            frames = w.getnframes()
            buffer = w.readframes(frames)
        return buffer, rate
