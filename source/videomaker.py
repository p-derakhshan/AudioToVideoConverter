from moviepy.editor import *
import os
import json
class VideoCreator:
    def __init__(self):
        self.images = {
            'A': 'char1.jpg', 'B': 'char4.jpg', 'C': 'char6.jpg', 'D': 'char8.jpg', 'E': 'char9.jpg',
            'F': 'char5.jpg', 'G': 'char6.jpg', 'H': 'char6.jpg', 'I': 'char1.jpg', 'J': 'char6.jpg',
            'K': 'char9.jpg', 'L': 'char8.jpg', 'M': 'char4.jpg', 'N': 'char8.jpg', 'O': 'char2.jpg', 
            'P': 'char4.jpg', 'Q': 'char3.jpg', 'R': 'char7.jpg', 'S': 'char6.jpg', 'T': 'char6.jpg',
            'U': 'char3.jpg', 'V': 'char5.jpg', 'W': 'char7.jpg', 'X': 'char6.jpg', 'Y': 'char7.jpg',
            'Z': 'char6.jpg', ' ': 'char4.jpg',}
        file_dir = os.path.normpath(os.path.dirname(os.path.realpath(__file__))+ os.sep + os.pardir+ os.sep+'sprites/')
        for key,value in self.images.items(): self.images[key]= os.path.join(file_dir, value) #.../sprites/char?
    
    def convert_phonemes(self,timestaps_path): #read .jason file and convert timestaps to sprites addresses
        json_file= open(timestaps_path, )
        data = json.load(json_file)
        timestamps = [[i["alignedWord"],i["start"],i["end"],i["phonemes"]] for i in data["words"]]
        return timestamps
    
    def word_values(self, word): #word = [word value, start, end, phonemes list]
        return word[0], (word[2]-word[1]), word[3]

    def phoneme_values(self,phoneme): #phoneme = [phoneme value, start, end]
        return phoneme[0], (phoneme[2]-phoneme[1])

    def output_path(self,file):
        i = 1
        while True:
            if os.path.exists(file+'.mp4'):
                file = '{}({})'.format(file, i)
                i+=1
            else:
                return file+'.mp4'

    def creat_video(self,audio_path, video_path, timestamps): #create the output video file
        fps=25
        texts, frames=[], []
        for word in timestamps:
            value, duration_total, phonemes = self.word_values(word)
            text = TextClip(value,color='green', font='Arial',fontsize=140).set_pos('bottom').set_duration(duration_total)
            texts.append(text)
            for phoneme in phonemes:
                vowel,duration=self.phoneme_values(phoneme)
                frame = ImageClip(self.images[vowel],duration=duration)
                frames.append(frame)
        subtitle = concatenate(texts,method='compose')
        video= concatenate(frames,method='compose')
        video = video.set_audio(AudioFileClip(audio_path))
        result = CompositeVideoClip([video,subtitle.set_pos('bottom')])
        result.write_videofile(self.output_path(video_path), audio=True,fps=fps)

'''test'''
timestamps=[
    [' ',0.0,0.27188208616780046,[[' ',0.0,0.27188208616780046]]],
    ['I',0.27188208616780046,0.43151927437641724,[['A',0.27188208616780046,0.43151927437641724]]],
    ['BEG',0.43151927437641724,0.7607709750566894,[['B',0.43151927437641724,0.6011337868480726],['E',0.6011337868480726,0.660997732426304],['G',0.660997732426304,0.7607709750566894]]],
    ['YOUR',0.7607709750566894,0.9303854875283447,[['Y',0.7607709750566894,0.8605442176870749],['O',0.8605442176870749,0.8904761904761905],['R',0.9303854875283447,0.9303854875283447]]],
    ['PARDON',0.9303854875283447,1.49,[['P',0.9303854875283447,1.05],['N',1.05,1.49]]],
    ['SP',1.49,1.62,[[' ',1.49,1.62]]],
    ['SAID',1.62,1.84,[['S',1.62,1.44],['D',1.44,1.84]]],
    ['THE',1.84,1.90,[['D',1.84,1.87],['E',1.87,1.90]]],
    ['MOUSE',1.90,2.46,[['M',1.90,2.16],['S',2.16,2.46]]],
    ['FROWNING',2.46,2.87,[['F',2.46,2.67],['G',2.46,2.67]]],
    ['BUT',2.87,3.06,[['B',2.87,2.96],['T',2.96,3.06]]],
    ['VERY',3.06,3.34,[['V',3.06,3.24],['Y',3.24,3.34]]],
    ['POLITELY',3.34,3.87,[['P',3.34,3.57],['Y',3.57,3.87]]],
    [' ',3.87,4.09,[[' ',3.87,4.09]]],
    ['DID',4.09,4.36,[['D',4.09,4.16],['Y',4.16,4.36]]],
    ['YOU',4.36,4.82,[['Y',4.36,4.50],['U',4.50,4.82]]],
    ['SPEAK',4.82,4.94,[['S',4.82,4.89],['K',4.89,4.94]]],
    [' ',4.94,5.43,[[' ',4.94,5.43]]]]