from speechrecognition import *


sample=speechrecognition('deepspeech-0.7.4-models.pbmm','deepspeech-0.7.4-models.scorer',100,0.75,1.85,"audio files/wrong_format")
filename='MY MORNING ROUTINE _ how my house is always clean!.mp3'
text_file = open(os.path.splitext(filename)[0]+".txt", "w+")
text_file.write(sample.convert_speech_to_text(filename))
text_file.close()
