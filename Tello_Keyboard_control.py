import Tello_Keyboard_module as kp
from djitellopy import tello
from time import sleep


kp.init()

# drone = tello.Tello()
# drone.connect()
# print(drone.get_battery())

def getKeyboardInput(drone):
    lr , fb , ud, yv = 0 , 0  , 0 , 0
    speed = 50

    if kp.getKey("LEFT"): lr = - speed
    elif kp.getKey("RIGHT"): lr = speed


    if kp.getKey("UP"): fb =  speed
    elif kp.getKey("DOWN"): fb = - speed
    
    if kp.getKey("w"): ud =  speed
    elif kp.getKey("s"): ud = -speed

    
    if kp.getKey("a"): yv =  -speed
    elif kp.getKey("d"): yv = speed

    if kp.getKey("q"): drone.land()
    if kp.getKey("e"): drone.takeoff()

    return [lr , fb , ud, yv]
    
def keyboardControl(drone):
    while True:
        vals = getKeyboardInput(drone)
        drone.send_rc_control(vals[0],vals[1],vals[2],vals[3])
        
