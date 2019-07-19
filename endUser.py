import pickle
import sys
from camera import take_picture
from C import C1
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from FaceToDescription import face_to_vector,desc_comp_data

def main():
    pickleName="mean_vecs.pickle"
    with open(pickleName,"rb") as faceFile:
        faceDic=pickle.load(faceFile)
    answer = "None"
    while answer.lower() not in ["yes", "no"]:
        answer = input("Type yes to take a picture and recognize faces")
        answer = answer.lower()
        if answer == "yes":
            pass
        elif answer == "no":
            sys.exit(0)
        else:
            answer = "None"

    # Add camera taking(perhaps me/perhaps Charles)
    #
    #


    img_array=take_picture()
    # faceIm,coordinates=C1(img_array)
    detections,shapes=C1(img_array)


    fig,ax=plt.subplots()
    ax.imshow(img_array)
    #

    for index,a in enumerate(detections):
        desc_vector=face_to_vector(img_array,shapes[index])
        match=desc_comp_data(desc_vector)
        l,r,t,b=a.left(),a.right(),a.top(),a.bottom()


        rectange = patches.Rectangle((l, b), r - l, t - b, linewidth=1, edgecolor='r', facecolor='none')

        ax.add_patch(rectange)
        ax.text((l + 10), b + 40, match, color="red", fontsize=20)

    plt.show()










#     import matplotlib.pyplot as plt
#     import matplotlib.patches as patches
#     from camera import take_picture
#     import camera
#     import sys
#     import dlib_models
#     from dlib_models import load_dlib_models
#
#     # this loads the dlib models into memory. You should only import the models *after* loading them.
#     # This does lazy-loading: it doesn't do anything if the models are already loaded.
#     load_dlib_models()
#
#     from dlib_models import models  # must be called after loading the models
#
#     answer = "None"
#     while answer.lower() not in ["yes", "no"]:
#         answer = input("Type yes to take a picture and recognize faces")
#         answer = answer.lower()
#         if answer == "yes":
#             pass
#         elif answer == "no":
#             sys.exit(0)
#         else:
#             answer = "None"
#     img_array = take_picture()
#     face_detect = models["face detect"]
#
#     # Number of times to upscale image before detecting faces.
#     # When would you want to increase this number?
#     upscale = 1
#
#     detections = face_detect(img_array, upscale)  # returns sequence of face-detections
#     detections = list(detections)
#
#     det = detections[0]  # first detected face in image
#
#     # bounding box dimensions for detection
#     l, r, t, b = det.left(), det.right(), det.top(), det.bottom()
#
#     print(l)
#     print(r)
#     print(t)
#
#     print(b)
#
#     fig, ax = plt.subplots()
#     ax.imshow(img_array)
#
#     rectange = patches.Rectangle((l, b), r - l, t - b, linewidth=1, edgecolor='r', facecolor='none')
#     ax.add_patch(rectange)
#
#     plt.show()