import pickle
import sys

pickleName=""
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
