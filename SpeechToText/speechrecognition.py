from deepspeech import Model
import numpy as np
import wave
from pydub import AudioSegment
import os
class speechrecognition:

    def __init__(self,model_file_path,lm_file_path,beam_width,lm_alpha,lm_beta,file_location):
        #self.filename=filename
        self.model_file_path=model_file_path
        self.lm_file_path=lm_file_path
        self.beam_width=beam_width
        self.lm_alpha=lm_alpha
        self.lm_beta=lm_beta
        self.file_location=file_location

    # set the features of training Model
    def set_model(self):
        model = Model(self.model_file_path)
        model.enableExternalScorer(self.lm_file_path)
        model.setScorerAlphaBeta(self.lm_alpha, self.lm_beta)
        model.setBeamWidth(self.beam_width)
        return model
    # read the wav file
    def read_wav_file(self,filename):
        with wave.open(filename, 'rb') as w:
            rate = w.getframerate()
            frames = w.getnframes()
            buffer = w.readframes(frames)
         # print(rate)
         # print(frames)
        return buffer, rate

    def transcribe(self,wav_filename):
        model=self.set_model()
        buffer, rate = self.read_wav_file(wav_filename)
        data16 = np.frombuffer(buffer, dtype=np.int16)
        return model.stt(data16)

    def tuning(self,wav_filename):
        wav_file = AudioSegment.from_file(file=wav_filename)
        wav_file = wav_file.set_frame_rate(16000)
        wav_file = wav_file.set_channels(1)
        out_file = os.path.splitext(wav_filename)[0] + "16khz(1)" + ".wav"
        wav_file.export(out_f=out_file,format="wav")
        return out_file

    def makewav(self ,filename,right_ff,location):

            if filename.endswith(".mp3") or filename.endswith(".flac"):
                wav_filename =  right_ff+'/'+os.path.splitext(filename)[0] + ".wav"
            AudioSegment.from_file(location+'/'+filename).export(wav_filename,format="wav")
            return wav_filename

    def convert_speech_to_text(self , filename):
        wav_filename=self.makewav(filename,'audio files/wav_format',self.file_location)
        return self.transcribe(self.tuning(wav_filename))

