# Choregraphe bezier export in Python.
from naoqi import ALProxy
names = list()
times = list()
keys = list()

names.append("HeadPitch")
times.append([1.56])
keys.append([[-0.371755, [3, -0.533333, 0], [3, 0, 0]]])

names.append("HeadYaw")
times.append([0.44, 0.72, 0.96, 1.56, 3.16])
keys.append([[0.132645, [3, -0.16, 0], [3, 0.0933333, 0]], [1.00182, [3, -0.0933333, 0], [3, 0.08, 0]], [0.895354, [3, -0.08, 0], [3, 0.2, 0]], [1.11177, [3, -0.2, 0], [3, 0.533333, 0]], [0, [3, -0.533333, 0], [3, 0, 0]]])

names.append("LElbowRoll")
times.append([0.72, 1.56, 4.76])
keys.append([[-0.666716, [3, -0.253333, 0], [3, 0.28, 0]], [-0.00872665, [3, -0.28, 0], [3, 1.06667, 0]], [-0.506145, [3, -1.06667, 0], [3, 0, 0]]])

names.append("LHand")
times.append([1.56])
keys.append([[0.98, [3, -0.533333, 0], [3, 0, 0]]])

names.append("LShoulderPitch")
times.append([0.96, 1.56, 4.76])
keys.append([[0.476475, [3, -0.333333, 0], [3, 0.2, 0]], [0.476475, [3, -0.2, 0], [3, 1.06667, 0]], [1.61967, [3, -1.06667, 0], [3, 0, 0]]])

names.append("LShoulderRoll")
times.append([0.72, 0.96, 1.56, 3.16, 4.76])
keys.append([[1.18857, [3, -0.253333, 0], [3, 0.08, 0]], [1.3282, [3, -0.08, -0.0139627], [3, 0.2, 0.0349067]], [1.3631, [3, -0.2, 0], [3, 0.533333, 0]], [0.783653, [3, -0.533333, 0.199258], [3, 0.533333, -0.199258]], [0.167552, [3, -0.533333, 0], [3, 0, 0]]])

names.append("LWristYaw")
times.append([1.56, 3.16, 4.76])
keys.append([[-1.82387, [3, -0.533333, 0], [3, 0.533333, 0]], [-1.15541, [3, -0.533333, -0.302524], [3, 0.533333, 0.302524]], [-0.00872665, [3, -0.533333, 0], [3, 0, 0]]])

try:
  # uncomment the following line and modify the IP if you use this script outside Choregraphe.
  # motion = ALProxy("ALMotion", IP, 9559)
  motion = ALProxy("ALMotion")
  motion.angleInterpolationBezier(names, times, keys)
except BaseException, err:
  print err
