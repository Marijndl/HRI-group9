import math
import numpy as np
import behaviour_based_navigation_ex2 as bn2
import random

import nao_nocv_2_1 as nao
import time

start_time = time.time() #the whole number, in seconds
timeout_limit = 20 #in seconds
timeout_time = start_time + timeout_limit

robot_IP="192.168.0.102"
# robot_IP="127.0.0.1"

nao.InitProxy(robot_IP)
# nao.GoToPosture("Stand")
nao.InitPose()
nao.InitSonar(True)
nao.InitLandMark()
nao.InitVideo(resolution_id=2) #[640,480]

sizeX_limits = {"min":[0.22,0.5], "max":[0.45,2.5]}

def print_landmark_debug():
    detected, timestamp, markerInfo=nao.DetectLandMark()
    print(detected,markerInfo)

def look_on_spot():
    found_bool, xvalue, sizeX = lookltr()
    if found_bool == False: #if not in view, turn around and try again
        nao.Walk(0.,0.,np.pi)
        found_bool, xvalue, sizeX = lookltr()
    return found_bool, xvalue, sizeX

def lookltr():
    yaw_start = 2
    yaw_end = -2
    yaw_counter = yaw_start
    yaw_rate = 0.5
    found_bool = False

    start_time = time.time()
    while ((found_bool == False) and (yaw_counter>=yaw_end)):
        # print_landmark_debug()
        current_time = time.time()
        if current_time - start_time >= 2:
            start_time = current_time
            nao.MoveHead(yaw_val=yaw_counter)
            found_bool, target_x_location, sizeX = is_target_found()
            print(found_bool, yaw_counter,yaw_counter>=yaw_end)
            yaw_counter = yaw_counter - yaw_rate
        

    return found_bool, target_x_location, sizeX


def is_target_found():
    detected, _, markerInfo = nao.DetectLandMark()
    if detected:
        return detected, markerInfo[0][1], markerInfo[0][3]
    return detected, 0, 0


def walk_to_target(target_x_location, sizeX, toggle=True):
    """
    walk to target by aligning, calculating distance, and walking said distance forward

    toggle parameter for use in loops - can stop robot if `False`
    """
    if toggle:
        safety_margin = 0.25
        #align body with target
        nao.Walk(0.,0.,target_x_location) 
        target_distance = get_target_distance(sizeX)
        print("target_distance: ",target_distance)
        nao.Walk(target_distance - safety_margin, 0.,0.)
        is_obstacle_close()

    else:
        nao.Move(0.0,0.0,0.0)
    

def get_target_distance(sizeX):
   
    global sizeX_limits
    size_min, dist_min = sizeX_limits["min"]
    size_max, dist_max = sizeX_limits["max"]

    return dist_min + (dist_max - dist_min) * (sizeX - size_min) / (size_max - size_min)


def change_location_random(walk_time = 4, avoid_obstacles = True):
    dx,dy,theta = get_random_move()
    nao.Walk(0.,0.,theta)
    nao.Move(dx,dy,0)
    #walk (& check obstacles) for n seconds and then stop moving 
    start_time = time.time()
    while (time.time() - start_time) <= walk_time:
        if avoid_obstacles:
            avoid_obstacle()
    nao.Move(0,0,0)
    print("moved to new location")
    

def get_random_move():
    dx = random.randint(5,10) * 0.05 
    dy = random.randint(5,10) *0.05
    theta = random.randint(0,314) * 0.01
    print("get_random_move: ",dx,dy, theta)
    return dx,dy, theta

def avoid_obstacle(min_distance=0.3, max_distance=0.6):
    [SL, SR]=nao.ReadSonar()
    SL, SR = round(SL,1), round(SR,1)
    if SL<SR:
        if SL<min_distance:
            print("left sonar obstacle - dodging - ", "SL:",SL, "SR:",SR)
            nao.Walk(0.,-min_distance*0.5,0.)
    elif SL>SR:
        if SR<min_distance:
            print("right sonar obstacle - dodging - ", "SL:",SL, "SR:",SR)
            nao.Walk(0.,min_distance*0.5,0.)
    elif SL<min_distance and SR<min_distance:
        print("both sonar obstacle - dodging - ", "SL:",SL, "SR:",SR)
        nao.Walk(-min_distance*0.5, 0.,0.)
        #else walk either straight backwards or to a random diagonal backwards

def is_obstacle_close(SL,SR, min_distance):
    if SL<min_distance or SR<min_distance:
        return True
    return False

def is_at_target(sizeX):
    return get_target_distance(sizeX) <= 0.5


###################################################################### execution loops below

found_bool = False
while found_bool == False:
    # print_landmark_debug()
    # found_bool, target_x_location, sizeX = look_on_spot()
    # print("target found", found_bool, target_x_location, sizeX)
    nao.MoveHead(yaw_val=0)
    # change_location_random()
    avoid_obstacle()


walk__bool = True
while walk__bool == True:
    walk_to_target(target_x_location, sizeX)    
    # if not is_obstacle_close:
    #     walk_to_target(target_x_location, sizeX)
    # else:
    #     walk_to_target(target_x_location, sizeX, is_obstacle_close)
    #     avoid_obstacle()
    if is_at_target(sizeX):
        nao.Move(0.,0.,0.)
        walk__bool = False



nao.InitSonar(False)
nao.Crouch()  