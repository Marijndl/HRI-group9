import math
import numpy as np
import behaviour_based_navigation_kalman as bn
from definitions import *
import random
from Kalman import kalman_filter


def compute_target_location(robot, alltargets):
    """This function computes the distance to the target and the angle relative to the robot in world coordinates"""
    dist = []
    angle = []
    for tar in alltargets:
        dx = tar.x - robot.x
        dy = tar.y - robot.y
        dist.append(np.linalg.norm([dx, dy]))
        angle.append(math.atan2(dy, dx))
    i = np.argmin(dist)
    return dist[i], angle[i]

class scanner():
    def __init__(self, start_L, start_R):
        self.mu = np.array([[start_L], [start_R]])
        self.sigma = np.array([[0.1, 0],[0, 0.1]])
        
    def scan_world(self, robot, allobstacles, alltargets):
        [sonar_left, sonar_right] = robot.sonar(allobstacles)
        target_distance, target_angle = compute_target_location(robot, alltargets)  # The angle is with respect to the world frame
        # print sonar_left, sonar_right, target_distance, target_angle
        target_angle_robot =  target_angle - robot.phi  # This is the angle relative to the heading direction of the robot.

        turn_rate = bn.compute_turnrate(target_distance, target_angle_robot, sonar_left, sonar_right, robot)
        velocity  = bn.compute_velocity(target_distance, target_angle_robot, sonar_left, sonar_right)
        mu, sigma = kalman_filter(self.mu, self.sigma, sonar_left, sonar_right, velocity)
        self.mu = mu
        self.sigma = sigma
        print(mu, sigma)
        
        robot.set_vel(velocity, turn_rate) # the simulated robot does not sidestep

