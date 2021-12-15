import cv2
#from djitellopy import tello
import cvzone
thres=0.6 # if the cam is 60% sure that it is a object it displays it
nmsThres=0.2
cap=cv2.VideoCapture(0)
cap.set(3,640) # For setting width
cap.set(4,480) # For setting height
classNames=[]
classFile='coco.names'
with open(classFile,'rt') as f: #opening file coco.names
    classNames=f.read().split('\n')
print(classNames)
# For paths and using this we can load it easily
configPath = 'ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt'
weightsPath = "frozen_inference_graph.pb"
# Configuration Parameters
net = cv2.dnn_DetectionModel(weightsPath,configPath)
net.setInputSize(320,320)
net.setInputScale(1.0/127.5)
net.setInputMean((127.5,127.5,127.5))
net.setInputSwapRB(True) # to flip opencv to rgr
while True:
    success,img=cap.read()
    #nms is used to detect duplicate objects
    classIds,confs,bbox=net.detect(img,confThreshold=thres,nmsThreshold=nmsThres)  # if 60% matches only the object is considered or ignored
    try:
        for classId,conf,box in zip(classIds.flatten(),confs.flatten(),bbox):
            cvzone.cornerRect(img,box)
            cv2.putText(img,f'{classNames[classId-1].upper()}{round(conf*100,2)}',
                        (box[0]+10,box[1]+30),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(0,255,0),2) # for displaying the text


    except:
        pass
    cv2.imshow("Image",img)
    cv2.waitKey(1)