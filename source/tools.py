import os, pyfoal
from pydub import AudioSegment

class Tools:
    def remove_annotations(self, script_file, output_dir):
        file_in = open(script_file, 'r')
        file_out = open(output_dir, 'w')
        for line in file_in:
            line = line.translate({ord(i): None for i in "!?.,:)|(;#%^*-_=+][}{\/"})
            line = line.replace('@', 'atsign')
            line = line.replace('$', 'dollar')
            line = line.replace('&', 'and')
            file_out.write(line) 
        file_in.close
        file_out.close

    def get_wav_file(self, audio, name, files_dir):
        if not audio.endswith('.wav'):
            new_file= files_dir+name+'.wav'
            AudioSegment.from_file(audio).export(new_file,format='wav')
            audio= new_file
        return audio

    def tune_audio(self,file_wav,files_dir):
        wav_file = AudioSegment.from_file(file=file_wav)
        wav_file = wav_file.set_frame_rate(16000)
        wav_file = wav_file.set_channels(1)
        out_file = '{}_16khz.wav'.format(os.path.splitext(files_dir)[0])
        wav_file.export(out_f=out_file,format='wav')
        return out_file
    
    def align_phonemes(self, audio_dir, script_dir, timestamps_dir):
        pyfoal.from_file_to_file(script_dir, audio_dir, timestamps_dir) 
