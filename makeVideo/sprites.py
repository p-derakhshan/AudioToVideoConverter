class Sprites():
    def __init__(self):
        super(Sprites, self).__init__()
        #read images
        self.images = {'A':'sprites/A.jpg',
                       'O':'sprites/O.jpg',
                       'E':'sprites/E.jpg',
                       'WR':'sprites/WR.jpg',
                       'TS':'sprites/TS.jpg',
                       'LN':'sprites/LN.jpg',
                       'UQ':'sprites/UQ.jpg',
                       'MBP':'sprites/MBP.jpg',
                       'FV':'sprites/FV.jpg'}
        
 
    def getImg(self,face):
        '''to make sure all pictures have the same size'''
        image = self.images[face]
        #image = cv2.resize(self.images[face],(110, 300)) 
        height, width, layers = image.shape
        size = (width, height)
        return image

def getLists():
    '''get list of frame names,vowels and durations'''
    #create sprite object
    face_sprites = Sprites()
    #desired face expression 
    import pandas as pd
    df=pd.read_csv('formants.csv')
    vowels = df['vowel'].tolist()
    durations = df['dur'].tolist()
    times = []
    faces = []
    frames = []
    for i in range(len(vowels)):
        faces.append(vowels[i])
        times.append(int((durations[i]/2) *100))
        frames.append(face_sprites.images[vowels[i]])
    return frames, times, faces
