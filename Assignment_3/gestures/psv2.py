# Choregraphe bezier export in Python.
from naoqi import ALProxy
names = list()
times = list()
keys = list()

names.append("LElbowRoll")
times.append([0.48, 4.88, 7.92, 8.6, 9.24, 10.28, 10.76, 15.04, 15.96])
keys.append([[-0.551524, [3, -0.173333, 0], [3, 1.46667, 0]], [-0.792379, [3, -1.46667, 0], [3, 1.01333, 0]], [-0.792379, [3, -1.01333, 0], [3, 0.226667, 0]], [-0.792379, [3, -0.226667, 0], [3, 0.213333, 0]], [-0.792379, [3, -0.213333, 0], [3, 0.346667, 0]], [-0.792379, [3, -0.346667, 0], [3, 0.16, 0]], [-0.792379, [3, -0.16, 0], [3, 1.42667, 0]], [-0.802851, [3, -1.42667, 0], [3, 0.306667, 0]], [-0.802851, [3, -0.306667, 0], [3, 0, 0]]])

names.append("LElbowYaw")
times.append([0.48, 4.88, 7.92, 8.6, 9.24, 10.28, 10.76, 15.04, 15.96])
keys.append([[-1.5132, [3, -0.173333, 0], [3, 1.46667, 0]], [-0.914553, [3, -1.46667, 0], [3, 1.01333, 0]], [-0.914553, [3, -1.01333, 0], [3, 0.226667, 0]], [-0.914553, [3, -0.226667, 0], [3, 0.213333, 0]], [-0.914553, [3, -0.213333, 0], [3, 0.346667, 0]], [-0.914553, [3, -0.346667, 0], [3, 0.16, 0]], [-0.914553, [3, -0.16, 0], [3, 1.42667, 0]], [-0.914553, [3, -1.42667, 0], [3, 0.306667, 0]], [-1.33169, [3, -0.306667, 0], [3, 0, 0]]])

names.append("LHand")
times.append([0.48, 4.88, 7.92, 8.6, 9.24, 10.28, 10.76, 15.04, 15.96])
keys.append([[0.02, [3, -0.173333, 0], [3, 1.46667, 0]], [0.85, [3, -1.46667, 0], [3, 1.01333, 0]], [0.85, [3, -1.01333, 0], [3, 0.226667, 0]], [0.85, [3, -0.226667, 0], [3, 0.213333, 0]], [0.85, [3, -0.213333, 0], [3, 0.346667, 0]], [0.85, [3, -0.346667, 0], [3, 0.16, 0]], [0.85, [3, -0.16, 0], [3, 1.42667, 0]], [0.85, [3, -1.42667, 0], [3, 0.306667, 0]], [0.85, [3, -0.306667, 0], [3, 0, 0]]])

names.append("LShoulderPitch")
times.append([0.48, 4.88, 7.92, 8.6, 9.24, 10.28, 10.76, 15.04, 15.96])
keys.append([[1.7558, [3, -0.173333, 0], [3, 1.46667, 0]], [0.733038, [3, -1.46667, 0], [3, 1.01333, 0]], [0.733038, [3, -1.01333, 0], [3, 0.226667, 0]], [0.733038, [3, -0.226667, 0], [3, 0.213333, 0]], [0.733038, [3, -0.213333, 0], [3, 0.346667, 0]], [0.733038, [3, -0.346667, 0], [3, 0.16, 0]], [0.733038, [3, -0.16, 0], [3, 1.42667, 0]], [0.127409, [3, -1.42667, 0], [3, 0.306667, 0]], [0.127409, [3, -0.306667, 0], [3, 0, 0]]])

names.append("LShoulderRoll")
times.append([0.48, 4.88, 7.92, 8.6, 9.24, 10.28, 10.76, 15.04, 15.96])
keys.append([[0.195477, [3, -0.173333, 0], [3, 1.46667, 0]], [0.242601, [3, -1.46667, 0], [3, 1.01333, 0]], [0.242601, [3, -1.01333, 0], [3, 0.226667, 0]], [0.242601, [3, -0.226667, 0], [3, 0.213333, 0]], [0.242601, [3, -0.213333, 0], [3, 0.346667, 0]], [0.242601, [3, -0.346667, 0], [3, 0.16, 0]], [0.242601, [3, -0.16, 0], [3, 1.42667, 0]], [0.383972, [3, -1.42667, 0], [3, 0.306667, 0]], [0.383972, [3, -0.306667, 0], [3, 0, 0]]])

names.append("LWristYaw")
times.append([0.48, 4.88, 7.92, 8.6, 9.24, 10.28, 10.76, 15.04, 15.96])
keys.append([[-0.176278, [3, -0.173333, 0], [3, 1.46667, 0]], [-0.176278, [3, -1.46667, 0], [3, 1.01333, 0]], [-0.176278, [3, -1.01333, 0], [3, 0.226667, 0]], [-0.176278, [3, -0.226667, 0], [3, 0.213333, 0]], [-0.176278, [3, -0.213333, 0], [3, 0.346667, 0]], [-0.176278, [3, -0.346667, 0], [3, 0.16, 0]], [-0.176278, [3, -0.16, 0], [3, 1.42667, 0]], [-0.176278, [3, -1.42667, 0], [3, 0.306667, 0]], [-0.176278, [3, -0.306667, 0], [3, 0, 0]]])

