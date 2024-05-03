import math
import numpy as np
import behaviour_based_navigation_ex2 as bn2
from definitions import *

import nao_nocv_2_1 as nao
import time

start_time = time.time() #the whole number, in seconds
timeout_limit = 20 #in seconds
timeout_time = start_time + timeout_limit

robot_IP="192.168.0.104"
nao.InitProxy(robot_IP)
# nao.GoToPosture("Stand")
nao.InitPose()
nao.InitSonar(True)
nao.InitLandMark()




def get_target_angle():
    detected, timestamp, markerInfo=nao.DetectLandMark()
    #bug in nao_nocv_2_1.py -> markerID is [1][0] instead of [0][0] (to fix? ask prof)
    return markerInfo[0][1] #x angle from robot's perspective - is this what `target_angle` means?


last_execution_10 = None
last_execution_05 = None
last_execution_025 = None
while start_time < timeout_time:
    elapsed_time = start_time - time.time() #time so far
    current_execution_10 = round(elapsed_time,1) #10HZ
    current_execution_05 = int(elapsed_time // 2) * 2 #0.5HZ -> every 2 seconds
    current_execution_025 = int(elapsed_time // 4) * 4 #0.25HZ -> every 4 seconds

    #this will execute at a rate of 10Hz
    if current_execution_10 != last_execution_10:
        [SL, SR]=nao.ReadSonar() #meters
        target_angle = get_target_angle() #

        #TODO: implement navigation to target (ask prof: have to use ex2 functions? desc. is confusing)
        #TODO: implement obstacle avoidance

    #this will execute at a rate of 0.5Hz
    if current_execution_05 != current_execution_05:
        nao.Move(0.1,0.,0.) #move 10cm forward
        #nao.Move(0.1,0.,target_angle) #move 10cm toward target? have to clarify meaning 

    last_execution_10 = current_execution_10
    last_execution_05 = current_execution_05
    last_execution_025 = current_execution_025



nao.InitSonar(False)
nao.Crouch()  