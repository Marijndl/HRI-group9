import math
import numpy as np
import random
import nao_nocv_2_1 as nao
import time
import pepper_nocv_2_0 as pepper
import pepper_laser as laser


###################################################################### initialization

robot_IP="192.168.0.119"
# robot_IP="127.0.0.1"

pepper.InitProxy(robot_IP)
pepper.InitPose()
pepper.InitSonar(True)
pepper.InitLandMark()
# pepper.InitVideo(resolution_id=2) # [160,120],[320,240],[640,480],[1280,960]
# pepper.ExtCollisionProtection("Move",True)


###################################################################### function definitions

def landmark_info_debug():
    detected, timestamp, markerInfo=pepper.DetectLandMark()
    print(detected,markerInfo)


def look_on_spot(rotate=True):
    """
    scans current view for landmark
    if not found and `rotate == True`, turns around and scans again 
    """
    found_bool, xvalue, sizeY, current_yaw, yaw_rate = lookltr()
    if (found_bool == False) and (rotate == True): #if not in view, turn around and try again
        pepper.Walk(0.,0.,np.pi)
        found_bool, xvalue, sizeY, current_yaw, yaw_rate = lookltr()
    return found_bool, xvalue, sizeY, current_yaw, yaw_rate

def lookltr(yaw_rate = 0.5):
    """
    look from left to right at `yaw_rate` until landmark is found or can't turn anymore
    """
    yaw_start = 2
    yaw_end = -2
    yaw_counter = yaw_start
    found_bool = False

    #to prevent spotting the target before the head has turned
    initial_pause = True

    start_time = time.time()
    while ((found_bool == False) and (yaw_counter>=yaw_end)):
        
        #every 2 seconds:
        if time.time() - start_time >= 2:
            pepper.MoveHead(yaw_val=yaw_counter)
            if initial_pause:
                time.sleep(2)
                initial_pause = False
            time.sleep(1)
            found_bool, target_x_location, sizeY = is_target_found()

            print(found_bool, yaw_counter) #debugging purposes
            yaw_counter = yaw_counter - yaw_rate #update yaw
            start_time = time.time() #reset timer


    print("YAW REAL, X VAL, CALC. ROT.:",yaw_counter, target_x_location,yaw_counter+yaw_rate+target_x_location )
    return found_bool, target_x_location, sizeY, yaw_counter,yaw_rate

def is_target_found():
    detected, _, markerInfo = pepper.DetectLandMark()
    if detected:
        return detected, markerInfo[0][1], markerInfo[0][4]
    return detected, 0, 0


def continuously_avoid_obstacles(avoidance_duration = 4, stop = True):
    """
    avoids obstacles for `avoidance_duration`, then stops by default
    """
    start_time = time.time()
    while (time.time() - start_time) <= avoidance_duration:
        avoid_obstacle()
    if stop:
        pepper.Move(0,0,0)


def walk_towards_target(target_x_location, sizeY,current_yaw, yaw_rate, move_duration = 10, stop = True):
    """
    Aligns body with target and sends Move command, moves 
    for `move_duration` seconds while avoiding obstacles, then stops by default.
    """
    #align body with target 
    print("walk_towards_target - YAW REAL, X VAL, CALC. ROT.:", current_yaw, target_x_location,current_yaw+yaw_rate+target_x_location)
    # raw_input("waiting - press enter") #pause
    pepper.Walk(0.,0.,current_yaw+yaw_rate+target_x_location)
    #start moving
    love_factor = calc_love_factor(sizeY)
    love_speed = love_factor
    pepper.Move(love_speed,0,0)
    #keep avoiding obstacles for `move_duration` (and potentially stop after )
    continuously_avoid_obstacles(move_duration, stop=stop)


def change_location_random(move_duration = 4, stop = True):
    dx,dy,theta = get_random_move()
    pepper.Walk(0.,0.,theta)
    pepper.Move(dx,dy,0)
    #while moving, continously check obstacles for n seconds (=move for n seconds) and then stop moving 
    continuously_avoid_obstacles(move_duration, stop=stop)
    print("@ new random location")
    

def get_random_move():
    dx = random.randint(5,11) * 0.1 #to get values from 0.5 to 1.
    dy = random.randint(5,11) * 0.1
    theta = random.randint(0,314) * 0.01
    print("get_random_move: ",dx,dy, theta)
    return dx,dy, theta


def avoid_obstacle(min_distance=0.3):
    [SL, SR] = pepper.ReadSonar()

    if SL<min_distance and SR<min_distance:
        print("both sonars obstacle - dodging - ", "SL:",SL, "SR:",SR)
        pepper.Walk(-min_distance*0.5, 0.,np.pi/8)
    elif SL<min_distance:
        print("left sonar obstacle - dodging - ", "SL:",SL, "SR:",SR)
        pepper.Walk(0.,-min_distance*0.5,0.)
    elif SR<min_distance:
        print("right sonar obstacle - dodging - ", "SL:",SL, "SR:",SR)
        pepper.Walk(0.,min_distance*0.5,0.)
        


def is_at_target(sizeY, size_limit = 0.2):
    return sizeY>=size_limit

def calc_love_factor(sizeY,size_limit = 0.20):
    love_factor= 1 - sizeY/size_limit + 0.3
    return love_factor

###################################################################### main execution loop

found_bool, target_x_location, sizeY, current_yaw, yaw_rate = look_on_spot()

while is_at_target(sizeY) == False:
    if found_bool:
        pepper.Say("found it")
        pepper.MoveHead(yaw_val=0)
        walk_towards_target(target_x_location, sizeY, current_yaw,yaw_rate, move_duration=4, stop = True)
    else:
        change_location_random(move_duration=4, stop = True) 
    found_bool, target_x_location, sizeY, current_yaw,yaw_rate = look_on_spot()
    pepper.MoveHead(yaw_val=0)

# while True:
#     pepper.ReadSonar()
#     # laser.get_laser_scan()
#     landmark_info_debug()    



###################################################################### park robot

pepper.InitSonar(False)
# pepper.ExtCollisionProtection("Move",False)
pepper.Crouch()  