names.append("RElbowRoll")
times.append([7.92, 8.6, 9.24, 10.28, 10.76, 11.28, 15.04, 15.96])
keys.append([[1.11701, [3, -2.65333, 0], [3, 0.226667, 0]], [0.980875, [3, -0.226667, 0], [3, 0.213333, 0]], [1.11701, [3, -0.213333, 0], [3, 0.346667, 0]], [0.909317, [3, -0.346667, 1.44255e-07], [3, 0.16, -6.6579e-08]], [0.909316, [3, -0.16, 6.6579e-08], [3, 0.173333, -7.21273e-08]], [0.612611, [3, -0.173333, 0], [3, 1.25333, 0]], [0.909316, [3, -1.25333, 0], [3, 0.306667, 0]], [0.909316, [3, -0.306667, 0], [3, 0, 0]]])

names.append("RElbowYaw")
times.append([0.48, 4.88, 7.92, 8.6, 9.24, 10.28, 10.76, 15.04, 15.96])
keys.append([[1.13446, [3, -0.173333, 0], [3, 1.46667, 0]], [1.13446, [3, -1.46667, 0], [3, 1.01333, 0]], [0.621337, [3, -1.01333, 0], [3, 0.226667, 0]], [0.849975, [3, -0.226667, 0], [3, 0.213333, 0]], [0.621337, [3, -0.213333, 0], [3, 0.346667, 0]], [1.20777, [3, -0.346667, 0], [3, 0.16, 0]], [1.20777, [3, -0.16, 0], [3, 1.42667, 0]], [1.20777, [3, -1.42667, 0], [3, 0.306667, 0]], [1.50447, [3, -0.306667, 0], [3, 0, 0]]])

names.append("RHand")
times.append([0.48, 4.88, 7.92, 8.6, 9.24, 10.28, 10.76, 15.04, 15.96])
keys.append([[0.32, [3, -0.173333, 0], [3, 1.46667, 0]], [0.66, [3, -1.46667, 0], [3, 1.01333, 0]], [0.34, [3, -1.01333, 0], [3, 0.226667, 0]], [0.82, [3, -0.226667, 0], [3, 0.213333, 0]], [0.68, [3, -0.213333, 0], [3, 0.346667, 0]], [0.68, [3, -0.346667, 0], [3, 0.16, 0]], [0.68, [3, -0.16, 0], [3, 1.42667, 0]], [0.68, [3, -1.42667, 0], [3, 0.306667, 0]], [0.68, [3, -0.306667, 0], [3, 0, 0]]])

names.append("RShoulderPitch")
times.append([0.48, 4.88, 7.92, 8.6, 9.24, 10.28, 10.76, 15.04, 15.96])
keys.append([[0.911062, [3, -0.173333, 0], [3, 1.46667, 0]], [0.911062, [3, -1.46667, 0], [3, 1.01333, 0]], [-0.31765, [3, -1.01333, 0.179461], [3, 0.226667, -0.0401426]], [-0.357792, [3, -0.226667, 0], [3, 0.213333, 0]], [-0.31765, [3, -0.213333, -0.0401426], [3, 0.346667, 0.0652317]], [0.162316, [3, -0.346667, 0], [3, 0.16, 0]], [0.162316, [3, -0.16, 0], [3, 1.42667, 0]], [0.188496, [3, -1.42667, -7.74343e-08], [3, 0.306667, 1.66448e-08]], [0.188496, [3, -0.306667, 0], [3, 0, 0]]])

names.append("RShoulderRoll")
times.append([0.48, 4.88, 7.92, 8.6, 9.24, 10.28, 10.76, 15.04, 15.96])
keys.append([[-0.464258, [3, -0.173333, 0], [3, 1.46667, 0]], [-0.464258, [3, -1.46667, 0], [3, 1.01333, 0]], [-0.532325, [3, -1.01333, 0.0427887], [3, 0.226667, -0.00957116]], [-0.621337, [3, -0.226667, 0], [3, 0.213333, 0]], [-0.532325, [3, -0.213333, -0.0542991], [3, 0.346667, 0.0882361]], [-0.193732, [3, -0.346667, 0], [3, 0.16, 0]], [-0.193732, [3, -0.16, 0], [3, 1.42667, 0]], [-0.42237, [3, -1.42667, 1.54869e-07], [3, 0.306667, -3.32895e-08]], [-0.42237, [3, -0.306667, 0], [3, 0, 0]]])

names.append("RWristYaw")
times.append([0.48, 4.88, 7.92, 8.6, 9.24, 10.28, 10.76, 15.04, 15.96])
keys.append([[1.52891, [3, -0.173333, 0], [3, 1.46667, 0]], [0.371755, [3, -1.46667, 0.212195], [3, 1.01333, -0.146608]], [0.225147, [3, -1.01333, 0.0741671], [3, 0.226667, -0.01659]], [0.0994838, [3, -0.226667, 0], [3, 0.213333, 0]], [0.225147, [3, -0.213333, -0.0660455], [3, 0.346667, 0.107324]], [0.619592, [3, -0.346667, -1.44255e-07], [3, 0.16, 6.6579e-08]], [0.619592, [3, -0.16, 0], [3, 1.42667, 0]], [0.00523599, [3, -1.42667, 0], [3, 0.306667, 0]], [0.00523599, [3, -0.306667, 0], [3, 0, 0]]])

try:
  # uncomment the following line and modify the IP if you use this script outside Choregraphe.
  # motion = ALProxy("ALMotion", IP, 9559)
  motion = ALProxy("ALMotion")
  motion.angleInterpolationBezier(names, times, keys)
except BaseException, err:
  print err
