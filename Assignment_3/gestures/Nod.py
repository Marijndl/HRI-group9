# Choregraphe bezier export in Python.
from naoqi import ALProxy
names = list()
times = list()
keys = list()

names.append("HeadPitch")
times.append([0.36, 0.96])
keys.append([[0.612605, [3, -0.133333, 0], [3, 0.2, 0]], [-0.37378, [3, -0.2, 0], [3, 0, 0]]])

names.append("HeadYaw")
times.append([0.96])
keys.append([[0.0171917, [3, -0.333333, 0], [3, 0, 0]]])

try:
  # uncomment the following line and modify the IP if you use this script outside Choregraphe.
  # motion = ALProxy("ALMotion", IP, 9559)
  motion = ALProxy("ALMotion")
  motion.angleInterpolationBezier(names, times, keys)
except BaseException, err:
  print err
