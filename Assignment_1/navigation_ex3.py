import math
import numpy as np
import behaviour_based_navigation_ex2 as bn2
import random

import nao_nocv_2_1 as nao
import time

start_time = time.time() #the whole number, in seconds
timeout_limit = 20 #in seconds
timeout_time = start_time + timeout_limit

# robot_IP="192.168.0.102"
# robot_IP="127.0.0.1"

nao.InitProxy(robot_IP)
# nao.GoToPosture("Stand")
nao.InitPose()
nao.InitSonar(True)
nao.InitLandMark()

sizeX_limits = {"min":[0.22,0.5], "max":[0.45,2.5]}

def print_landmark_debug():
    detected, timestamp, markerInfo=nao.DetectLandMark()
    print(detected,markerInfo)

def look_on_spot():
    found_bool, xvalue, sizeX = lookltr()
    if found_bool == False: #if not in view, turn around and try again
        nao.Walk(0.,0.,180)
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
        if current_time - start_time >= 1:
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
        safety_margin = 0.15
        #align with target
        nao.Walk(0.,0.,target_x_location) #how to convert target_x_location to angles?

        target_distance = get_target_distance(sizeX)
        print("target_distance: ",target_distance)
        # nao.Walk(target_distance - safety_margin, 0.,0.)
        nao.Walk(.5, 0.,0.)

    else:
        nao.Move(0.0,0.0,0.0)
    

def get_target_distance(sizeX):
   
    global sizeX_limits
    size_min, dist_min = sizeX_limits["min"]
    size_max, dist_max = sizeX_limits["max"]

    return dist_min + (dist_max - dist_min) * (sizeX - size_min) / (size_max - size_min)


def change_location_random():
    x,y,theta = get_random_walk()
    nao.Walk(0.,0.,theta)
    nao.Walk(x,y,0.)

def get_random_walk():
    x = random.randrange(10) / 20 #get values from 0 to 0.95
    y = random.randrange(10) / 20
    theta = random.randrange(360)
    return x,y, theta

def avoid_obstacle(SL,SR, min_distance):
    if SL<SR:
        if SL<min_distance:
            nao.Walk(0.,-min_distance,0.)
    elif SL>SR:
        if SR<min_distance:
            nao.Walk(0.,min_distance,0.)
    else:
        nao.Walk(-min_distance, 0.,0.)
        #else walk either straight backwards or to a random diagonal backwards

def is_obstacle_close(SL,SR, min_distance):
    if SL<min_distance or SR<min_distance:
        return True
    return False

def is_at_target():
    return get_target_distance() <= 0.5





# finding target
found_bool = False
while found_bool == False:
    # print_landmark_debug()
    found_bool, target_x_location, sizeX = look_on_spot()
    print("target found", found_bool, target_x_location, sizeX)
    # change_location_random()

walk__bool = True
while walk__bool == True:
    walk_to_target(target_x_location, sizeX)
    # if not is_obstacle_close:
    #     walk_to_target(target_x_location, sizeX)
    # else:
    #     walk_to_target(target_x_location, sizeX, is_obstacle_close)
    #     avoid_obstacle()
    if is_at_target():
        nao.Move(0.,0.,0.)
        walk__bool = False
    

#TODO: finish impelemting - rewrite below

# last_execution_10 = None
# last_execution_05 = None
# last_execution_025 = None
# # new_yaw = None
# while start_time < timeout_time:
#     elapsed_time = start_time - time.time() #time so far
#     current_execution_10 = round(elapsed_time,1) #10HZ
#     current_execution_05 = int(elapsed_time // 2) * 2 #0.5HZ -> every 2 seconds
#     current_execution_025 = int(elapsed_time // 4) * 4 #0.25HZ -> every 4 seconds




#     #this will execute at a rate of 10Hz
#     if current_execution_10 != last_execution_10:
#         [SL, SR]=nao.ReadSonar() #meters
#         # target_angle = get_target_angle() #
#         detected, timestamp, markerInfo=nao.DetectLandMark()
#         print(detected,markerInfo)


#         #TODO: implement navigation to target 
#         #TODO: implement obstacle avoidance

#     #this will execute at a rate of 0.25Hz
#     # if current_execution_025 != last_execution_025:
#         # nao.Walk(0.1,0.,0.) #walk 10cm forward
#         # nao.Move(0.1,0.,0) #move 10cm toward target? have to clarify meaning 
#         # nao.Move(0.1,0.,target_angle) #move 10cm toward target? have to clarify meaning 

#     # if current_execution_05 != last_execution_05:
#     #     new_yaw = initial_yaw - 0.25
#     #     looking(detected)

#     last_execution_10 = current_execution_10
#     last_execution_05 = current_execution_05
#     last_execution_025 = current_execution_025



nao.InitSonar(False)
nao.Crouch()  