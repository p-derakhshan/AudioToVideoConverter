from moviepy.editor import *
from moviepy.video.tools.subtitles import SubtitlesClip
import os, json, math
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
    
    def convert_phonemes(self, timestamps_path): #read .jason file and convert timestaps to sprites addresses
        json_file= open(timestamps_path, )
        data = json.load(json_file)
        self.timestamps = [[word["alignedWord"],word["start"],word["end"],word["phonemes"]] for word in data["words"]]

    def time_format(self, x): #return hh:mm:ss,ms format
        x_f=math.floor(x)
        hour=x_f//3600
        minute=(x_f-hour*3600)//60
        sec = x_f - hour*3600-minute*60
        msec = int(math.modf(x)[0] * 100)
        r = '{}:{}:{},{}'.format(str(hour).zfill(2),str(minute).zfill(2),str(sec).zfill(2),str(msec). zfill(3))
        return r
        
    def create_subtitles(self, subtitles_path):
        subtitle=''
        for i in range(0,len(self.timestamps),7):
            line, words = '', self.timestamps[i:i+7]
            for word in words: #word = [word value, start, end, phonemes list]
                if not word[0] in ['sp','sil','LG','NS','BR','CG','LS']: line += (word[0].lower()+' ')
            start_msec,end_msec = words[0][1],words[-1][2]
            start,end=self.time_format(start_msec),self.time_format(end_msec)
            subtitle += ('{}\n{} --> {}\n{}\n\n'.format(i+1,start,end,line))
            srt_file = open(subtitles_path,'w',encoding='utf-8')
            srt_file.write(subtitle)
            srt_file.close
        return subtitles_path

    def creat_video(self, audio_path, video_path, subtitles_path): #create the output video file
        frames, fps = [], 25
        for word in self.timestamps:
            phonemes = word[3]
            for phoneme in phonemes: #phoneme = [phoneme value, start, end]
                vowel,duration = phoneme[0], (phoneme[2]-phoneme[1])
                frame = ImageClip(self.images[vowel],duration=duration)
                frames.append(frame)

        generator = lambda txt: TextClip(txt, font='Arial', fontsize=80, color='green')
        subtitles = SubtitlesClip(subtitles_path, generator)

        video= concatenate_videoclips(frames,method='compose')
        video = video.set_audio(AudioFileClip(audio_path))
        result = CompositeVideoClip([video,subtitles.set_pos('bottom')])
        result.write_videofile(video_path, audio=True,fps=fps)

