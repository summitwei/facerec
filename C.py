def Csub1():
    '''Use this once to load all the pictures'''
    from dlib_models import download_model, download_predictor, load_dlib_models
    download_model()
    download_predictor()
    from dlib_models import models
    load_dlib_models()
    face_detect = models["face detect"]
    face_rec_model = models["face rec"]
    shape_predictor = models["shape predict"]

def Csub3(image):
    detections = list(face_detect(image))

def Csub4():
    print("Number of faces detected: {}".format(len(detections)))
    l=[]
    for k, d in enumerate(detections):
    # Get the landmarks/parts for the face in box d.
        shape = shape_predictor(image, d
        l.append(shape)
    return l


def C1(image):
    ''' Inputs a picture returns the picture and array of shapes '''

    Csub3(image)
    shape=Csub4
    shape= shape_predictor(pic, detections[0])
    return (image,shape), l