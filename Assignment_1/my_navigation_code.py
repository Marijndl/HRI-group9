import math
import numpy as np
import behaviour_based_navigation_love as bn
from definitions import *
import random




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

class scanner:
    def __init__(self):
        self.explore_location = [random.randint(10,40), random.randint(10,30)]

    def scan_world(self, robot, allobstacles, alltargets):
        [sonar_left, sonar_right] = robot.sonar(allobstacles)
        target_distance, target_angle = compute_target_location(robot, alltargets)  # The angle is with respect to the world frame
        # print sonar_left, sonar_right, target_distance, target_angle
        target_angle_robot =  target_angle - robot.phi  # This is the angle relative to the heading direction of the robot.
        explore_angle_robot = math.atan2(self.explore_location[1] - robot.y, self.explore_location[0] - robot.x) - robot.phi
        explore_distance = np.linalg.norm([self.explore_location[0] - robot.x, self.explore_location[1] - robot.y])       


        turn_rate = bn.compute_turnrate(target_distance, target_angle_robot, sonar_left, sonar_right, explore_angle_robot, robot)
        velocity, explore_location  = bn.compute_velocity(target_distance, target_angle_robot, sonar_left, sonar_right, explore_distance, self.explore_location)
        self.explore_location = explore_location
        robot.set_vel(velocity, turn_rate) # the simulated robot does not sidestep

