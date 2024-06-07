# Choregraphe bezier export in Python.
from naoqi import ALProxy
names = list()
times = list()
keys = list()

names.append("HeadPitch")
times.append([0.92, 2.52, 4.96])
keys.append([[-0.381962, [3, -0.32, 0], [3, 0.533333, 0]], [-0.237767, [3, -0.533333, 0], [3, 0.813333, 0]], [-0.341185, [3, -0.813333, 0], [3, 0, 0]]])

names.append("HeadYaw")
times.append([0.92, 2.52, 4.96])
keys.append([[0.0184078, [3, -0.32, 0], [3, 0.533333, 0]], [-1.13373, [3, -0.533333, 0], [3, 0.813333, 0]], [0.0591846, [3, -0.813333, 0], [3, 0, 0]]])

names.append("HipPitch")
times.append([0.92, 4.96])
keys.append([[-0.0357292, [3, -0.32, 0], [3, 1.34667, 0]], [0.00504772, [3, -1.34667, 0], [3, 0, 0]]])

names.append("HipRoll")
times.append([0.92, 4.96])
keys.append([[-3.50031e-07, [3, -0.32, 0], [3, 1.34667, 0]], [0.0407765, [3, -1.34667, 0], [3, 0, 0]]])

names.append("KneePitch")
times.append([0.92, 4.96])
keys.append([[-0.0110562, [3, -0.32, 0], [3, 1.34667, 0]], [0.0297206, [3, -1.34667, 0], [3, 0, 0]]])

names.append("LElbowRoll")
times.append([0.92, 4.96])
keys.append([[-0.113438, [3, -0.32, 0], [3, 1.34667, 0]], [-0.0726614, [3, -1.34667, 0], [3, 0, 0]]])

names.append("LElbowYaw")
times.append([0.92, 4.96])
keys.append([[-1.71877, [3, -0.32, 0], [3, 1.34667, 0]], [-1.678, [3, -1.34667, 0], [3, 0, 0]]])

names.append("LHand")
times.append([0.92, 4.96])
keys.append([[0.6942, [3, -0.32, 0], [3, 1.34667, 0]], [3.03054, [3, -1.34667, 0], [3, 0, 0]]])

names.append("LShoulderPitch")
times.append([0.92, 4.96])
keys.append([[1.76561, [3, -0.32, 0], [3, 1.34667, 0]], [1.80639, [3, -1.34667, 0], [3, 0, 0]]])

names.append("LShoulderRoll")
times.append([0.92, 4.96])
keys.append([[0.104679, [3, -0.32, 0], [3, 1.34667, 0]], [0.145455, [3, -1.34667, 0], [3, 0, 0]]])

names.append("LWristYaw")
times.append([0.92, 4.96])
keys.append([[0.0328401, [3, -0.32, 0], [3, 1.34667, 0]], [0.073617, [3, -1.34667, 0], [3, 0, 0]]])

names.append("RElbowRoll")
times.append([0.92, 2.52, 4.96])
keys.append([[0.102678, [3, -0.32, 0], [3, 0.533333, 0]], [0.493433, [3, -0.533333, 0], [3, 0.813333, 0]], [0.143455, [3, -0.813333, 0], [3, 0, 0]]])

names.append("RElbowYaw")
times.append([0.92, 2.56, 4.96])
keys.append([[1.69289, [3, -0.32, 0], [3, 0.546667, 0]], [2.07704, [3, -0.546667, 0], [3, 0.8, 0]], [1.73367, [3, -0.8, 0], [3, 0, 0]]])

names.append("RHand")
times.append([0.92, 2.52, 4.96])
keys.append([[0.688049, [3, -0.32, 0], [3, 0.533333, 0]], [0.150803, [3, -0.533333, 0], [3, 0.813333, 0]], [3.02439, [3, -0.813333, 0], [3, 0, 0]]])

names.append("RShoulderPitch")
times.append([0.92, 2.52, 4.96])
keys.append([[1.74495, [3, -0.32, 0], [3, 0.533333, 0]], [1.34719, [3, -0.533333, 0], [3, 0.813333, 0]], [1.78573, [3, -0.813333, 0], [3, 0, 0]]])

names.append("RShoulderRoll")
times.append([0.92, 2.52, 4.96])
keys.append([[-0.104726, [3, -0.32, 0], [3, 0.533333, 0]], [-1.10212, [3, -0.533333, 0], [3, 0.813333, 0]], [-0.0639488, [3, -0.813333, 0], [3, 0, 0]]])

names.append("RWristYaw")
times.append([0.92, 2.52, 4.96])
keys.append([[-0.022564, [3, -0.32, 0], [3, 0.533333, 0]], [1.83862, [3, -0.533333, 0], [3, 0.813333, 0]], [0.0182128, [3, -0.813333, 0], [3, 0, 0]]])

try:
  # uncomment the following line and modify the IP if you use this script outside Choregraphe.
  # motion = ALProxy("ALMotion", IP, 9559)
  motion = ALProxy("ALMotion")
  motion.angleInterpolationBezier(names, times, keys)
except BaseException, err:
  print err
