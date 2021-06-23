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
                        "Z": "char5.jpg", "ZH": "char5.jpg", "br": "char7.jpg",
                        "cg": "char7.jpg", "lg": "char7.jpg", "ls": "char7.jpg",
                        "ns": "char7.jpg", "sil": "char7.jpg", "sp": "char7.jpg"}

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
        values=['']
        for i in range(len(timestamps)):
            if i%7==0: values = [values[-1]]
            word = timestamps[i]
            value, duration_total, phonemes = self.word_values(word)
            if not value in ['sp','sil','LG','NS','BR','CG','LS']:
                values.append(value.lower())
            text = TextClip(' '.join(values),color='green', font='Arial',fontsize=80).set_duration(duration_total)
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

