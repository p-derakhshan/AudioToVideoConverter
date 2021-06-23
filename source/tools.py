import os, pyfoal
from pydub import AudioSegment

class Tools:
    def remove_annotations(self, script_file, output_dir):
        with open(script_file, "r") as input:
            with open(output_dir, "w") as output:
                for line in input:
                    if "ROW" in line:
                        line = line.translate({ord(i): None for i in "!?.,:)|(;#%^*-_=+][}{\/"})
                        line = line.replace('@', 'atsign')
                        line = line.replace('$', 'dollar')
                        line = line.replace('&', 'and')
                        output.write(line) 

    def get_wav_file(self, audio, name, files_dir):
        if not audio.endswith('.wav'):
            new_file= files_dir+name+'.wav'
            AudioSegment.from_file(audio).export(new_file,format='wav')
            audio= new_file
        return audio

    def tune_audio(self,file_wav):
        wav_file = AudioSegment.from_file(file=file_wav)
        wav_file = wav_file.set_frame_rate(16000)
        wav_file = wav_file.set_channels(1)
        out_file = '{}16khz(1).wav'.format(os.path.splitext(file_wav)[0])
        wav_file.export(out_f=out_file,format='wav')
        return out_file
    
    def align_phonemes(self, audio_dir, script_dir, output_dir ):
        pyfoal.from_file_to_file(audio_dir, output_dir, output_dir) 
