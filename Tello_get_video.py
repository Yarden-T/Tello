from djitellopy import tello
import cv2
from time import sleep

# drone = tello.Tello()
# drone.connect()
# print("Battery:", drone.get_battery())


# drone.streamon()

def getVideo(drone):
    while True:
        img = drone.get_frame_read().frame
        img = cv2.resize(img, (360,240))
        cv2.imshow("image", img)
        cv2.waitKey(1)

if __name__ =='__main__':
    
    while True:
        getVideo()