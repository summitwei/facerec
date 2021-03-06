import numpy as np
import pickle
from dlib_models import models


def face_to_vector(pic, shape):
    """
    Receives a face as a numpy array from dlib. Converts this face array to a 128-dimensional vector using dlib

    :param
    pic: numpy.ndarray()
    The face's image data (cropped)

    shape: np.array
    The parts of the image that we want

    :return:
    descriptor: 128-dimensional array
    The descriptions related to the individual faces

    """
    face_rec_model = models["face rec"]
    descriptor = np.array(face_rec_model.compute_face_descriptor(pic, shape))

    return descriptor


def desc_comp_data(vect):
    """
    Takes the 128-dimensional vector describing individual faces and compares it to the database. Returns the name of the match or that there was no match found.

    :param
    vect: numpy.ndarray(shape=(128,))
    This is the descriptory vector given by face_to_vector.

    :return:
    closest: String
    This is the final match that the face will be recognized as (given in a string)

    least: float-number
    This is the similarity number (lower = more similar) that 'closest' returned
    """
    with open("mean_vecs.pickle", "rb") as faceFile:
        faceDict = dict(pickle.load(faceFile))


    diffs = {}
    index=0

    for key in faceDict:
        print(faceDict[key].shape)
        currentdiff = np.sqrt(np.sum(vect-faceDict[key])**2)
        # index+=1
        # print(vect[index])
        # print(faceDict[key])
        diffs[key] = currentdiff

    mydictkeys = list(diffs.keys())
    least = diffs[mydictkeys[0]]
    closest = mydictkeys[0]

    for key in diffs:

        if diffs[key]<least:
            least = diffs[key]
            closest = key

    # To be computed after data: gives threshold if face is not close to any
    threshhold = 0.5
    if (least>threshhold):
        return "No face match found from database",least
    else:
        return closest,least

    # return closest, least