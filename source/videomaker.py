'''preprocess'''
import os
images = {'A': 'sprites/char1.jpg', 'I': 'sprites/char1.jpg', 'O': 'sprites/char2.jpg', 'E': 'sprites/char9.jpg', 'K': 'sprites/char9.jpg',
          'W': 'sprites/char7.jpg', 'R': 'sprites/char7.jpg', 'Y': 'sprites/char7.jpg', 'T': 'sprites/char6.jpg',
          'J': 'sprites/char6.jpg',
          'C': 'sprites/char6.jpg', 'S': 'sprites/char6.jpg', 'G': 'sprites/char6.jpg', 'Z': 'sprites/char6.jpg',
          'H': 'sprites/char6.jpg',
          'X': 'sprites/char6.jpg', 'L': 'sprites/char8.jpg', 'D': 'sprites/char8.jpg', 'N': 'sprites/char8.jpg',
          'U': 'sprites/char3.jpg',
          'Q': 'sprites/char3.jpg', 'M': 'sprites/char4.jpg', 'B': 'sprites/char4.jpg', 'P': 'sprites/char4.jpg',
          ' ': 'sprites/char4.jpg',
          'W': 'sprites/char4.jpg', 'F': 'sprites/char5.jpg', 'V': 'sprites/char5.jpg'}
file_dir = os.path.normpath(os.path.dirname(os.path.realpath(__file__))+ os.sep + os.pardir)
for key,value in images.items(): images[key]= os.path.join(file_dir, value)
        
class Word():
    def __init__(self,word,start,end,phonemes):
        self.aligned_word,self.dur,self.phonemes=word,(end-start),phonemes

words=[Word(' ',0.0,0.27188208616780046,[[' ',0.0,0.27188208616780046]]),
        Word('I',0.27188208616780046,0.43151927437641724,[['A',0.27188208616780046,0.43151927437641724]]),
        Word('BEG',0.43151927437641724,0.7607709750566894,[['B',0.43151927437641724,0.6011337868480726],['E',0.6011337868480726,0.660997732426304],['G',0.660997732426304,0.7607709750566894]]),
        Word('YOUR',0.7607709750566894,0.9303854875283447,[['Y',0.7607709750566894,0.8605442176870749],['O',0.8605442176870749,0.8904761904761905],['R',0.9303854875283447,0.9303854875283447]]),
        Word('PARDON',0.9303854875283447,1.49,[['P',0.9303854875283447,1.05],['N',1.05,1.49]]),
        Word('SP',1.49,1.62,[[' ',1.49,1.62]]),
        Word('SAID',1.62,1.84,[['S',1.62,1.44],['D',1.44,1.84]]),
        Word('THE',1.84,1.90,[['D',1.84,1.87],['E',1.87,1.90]]),
        Word('MOUSE',1.90,2.46,[['M',1.90,2.16],['S',2.16,2.46]]),
        Word('FROWNING',2.46,2.87,[['F',2.46,2.67],['G',2.46,2.67]]),
        Word('BUT',2.87,3.06,[['B',2.87,2.96],['T',2.96,3.06]]),
        Word('VERY',3.06,3.34,[['V',3.06,3.24],['Y',3.24,3.34]]),
        Word('POLITELY',3.34,3.87,[['P',3.34,3.57],['Y',3.57,3.87]]),
        Word(' ',3.87,4.09,[[' ',3.87,4.09]]),
        Word('DID',4.09,4.36,[['D',4.09,4.16],['Y',4.16,4.36]]),
        Word('YOU',4.36,4.82,[['Y',4.36,4.50],['U',4.50,4.82]]),
        Word('SPEAK',4.82,4.94,[['S',4.82,4.89],['K',4.89,4.94]]),
        Word(' ',4.94,5.43,[[' ',4.94,5.43]])]
        
'''process'''
from moviepy.editor import * #ImageClip
fps=25
texts, frames=[], []
for word in words:
    value,dur,phonemes=word.aligned_word, word.dur, word.phonemes
    text = TextClip(value,color='green', font='Arial',fontsize=140).set_pos('bottom').set_duration(dur)
    texts.append(text)
    for phonem in phonemes:
        vowel,duration=phonem[0],(phonem[2]-phonem[1])
        frame = ImageClip(images[vowel],duration=duration)
        frames.append(frame)


subtitle = concatenate(texts,method='compose')
video= concatenate(frames,method='compose')
video = video.set_audio(AudioFileClip('files/test.wav'))
result = CompositeVideoClip([video,subtitle.set_pos('bottom')])
result.write_videofile('files/test.mp4', audio=True,fps=fps)