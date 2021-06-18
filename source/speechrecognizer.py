#from deepspeech import Model
import numpy as np
import wave
from pydub import AudioSegment
import os

class SpeechRecognition:
    def __init__(self,model):
        self.model = model

    def convert_speech_to_text(self,audio_path,text_path):
        self.files='./files'
        self.file_path, self.file_name = os.path.split(audio_path)
        result = self.transcribe(self.tuning(self.get_wav_file()))
        text_file = open(text_path, 'w+')
        text_file.write(result)
        text_file.close()

    def get_wav_file(self):
        file_name = '/{}.wav'.format(os.path.splitext(self.file_name)[0])
        file = self.file_path+file_name
        if not self.file_name.endswith('.wav'):
            new_file= self.files+file_name
            AudioSegment.from_file(file).export(new_file,format='wav')
            file = new_file
        return file
        #if filename.endswith('.mp3') or filename.endswith('.flac'):

    def tuning(self,file_wav):
        wav_file = AudioSegment.from_file(file=file_wav)
        wav_file = wav_file.set_frame_rate(16000)
        wav_file = wav_file.set_channels(1)
        out_file = '{}16khz(1).wav'.format(os.path.splitext(file_wav)[0])
        wav_file.export(out_f=out_file,format='wav')
        return out_file

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


