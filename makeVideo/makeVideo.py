from os.path import isfile, join
import cv2

class MakeVideo():
    def __init__(self,path_out, frames, times, texts):
        self.fps=19
        self.path_out, self.frames, self.times, self.texts = path_out, frames, times, texts
        self.font = cv2.FONT_HERSHEY_SIMPLEX
        self.pic_to_video()

    def pic_to_video(self):
        #converts images to video
        frame_array =[]
        text_array=[]
        current_text=''
        for i in range(len(self.frames)):
        #read images
            filename = self.frames[i]
            img = cv2.imread(filename)
            #to make sure all pictures have the same size
            #img = cv2.resize(img,(816,460)) 
            height, width, layers = img.shape
            size = (width, height)
            current_text+=self.texts[i]
            for time in range(self.times[i]):
                text_array.append(current_text)
                frame_array.append(img)
            if i %5 ==0 : current_text=''
        out = cv2.VideoWriter(self.path_out, cv2.VideoWriter_fourcc(*'mp4v'),self.fps,size)
        for i in range(len(frame_array)):
            out.write(frame_array[i])
            cv2.putText(frame_array[i],text_array[i],(100, 1300), self.font, 1, (255, 0, 0), 2, cv2.LINE_4)
        out.release()  
        return text_array