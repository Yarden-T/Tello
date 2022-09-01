from threading import Thread
from djitellopy import tello
import Tello_Keyboard_module as kp
import Tello_Keyboard_control as kc
import Tello_get_video as vd


kp.init()

drone = tello.Tello()
drone.connect()
print(drone.get_battery())
drone.streamon()

th2 = Thread(target= vd.getVideo(drone))
th1 = Thread(target = kc.keyboardControl(drone))


th2.start()
th1.start()

