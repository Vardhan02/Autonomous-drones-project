import cv2
import numpy as np

# Parameters
frameWidth=640
franeHeight=480
cap=cv2.VideoCapture(1)
cap.set(3,frameWidth)
cap.set(4,franeHeight)

deadZone=100
global imgContour

def empty(a):
    pass
# Trackbars for Hsv space
cv2.namedWindow("HSV")
cv2.resizeWindow("HSV",640,240)
cv2.createTrackbar("HUE Min","HSV",19,179,empty)
cv2.createTrackbar("HUE Max","HSV",35,179,empty)
cv2.createTrackbar("SAT Min","HSV",107,255,empty)
cv2.createTrackbar("SAT Max","HSV",255,255,empty)
cv2.createTrackbar("VALUE Min","HSV",89,255,empty)
cv2.createTrackbar("VALUE Max","HSV",255,255,empty)

# Trackbar for kenny edge detector
cv2.namedWindow("Parameters")
cv2.resizeWindow("Parameters",640,240)
cv2.createTrackbar("Threshold1","Parameters",166,255,empty)
cv2.createTrackbar("Threshold2","Parameters",171,255,empty)
cv2.createTrackbar("Area","Parameters",3750,30000,empty)

def stackImages(scale,imgArray):
    rows=len(imgArray)
    cols=len(imgArray[0])
    rowAvailable=isinstance(imgArray[0],list)
    width=imgArray[0][0].shape[1]
    height=imgArray[0][0].shape[0]
    if rowAvailable:
        for x in range(0,rows):
            for y in range(0,cols):
                if imgArray[x][y].shape[:2]==imgArray[0][0].shape[:2]:
                    imgArray[x][y]=cv2.resize(imgArray[x][y],(0,0),None,scale,scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y],(imgArray[0][0].shape[1],imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y].shape)==2:
                    imgArray[x][y]=cv2.cvtColor(imgArray[x][y],cv2.COLOR_GRAY2BGR)
                    imageBlank=np.zeroes((height,width,3),np.uints)
                    hor=[imageBlank]*rows
                    hor_con=[imageBlank]*rows
                    for x in range(0,rows):
                        hor[x]=np.hstack(imgArray[x])
                    ver=np.vstack(hor)
                else:
                    for x in range(0,rows):
                        if imgArray[x][y].shape[:2] == imgArray[0][0].shape[:2]:
                            imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                        else:
                            imgArray[x][y] = cv2.resize(imgArray[x][y],
                                                        (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale,scale)
                        if len(imgArray[x][y].shape) == 2:
                            imgArray[x][y] = cv2.cvtColor(imgArray[x][y], cv2.COLOR_GRAY2BGR)
                hor=np.hstack(imgArray)
                ver=hor
    return ver
def getContours(img,imgContour):
    contours,heirachy=cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area=cv2.counterArea(cnt)
        areaMin=cv2.getTrackbarPos("Area","Parameters")
        if area>areaMin:
            cv2.drawContours(imgContour,cnt,-1,(255,0,255),7)
            peri=cv2.arcLength(cnt,True)
            approx=cv2.approxPolyDP(cnt,0.02*peri,True)
            print(len(approx))
            x,y,w,h=cv2.boundingRect(approx)
            cv2.rectangle(imgContour,(x,y),(x+w,y+h),(0,255,0),5)
            cv2.puttext(imgContour,"Points: ",+str(len(approx)),(x+w+20,y+20),cv2.FONT_HERSHEY_COMPLEX,0.7,(0,255,0),2)
            cv2.puttext(imgContour, "Area: ", +str(len(area)), (x + w + 20, y + 45), cv2.FONT_HERSHEY_COMPLEX, 0.7,
                        (0, 255, 0), 2)
            cv2.puttext(imgContour, " ", +str(int(x))+"",+str(int(y)),(x-20,y-45),cv2.FONT_HERSHEY_COMPLEX, 0.7,
                        (0, 255, 0), 2
            cx=int(x+(w/2))
            cy=int(y+(h/2))

            if()







