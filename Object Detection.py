from djitellopy import tello
import cv2
##################################################
width=320  # Width of the image
height=240 # height of the image
startCounter=0 # 0 for flight 1 for testing
#################################################

#connect to tello
me=tello.Tello()
me.connect()
me.for_back_velocity=0
me.left_right_velocity=0
me.up_down_velocity=0
me.yaw_velocity=0
me.speed=0
print(me.get_battery())
me.streamoff()
me.streamon()

while True:
    # get the image from tello
    fra,e_read=me.get_frame_read()
    myFrame=frame_read.frame
    img=cv2.resize(myFrame,(width,height))

    #to go up in in the begining
