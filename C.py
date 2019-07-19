def Csub1():
    from dlib_models import download_model, download_predictor, load_dlib_models
    download_model()
    download_predictor()
    from dlib_models import models
#DLIB

def Csub2():
    load_dlib_models()
    face_detect = models["face detect"]
    face_rec_model = models["face rec"]
    shape_predictor = models["shape predict"]

def Csub3(image):
    detections = list(face_detect(image))

def Csub4():
    print("Number of faces detected: {}".format(len(detections)))
    for k, d in enumerate(detections):
    # Get the landmarks/parts for the face in box d.
        shape = shape_predictor(image, d)
    return shape
def C1(image):
    ''' Inputs a picture returns the picture and shape'''
    Csub1()
    Csub2()
    Csub3(image)
    shape=Csub4
    return (image, shape),shape