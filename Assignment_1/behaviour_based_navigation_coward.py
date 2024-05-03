import math
import random

degree = math.pi/180.0 # radians per degree

def FTarget(target_distance, target_angle):

    #do something useful here
    Ftar=0
    return Ftar

def FObstacle(obs_distance, obs_angle):
    too_far=10 #cm

    if obs_distance < too_far:
        #do something useful here
        Fobs=0 # needs replacing !
    else:
        Fobs=0
    return Fobs

def FStochastic():
    """FStochastic adds noise to the turnrate force. This is just to make the simulation more realistic by adding some noie something useful here"""
    Kstoch=0.03
    
    Fstoch =Kstoch*random.randint(1,100)/100.0
    return Fstoch

def FOrienting(target_angle, target_distance, robot_poss):
    Forient = 0
    if target_distance <= 10:
        if target_angle < 0:
            Forient = math.pi + target_angle
        elif target_angle > 0:
            Forient =  target_angle - math.pi
        else:
            Forient = 0
    
    # Flip robot if near end of map
    if robot_poss.x < 3 or robot_poss.x > 63 or robot_poss.y < 3 or robot_poss.y > 33:
        Forient += math.pi
    
    return Forient

def compute_velocity(target_distance, target_angle_robot, sonar_distance_left, sonar_distance_right):
    max_velocity = 1.0
    max_distance = 0.5 #m
    min_distance = 3 #m

    

    if target_distance > min_distance:
        velocity = (1 / target_distance) * max_velocity * 30
    else:
        velocity = (1 / min_distance) * max_velocity * 100

    return velocity

def compute_turnrate(target_dist, target_angle, sonar_distance_left, sonar_distance_right, robot_poss):
    max_turnrate = 0.349 #rad/s # may need adjustment!

    delta_t = 1 # may need adjustment!
    sonar_angle_left = 30 * degree
    sonar_angle_right = -30 * degree
    
    Fobs_left = FObstacle(sonar_distance_left, sonar_angle_left)
    Fobs_right = FObstacle(sonar_distance_right, sonar_angle_right)

    FTotal = FTarget(target_dist, target_angle) + \
             Fobs_left + \
             Fobs_right + \
             FOrienting(target_angle, target_dist, robot_poss) + \
             FStochastic()
             
    # turnrate: d phi(t) / dt = sum( forces ) 
    turnrate =  FTotal*delta_t
    
    #normalise turnrate value
    if turnrate>max_turnrate:
        turnrate=1.0
    elif -1*turnrate>max_turnrate:
        turnrate=-1.0
    else:
        turnrate=turnrate/max_turnrate

    return turnrate

if __name__=="__main__":
    pass
