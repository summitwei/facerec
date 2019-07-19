# Take existing pictures and make database of name:descriptor vectors & mean vector.(Eric)
from FaceToDescription import face_to_vector
import dlib
import numpy as np

def make_data(pics):
    '''
    Creates a database of people and their associated vectors.

    Takes in images and creates databases (dictionaries) that map names to descriptor vectors
    and the mean vector for that person. Then puts these databases into pickle files.

    Parameters:
    -----------
    pics: list[tuple(String, ndarray)]
    ndarray dims: 3xnxn


    Returns:
    --------
    Dict{String, ndarray}
    ndarray dims: (128, )
    The mean arrays for every person.
    '''
    
    vecs = {}
    mean_vecs = {}
    for pic in pics:
        name = pic[0]
        descriptor = face_to_vector(pic[1])
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