import math
import numpy as np
import behaviour_based_navigation_ex2 as bn2
import random

import nao_nocv_2_1 as nao
import time


robot_IP="192.168.0.102"
# robot_IP="127.0.0.1"

nao.InitProxy(robot_IP)
nao.InitPose()
nao.InitSonar(True)
nao.InitLandMark()
nao.InitVideo(resolution_id=2) #[640,480]

sizeX_limits = {"min":[0.22,0.5], "max":[0.45,2.5]}


def landmark_info_debug():
    detected, timestamp, markerInfo=nao.DetectLandMark()
    print(detected,markerInfo)


def look_on_spot():
    """
    scans current view for landmark, if not found, turns around and scans again
    """
    found_bool, xvalue, sizeX = lookltr()
    if found_bool == False: #if not in view, turn around and try again
        nao.Walk(0.,0.,np.pi)
        found_bool, xvalue, sizeX = lookltr()
    return found_bool, xvalue, sizeX

def lookltr(yaw_rate = 0.5):
    """
    look from left to right at `yaw_rate` until landmark is found or can't turn anymore
    """
    yaw_start = 2
    yaw_end = -2
    yaw_counter = yaw_start
    found_bool = False

    start_time = time.time()
    while ((found_bool == False) and (yaw_counter>=yaw_end)):
        #every 2 seconds:
        if time.time() - start_time >= 2:
            nao.MoveHead(yaw_val=yaw_counter)
            found_bool, target_x_location, sizeX = is_target_found()

            print(found_bool, yaw_counter)
            yaw_counter = yaw_counter - yaw_rate #update yaw
            start_time = time.time() #reset timer
    return found_bool, target_x_location, sizeX


def is_target_found():
    detected, _, markerInfo = nao.DetectLandMark()
    if detected:
        return detected, markerInfo[0][1], markerInfo[0][3]
    return detected, 0, 0


def continuously_avoid_obstacles(avoidance_duration = 4, stop = True):
    start_time = time.time()
    while (time.time() - start_time) <= avoidance_duration:
        avoid_obstacle()
    if stop:
        nao.Move(0,0,0)


def walk_towards_target(target_x_location, sizeX, move_duration = 4):
    """
    Aligns body with target and sends Move command, moves 
    for `move_duration` seconds while avoiding obstacles, then stops.
    """
    #align body with target
    nao.Walk(0.,0.,target_x_location) 
    nao.Move(0.3,0.3,0)
    continuously_avoid_obstacles(move_duration, stop=True)


def get_target_distance(sizeX):
    global sizeX_limits
    size_min, dist_min = sizeX_limits["min"]
    size_max, dist_max = sizeX_limits["max"]
    return dist_min + (dist_max - dist_min) * (sizeX - size_min) / (size_max - size_min)


def change_location_random(move_duration = 4):
    dx,dy,theta = get_random_move()
    nao.Walk(0.,0.,theta)
    nao.Move(dx,dy,0)
    #while moving, check obstacles for n seconds (=move for n seconds) and then stop moving 
    continuously_avoid_obstacles(move_duration, stop=True)
    print("@ new random location")
    

def get_random_move():
    dx = random.randint(5,10) * 0.05 
    dy = random.randint(5,10) *0.05
    theta = random.randint(0,314) * 0.01
    print("get_random_move: ",dx,dy, theta)
    return dx,dy, theta


def avoid_obstacle(min_distance=0.3):
    [SL, SR] = nao.ReadSonar()
    SL, SR = round(SL,1), round(SR,1)

    if SL<min_distance and SR<min_distance:
        print("both sonars obstacle - dodging - ", "SL:",SL, "SR:",SR)
        nao.Walk(-min_distance*0.5, 0.,0.)
    elif SL<min_distance:
        print("left sonar obstacle - dodging - ", "SL:",SL, "SR:",SR)
        nao.Walk(0.,-min_distance*0.5,0.)
    elif SR<min_distance:
        print("right sonar obstacle - dodging - ", "SL:",SL, "SR:",SR)
        nao.Walk(0.,min_distance*0.5,0.)
        

def is_obstacle_close(SL,SR, min_distance):
    if SL<min_distance or SR<min_distance:
        return True
    return False


def is_at_target(sizeX, min_distance = 0.5):
    return get_target_distance(sizeX) <= min_distance


###################################################################### execution loops below

found_bool = False
while found_bool == False:
    found_bool, target_x_location, sizeX = look_on_spot()
    print("target found?:", found_bool, target_x_location, sizeX)
    nao.MoveHead(yaw_val=0)
    change_location_random()
    avoid_obstacle()

walk__bool = True
while walk__bool == True:
    if is_at_target(sizeX):
        nao.Move(0.,0.,0.)
        walk__bool = False
    walk_towards_target(target_x_location, sizeX, move_duration=4)  
    found_bool, target_x_location, sizeX = look_on_spot()



nao.InitSonar(False)
nao.Crouch()  