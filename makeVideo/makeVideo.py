'''preprocess'''
images = {'A': 'sprites/A.jpg', 'I': 'sprites/A.jpg', 'O': 'sprites/O.jpg', 'E': 'sprites/E.jpg', 'K': 'sprites/E.jpg',
          'W': 'sprites/WR.jpg', 'R': 'sprites/WR.jpg', 'Y': 'sprites/WR.jpg', 'T': 'sprites/TS.jpg',
          'J': 'sprites/TS.jpg',
          'C': 'sprites/TS.jpg', 'S': 'sprites/TS.jpg', 'G': 'sprites/TS.jpg', 'Z': 'sprites/TS.jpg',
          'H': 'sprites/TS.jpg',
          'X': 'sprites/TS.jpg', 'L': 'sprites/LN.jpg', 'D': 'sprites/LN.jpg', 'N': 'sprites/LN.jpg',
          'U': 'sprites/UQ.jpg',
          'Q': 'sprites/UQ.jpg', 'M': 'sprites/MBP.jpg', 'B': 'sprites/MBP.jpg', 'P': 'sprites/MBP.jpg',
          ' ': 'sprites/MBP.jpg',
          'W': 'sprites/MBP.jpg', 'F': 'sprites/FV.jpg', 'V': 'sprites/FV.jpg'}

class Word():
    def __init__(self,word,start,end,phonemes):
        self.aligned_word,self.dur,self.phonemes=word,(end-start),phonemes
'''test'''
words=[Word('SP',0.0,0.27,[[' ',0.0,0.27]]),
        Word('I',0.27,0.43,[['A',0.27,0.43]]),
        Word('BEG',0.43,0.76,[['B',0.43,0.60],['E',0.60,0.66],['G',0.66,0.76]]),
        Word('YOUR',0.76,0.93,[['Y',0.76,0.86],['O',0.86,0.89],['R',0.89,0.93]]),
        Word('PARDON',0.93,1.49,[['P',0.93,1.05],['N',1.05,1.49]]),
        Word('SP',1.49,1.62,[[' ',1.49,1.62]]),
        Word('SAID',1.62,1.84,[['S',1.62,1.44],['D',1.44,1.84]]),
        Word('THE',1.84,1.90,[['D',1.84,1.87],['E',1.87,1.90]]),
        Word('MOUSE',1.90,2.46,[['M',1.90,2.16],['S',2.16,2.46]]),
        Word('FROWNING',2.46,2.87,[['F',2.46,2.67],['G',2.46,2.67]]),
        Word('BUT',2.87,3.06,[['B',2.87,2.96],['T',2.96,3.06]]),
        Word('VERY',3.06,3.34,[['V',3.06,3.24],['Y',3.24,3.34]]),
        Word('POLITELY',3.34,3.87,[['P',3.34,3.57],['Y',3.57,3.87]]),
        Word('SP',3.87,4.09,[[' ',3.87,4.09]]),
        Word('DID',4.09,4.36,[['D',4.09,4.16],['Y',4.16,4.36]]),
        Word('YOU',4.36,4.82,[['Y',4.36,4.50],['U',4.50,4.82]]),
        Word('SPEAK',4.82,4.94,[['S',4.82,4.89],['K',4.89,4.94]]),
        Word('SP',4.94,5.43,[[' ',4.94,5.43]])]
        
'''process'''
from moviepy.editor import *
fps=25
videos = []
for word in words:
    value,dur,phonemes=word.aligned_word, word.dur, word.phonemes
    sub_txt = TextClip(value,color='green', font='Arial',fontsize=20).set_pos('center','bottom').set_duration(dur)
    frames=[]
    for phonem in phonemes:
        vowel,duration=phonem[0],(phonem[2]-phonem[1])
        frames.append(ImageClip(images[phonem],duration=duration).img)
    sub_video=ImageSequenceClip(frames,fps=fps)
    videos.append(CompositeVideoClip[sub_video,sub_txt])
        
video = concatenate_videoclips(videos)
video = video.set_audio(AudioFileClip('test.wav'))
video.write_videofile("test.mp4", audio=True)
