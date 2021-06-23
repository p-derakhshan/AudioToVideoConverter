from moviepy.editor import *
import os
import json
class VideoCreator:
    def __init__(self):
        self.images = {"AA0": "char3.jpg", "AA1": "char3.jpg", "AA2": "char3.jpg",
                        "AE0":"char1.jpg", "AE1": "char1.jpg", "AE2": "char1.jpg",
                        "AH0": "char3.jpg", "AH1": "char3.jpg", "AH2": "char3.jpg",
                        "AO0": "char6.jpg", "AO1": "char6.jpg", "AO2": "char6.jpg",
                        "AW0": "char3.jpg", "AW1": "char3.jpg", "AW2": "char3.jpg",
                        "AY0": "char3.jpg", "AY1": "char3.jpg", "AY2": "char3.jpg",
                        "B": "char7.jpg", "CH": "char8.jpg", "D": "char9.jpg", "DH": "char10.jpg",
                        "EH0": "char4.jpg", "EH1": "char4.jpg", "EH2": "char4.jpg",
                        "ER0": "char2.jpg", "ER1": "char2.jpg", "ER2": "char2.jpg",
                        "EY0": "char1.jpg", "EY1": "char1.jpg", "EY2": "char1.jpg",
                        "F": "char11.jpg", "G": "char9.jpg", "HH": "char10.jpg",
                        "IH0": "char4.jpg", "IH1": "char4.jpg", "IH2": "char4.jpg",
                        "IY0": "char5.jpg", "IY1": "char5.jpg", "IY2": "char5.jpg",
                        "JH":"char9.jpg" , "K": "char9.jpg", "L": "char10.jpg",
                        "M": "char7.jpg", "N": "char9.jpg", "NG": "char9.jpg",
                        "OW0": "char6.jpg", "OW1": "char6.jpg", "OW2": "char6.jpg",
                        "OY0": "char6.jpg", "OY1": "char6.jpg", "OY2": "char6.jpg",
                        "P": "char7.jpg", "R": "char2.jpg", "S": "char5.jpg",
                        "SH": "char5.jpg","T": "char8.jpg", "TH": "char10.jpg",
                        "UH0": "char2.jpg", "UH1": "char2.jpg", "UH2": "char2.jpg",
                        "UW0": "char6.jpg", "UW1": "char6.jpg", "UW2": "char6.jpg",
                        "V": "char11.jpg", "W": "char6.jpg", "Y": "char5.jpg",
                        "Z": "char5.jpg", "ZH": "char5.jpg", "br": "char.jpg",
                        "cg": "char.jpg", "lg": "char.jpg", "ls": "char.jpg",
                        "ns": "char.jpg", "sil": "char.jpg", "sp": "char.jpg"}

        file_dir = os.path.normpath(os.path.dirname(os.path.realpath(__file__))+ os.sep + os.pardir+ os.sep+'sprites/')
        for key,value in self.images.items(): self.images[key]= os.path.join(file_dir, value) #.../sprites/char?
    
    def convert_phonemes(self,timestaps_path): #read .jason file and convert timestaps to sprites addresses
        json_file= open(timestaps_path, )
        data = json.load(json_file)
        timestamps = [[word["alignedWord"],word["start"],word["end"],word["phonemes"]] for word in data["words"]]
        return timestamps

    def word_values(self, word): #word = [word value, start, end, phonemes list]
        return word[0], (word[2]-word[1]), word[3]

    def phoneme_values(self,phoneme): #phoneme = [phoneme value, start, end]
        return phoneme[0], (phoneme[2]-phoneme[1])

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
        result.write_videofile(video_path, audio=True,fps=fps)

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