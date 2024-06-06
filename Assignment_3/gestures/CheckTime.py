# Choregraphe bezier export in Python.
from naoqi import ALProxy
names = list()
times = list()
keys = list()

names.append("HeadPitch")
times.append([0.76, 2.36, 4.36])
keys.append([[-0.185005, [3, -0.266667, 0], [3, 0.533333, 0]], [0.445059, [3, -0.533333, 0], [3, 0.666667, 0]], [-0.24985, [3, -0.666667, 0], [3, 0, 0]]])

names.append("HeadYaw")
times.append([0.76, 5.16])
keys.append([[0.0104907, [3, -0.266667, 0], [3, 1.46667, 0]], [0.0104907, [3, -1.46667, 0], [3, 0, 0]]])

names.append("HipPitch")
times.append([0.76, 5.16])
keys.append([[-0.0357909, [3, -0.266667, 0], [3, 1.46667, 0]], [-0.0357909, [3, -1.46667, 0], [3, 0, 0]]])

names.append("HipRoll")
times.append([0.76, 5.16])
keys.append([[-0.000594313, [3, -0.266667, 0], [3, 1.46667, 0]], [-0.000594313, [3, -1.46667, 0], [3, 0, 0]]])

names.append("KneePitch")
times.append([0.76, 5.16])
keys.append([[-0.0142155, [3, -0.266667, 0], [3, 1.46667, 0]], [-0.0142155, [3, -1.46667, 0], [3, 0, 0]]])

names.append("LElbowRoll")
times.append([0.76, 2.36, 4.36])
keys.append([[-0.119603, [3, -0.266667, 0], [3, 0.533333, 0]], [-1.47131, [3, -0.533333, 0], [3, 0.666667, 0]], [-0.152026, [3, -0.666667, 0], [3, 0, 0]]])

names.append("LElbowYaw")
times.append([0.76, 2.36, 4.36])
keys.append([[-1.70898, [3, -0.266667, 0], [3, 0.533333, 0]], [0.102974, [3, -0.533333, 0], [3, 0.666667, 0]], [-1.68119, [3, -0.666667, 0], [3, 0, 0]]])

names.append("LHand")
times.append([0.76, 5.16])
keys.append([[0.6942, [3, -0.266667, 0], [3, 1.46667, 0]], [0.6942, [3, -1.46667, 0], [3, 0, 0]]])

names.append("LShoulderPitch")
times.append([0.76, 2.36, 4.36])
keys.append([[1.75742, [3, -0.266667, 0], [3, 0.533333, 0]], [-0.015708, [3, -0.533333, 0], [3, 0.666667, 0]], [1.75279, [3, -0.666667, 0], [3, 0, 0]]])

names.append("LShoulderRoll")
times.append([0.76, 5.16])
keys.append([[0.118376, [3, -0.266667, 0], [3, 1.46667, 0]], [0.118376, [3, -1.46667, 0], [3, 0, 0]]])

names.append("LWristYaw")
times.append([0.76, 5.16])
keys.append([[0.0341748, [3, -0.266667, 0], [3, 1.46667, 0]], [0.0341748, [3, -1.46667, 0], [3, 0, 0]]])

names.append("RElbowRoll")
times.append([0.76, 5.16])
keys.append([[0.100305, [3, -0.266667, 0], [3, 1.46667, 0]], [0.100305, [3, -1.46667, 0], [3, 0, 0]]])

names.append("RElbowYaw")
times.append([0.76, 5.16])
keys.append([[1.69033, [3, -0.266667, 0], [3, 1.46667, 0]], [1.69033, [3, -1.46667, 0], [3, 0, 0]]])

names.append("RHand")
times.append([0.76, 5.16])
keys.append([[0.688049, [3, -0.266667, 0], [3, 1.46667, 0]], [0.688049, [3, -1.46667, 0], [3, 0, 0]]])

names.append("RShoulderPitch")
times.append([0.76, 5.16])
keys.append([[1.74683, [3, -0.266667, 0], [3, 1.46667, 0]], [1.74683, [3, -1.46667, 0], [3, 0, 0]]])

names.append("RShoulderRoll")
times.append([0.76, 5.16])
keys.append([[-0.109908, [3, -0.266667, 0], [3, 1.46667, 0]], [-0.109908, [3, -1.46667, 0], [3, 0, 0]]])

names.append("RWristYaw")
times.append([0.76, 5.16])
keys.append([[-0.0258009, [3, -0.266667, 0], [3, 1.46667, 0]], [-0.0258009, [3, -1.46667, 0], [3, 0, 0]]])

try:
  # uncomment the following line and modify the IP if you use this script outside Choregraphe.
  # motion = ALProxy("ALMotion", IP, 9559)
  motion = ALProxy("ALMotion")
  motion.angleInterpolationBezier(names, times, keys)
except BaseException, err:
  print err
