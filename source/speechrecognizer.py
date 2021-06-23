#from deepspeech import Model
import numpy as np
import wave, os, pyfoal
from pydub import AudioSegment


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

class forcedAlignment:
    def phoneme_alignments(self, audio_dir, text_dir, output_dir ):
        phoneme_alignments = pyfoal.from_file_to_file(audio_dir, text_dir, output_dir)        


