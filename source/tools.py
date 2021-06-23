import os
from pydub import AudioSegment

class Tools:
    def annotation_remover(self, script_file, output_dir):
        
        with open(script_file, "r") as input:
            with open(output_dir, "w") as output:
                for line in input:
                    if "ROW" in line:
                        line = line.translate({ord(i): None for i in "!?.,:)|(;#%^*-_=+][}{\/"})
                        line = line.replace('@', 'atsign')
                        line = line.replace('$', 'dollar')
                        line = line.replace('&', 'and')
                        output.write(line) 

    def get_wav_file(self, audio_dir, files_dir):
        input_dir, audio = os.path.split(audio_dir)
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
    
