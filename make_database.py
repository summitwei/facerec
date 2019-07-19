# Take existing pictures and make database of name:descriptor vectors & mean vector.(Eric)
from C import C_1
from Camera import take_picture
import dlib
from FaceToDescription import face_to_vector
import numpy as np
import pickle

def make_data(pics, nms):
    '''
    Creates a database of people and their associated vectors.

    Takes in images and creates databases (dictionaries) that map names to descriptor vectors
    and the mean vector for that person. Then puts these databases into pickle files.

    Parameters:
    -----------
    pics: list[ndarray]
    ndarray dims: 3xnxn

    nms: list[String]

    Returns:
    --------
    Dict{String, ndarray}
    ndarray dims: (128, )
    The mean arrays for every person.
    '''

    try:
        with open("vecs.pickle","rb") as vecFile:
            vecs=pickle.load(faceFile)
    except:
        vecs = {}
    
    mean_vecs = {}
    for i in range(len(pics)):
        name = nms[i]
        pic = pics[i]
        detecs, shapes = C1(pic)
        descriptor = face_to_vector(pic, shapes[0])
        if(names not in vecs):
            vecs[name] = np.array([descriptor])
        else:
            vecs[name].append(descriptor)
    
    for name,descs in vecs:
        mean_vecs[name] = np.mean(descs, axis=1)
    
    pickle_out = open("vecs.pickle", "wb")
    pickle.dump(vecs, pickle_out)
    pickle_out.close()
    pickle_out2 = open("mean_vecs.pickle", "wb")
    pickle.dump(mean_vecs, pickle_out2)
    pickle_out2.close()
    return mean_vecs

def add_to_dict():
    '''take camera picture and add it to the dictionary'''

    img = take_picture()
    answer = input("who is this?")
    make_data([img], [answer])
