import math
import numpy as np
import behaviour_based_navigation_ex2 as bn2
import random

import nao_nocv_2_1 as nao
import time



###################################################################### initialization

robot_IP="192.168.0.112"
# robot_IP="127.0.0.1"

nao.InitProxy(robot_IP)
nao.InitPose()
nao.InitSonar(True)
nao.InitLandMark()
nao.InitVideo(resolution_id=2) # 2 = [640,480]

sizeY_limits_a4 = {"min":[0.28,0.45], "max":[0.073,1.9]}
# sizeY_limits_a4 = {"min":[0.45,0.5], "max":[0.22,2.5]}


###################################################################### function definitions

def landmark_info_debug():
    detected, timestamp, markerInfo=nao.DetectLandMark()
    print(detected,markerInfo)


def look_on_spot():
    """
    scans current view for landmark, if not found, turns around and scans again
    """
    found_bool, xvalue, sizeY, current_yaw, yaw_rate = lookltr()
    # if found_bool == False: #if not in view, turn around and try again
    #     nao.Walk(0.,0.,np.pi)
    #     found_bool, xvalue, sizeY, current_yaw = lookltr()
    return found_bool, xvalue, sizeY, current_yaw, yaw_rate

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
        # print(landmark_info_debug())
        
        #every 2 seconds:
        if time.time() - start_time >= 2:
            nao.MoveHead(yaw_val=yaw_counter)
            time.sleep(1)
            found_bool, target_x_location, sizeY = is_target_found()

            print(found_bool, yaw_counter)
            yaw_counter = yaw_counter - yaw_rate #update yaw
            start_time = time.time() #reset timer

    print("YAW, X VAL, CALC.:",yaw_counter+yaw_rate, target_x_location,yaw_counter+yaw_rate+target_x_location )
    return found_bool, target_x_location, sizeY, yaw_counter, yaw_rate


def is_target_found():
    detected, _, markerInfo = nao.DetectLandMark()
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
        nao.Move(0,0,0)


def walk_towards_target(target_x_location, sizeY,current_yaw, move_duration = 4, stop = True):
    """
    Aligns body with target and sends Move command, moves 
    for `move_duration` seconds while avoiding obstacles, then stops by default.
    """
    #align body with target
    print("yaw, target x, +", current_yaw, target_x_location,current_yaw+target_x_location)
    raw_input("waiting - press enter")
    nao.Walk(0.,0.,current_yaw+target_x_location) 
    nao.Move(0.6,0.6,0)
    continuously_avoid_obstacles(move_duration, stop=stop)


def get_target_distance(sizeY):
    """
    interpolate landmark distance from sizeY of landmark (assumes no sizeY deformations)
    """
    global sizeY_limits_a4
    size_min, dist_min = sizeY_limits_a4["min"]
    # print(size_min, dist_min)
    size_max, dist_max = sizeY_limits_a4["max"]
    # print(size_max, dist_max)
    # return dist_min + (sizeY - size_min) * (dist_max - dist_min) / (size_max - size_min)
    return 1/((sizeY-size_max)/(size_min-size_max)) * (dist_max - dist_min) + dist_min


def change_location_random(move_duration = 4, stop = True):
    dx,dy,theta = get_random_move()
    nao.Walk(0.,0.,theta)
    nao.Move(dx,dy,0)
    #while moving, check obstacles for n seconds (=move for n seconds) and then stop moving 
    continuously_avoid_obstacles(move_duration, stop=stop)
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


def is_at_target(sizeY, min_distance = 0.2):
    print("distance: ",get_target_distance(sizeY))
    return get_target_distance(sizeY) <= min_distance


###################################################################### execution loop

# while True:
#     landmark_info_debug()
# found_bool, target_x_location, sizeY, current_yaw = look_on_spot()
# print("am I close?",is_at_target(sizeY))
# while is_at_target(sizeY) == False:
#     if found_bool:
#         print("found!")
#         walk_towards_target(target_x_location, sizeY, current_yaw, move_duration=4, stop = True)
#     else:
#         change_location_random(move_duration=4, stop = True) 
#     found_bool, target_x_location, sizeY, current_yaw = look_on_spot()
#     nao.MoveHead(yaw_val=0)



# found_bool = False
# while found_bool == False:
#     found_bool, target_x_location, sizeY, current_yaw, yaw_rate = look_on_spot()
# dist = get_target_distance(sizeY)
# print("dist:",dist)
# # time.sleep(2)
# nao.Walk(0,0,current_yaw+target_x_location+yaw_rate)
# nao.Walk(dist-0.1,0,0)

while True:
    # landmark_info_debug()
    detected, _, markerInfo = nao.DetectLandMark()
    try:
        print("Y, DIST:",get_target_distance(markerInfo[0][4]))
    except:
        pass
###################################################################### park robot

nao.InitSonar(False)
nao.Crouch()  