
'''Use this once to load all the pictures'''
from dlib_models import download_model, download_predictor, load_dlib_models
download_model()
download_predictor()
from dlib_models import models
load_dlib_models()
face_detect = models["face detect"]
face_rec_model = models["face rec"]
shape_predictor = models["shape predict"]
shape =[]
image =None
shape = None
def Csub3(image):
    image = image
    shape = shape
    detections = list(face_detect(image,1)) #This is holding all the faces in the photo
    return detections # These are the corners
def Csub4(detections):
    #print("Number of faces detected: {}".format(len(detections))) # I see x faces
    l=[]#holds the shape vectors

    for k, d in enumerate(detections):
    # Get the landmarks/parts for the face in box d.
        shape = shape_predictor(image, d) #mesh
        l.append(shape)
    return l


def C1(image):
    ''' Inputs a picture returns the picture and array of shapes '''

    detections = Csub3(image)
    shape=Csub4(detections)
    shape= shape_predictor(image, detections[0])
    C2(image , shape)
    return detections
def C2():
    return image, shape