import math
import random
import numpy as np

degree = math.pi/180.0 # radians per degree

def FTarget(target_distance, robot_angle, target_angle):
    """"
    Function to adjust robots orientation. Formula F3 is used here.

    Parameters:
    target_distance: Distance to the target.
    robot_angle: Current heading of the robot.
    target_angle: Angle target with respect to the world frame.
        
    """
 
    return -np.exp(-target_distance) * np.sin(robot_angle - target_angle)




def FObstacle(sonar_distance, sonar_angle, robot_angle, sigma_obs=15, beta=3):
    """
    Function to compute repulsive force from obstacles.
    
    Parameters:
        sonar_distance: Distance to obstacle.
        sonar_angle: Angle to the obstacle from the robot's position.
        robot_angle: Current heading of the robot in radians.
        sigma_obs: Sensitivity parameter for angular differences.
        beta: Sensitivity parameter for distance effects.

    """
    too_far=10 #cm

    

    if sonar_distance < too_far:
        angle_diff = robot_angle - sonar_angle
        print angle_diff, sonar_angle 
        force_magnitude = np.exp(-angle_diff**2 / (2 * sigma_obs**2))
        force_magnitude *= angle_diff * np.exp(-sonar_distance / beta)

        return abs(force_magnitude)
    return 0



def FStochastic():
    """FStochastic adds noise to the turnrate force. This is just to make the simulation more realistic by adding some noie something useful here"""
    Kstoch=0.03
    
    Fstoch = Kstoch*random.randint(1,100)/100.0
    return Fstoch

def FOrienting(robot_angle, target_angle):
    """
    Parameters:
    robot_angle: Current angle robot.
    target_angle: Angle to the target with respect to the world frame.
    """

    return -np.sin(robot_angle - target_angle)

def compute_velocity(target_distance, target_angle_robot, sonar_distance_left, sonar_distance_right):
    max_velocity = 1.0
    max_distance = 0.5 #m
    min_distance = 0.2 #m

    if sonar_distance_left>max_distance and sonar_distance_right > max_distance:
        velocity = max_velocity
    elif sonar_distance_left<min_distance or sonar_distance_right < min_distance:
        velocity = 0.0
    elif sonar_distance_left<sonar_distance_right:
        velocity = max_velocity*sonar_distance_left/max_distance
    else:
        velocity = max_velocity*sonar_distance_right/max_distance

    
    return velocity

def compute_turnrate(target_dist, target_angle_robot, sonar_distance_left, sonar_distance_right, robot_angle, target_angle):
    """
    Parameters:
    target_dist: Distance to the target.
    target_angle_robot: Angle to the target from the robot's current position.
    sonar_distance_left: Distance to the left obstacle.
    sonar_distance_right: Distance to the right obstacle.
    robot_angle: Current angle robot.
    target_angle: Angle target with respect to the world frame.
    """

    max_turnrate = 0.349 #rad/s # may need adjustment!
    delta_t = 0.15 # may need adjustment!
    sonar_angle_left = 30 * degree
    sonar_angle_right = -30 * degree

    w_target = 0.5
    w_obstacle = 2.0
    w_orienting =  0.25
    w_stochastic = 0.1

    Fobs_left = -FObstacle(sonar_distance_left, sonar_angle_left, robot_angle)
    Fobs_right = FObstacle(sonar_distance_right, sonar_angle_right, robot_angle)
    
    f_target = w_target * FTarget(target_dist, robot_angle, target_angle)
    f_obs_left = w_obstacle * Fobs_left
    f_obs_right = w_obstacle * Fobs_right
    f_orienting = w_orienting * FOrienting(robot_angle, target_angle)
    f_stochastic = w_stochastic * FStochastic()

    FTotal = f_target + f_obs_left + f_obs_right + f_orienting + f_stochastic
    # turnrate: d phi(t) / dt = sum( forces ) 
    turnrate =  FTotal*delta_t

    #normalise turnrate value
    if abs(turnrate)>max_turnrate:
        turnrate=1.0 * turnrate/abs(turnrate)
    else:
        turnrate=turnrate/max_turnrate
    #print round(sonar_distance_left, 4), round(sonar_distance_right, 4), "Fobs_left:", round(w_obstacle* Fobs_left, 4), "Fobs_right:", round(w_obstacle * Fobs_right, 4), "Ftarget:", round(w_target*FTarget(target_dist, robot_angle, target_angle), 4), "Forienting:", round(w_orienting* FOrienting(robot_angle, target_angle), 4), "Fstochastic:", round(w_stochastic*FStochastic(), 4), "FTotal:", round(FTotal, 4), "turnrate:", round(turnrate, 4), "angle test", round(robot_angle - target_angle, 4), "Robot angle", round(robot_angle, 4)
    #print round(sonar_distance_left, 4), round(sonar_distance_right, 4), "Fobs_left:", round(f_obs_left, 4), "Fobs_right:", round(f_obs_right, 4), "Ftarget:", round(f_target, 4), "Forienting:", round(f_orienting, 4), "Fstochastic:", round(f_stochastic, 4), "FTotal:", round(FTotal, 4), "turnrate:", round(turnrate, 4), "angle test", round(robot_angle - target_angle, 4), "Robot angle", round(robot_angle, 4)
    return turnrate

if __name__=="__main__":
    pass
