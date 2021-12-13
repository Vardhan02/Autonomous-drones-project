#from djitellopy import tello
import KeyPressModule as kp
import time
import cv2

kp.init()
#me = tello.Tello()
#me.connect()
#print(me.get_battery())
global img
#me.streamon()
cap = cv2.VideoCapture(0)
cap.set(3,640) # For setting width
cap.set(4,480) # For setting height

def getKeyboardInput():
    lr, fb, ud, yv = 0, 0, 0, 0
    speed = 50

    if kp.getKey("LEFT"): lr = -speed
    elif kp.getKey("RIGHT"): lr = speed

    if kp.getKey("UP"): fb = speed
    elif kp.getKey("DOWN"): fb = -speed

    if kp.getKey("w"): ud = speed
    elif kp.getKey("s"): ud = -speed

    if kp.getKey("a"): yv = -speed
    elif kp.getKey("d"): yv = speed

    if kp.getKey("q"): yv = time.sleep(3); #me.land()
    #if kp.getKey("e"): yv = me.takeoff()

    if kp.getKey('z'):
        cv2.imwrite(f'Resources/Images/{time.time()}.jpg',img)
        time.sleep(0.3)

    return [lr, fb, ud, yv]

while True:
    vals = getKeyboardInput()
    #me.send_rc_control(vals[0], vals[1], vals[2], vals[3])
    #img = me.get_frame_read().frame
    success,img=cap.read()
    cv2.imshow("Image", img)
    cv2.waitKey(1)
