# Choregraphe bezier export in Python.
from naoqi import ALProxy
names = list()
times = list()
keys = list()

names.append("LElbowRoll")
times.append([ 0.24000, 0.40000, 0.56000, 0.72000, 0.88000, 1.04000, 1.24000, 1.44000, 1.64000, 1.88000, 2.04000])
keys.append([ [ -0.44328, [ 3, -0.08000, 0.00000], [ 3, 0.05333, 0.00000]], [ -0.44328, [ 3, -0.05333, 0.00000], [ 3, 0.05333, 0.00000]], [ -0.44175, [ 3, -0.05333, 0.00000], [ 3, 0.05333, 0.00000]], [ -0.44328, [ 3, -0.05333, 0.00000], [ 3, 0.05333, 0.00000]], [ -0.43715, [ 3, -0.05333, 0.00000], [ 3, 0.05333, 0.00000]], [ -0.43715, [ 3, -0.05333, 0.00000], [ 3, 0.06667, 0.00000]], [ -0.44175, [ 3, -0.06667, 0.00102], [ 3, 0.06667, -0.00102]], [ -0.44328, [ 3, -0.06667, 0.00000], [ 3, 0.06667, 0.00000]], [ -0.44328, [ 3, -0.06667, 0.00000], [ 3, 0.08000, 0.00000]], [ -0.44328, [ 3, -0.08000, 0.00000], [ 3, 0.05333, 0.00000]], [ -0.44328, [ 3, -0.05333, 0.00000], [ 3, 0.00000, 0.00000]]])

names.append("LElbowYaw")
times.append([ 0.24000, 0.40000, 0.56000, 0.72000, 0.88000, 1.04000, 1.24000, 1.44000, 1.64000, 1.88000, 2.04000])
keys.append([ [ -1.59694, [ 3, -0.08000, 0.00000], [ 3, 0.05333, 0.00000]], [ -1.59694, [ 3, -0.05333, 0.00000], [ 3, 0.05333, 0.00000]], [ -1.59694, [ 3, -0.05333, 0.00000], [ 3, 0.05333, 0.00000]], [ -1.59694, [ 3, -0.05333, 0.00000], [ 3, 0.05333, 0.00000]], [ -1.59694, [ 3, -0.05333, 0.00000], [ 3, 0.05333, 0.00000]], [ -1.59694, [ 3, -0.05333, 0.00000], [ 3, 0.06667, 0.00000]], [ -1.59694, [ 3, -0.06667, 0.00000], [ 3, 0.06667, 0.00000]], [ -1.59694, [ 3, -0.06667, 0.00000], [ 3, 0.06667, 0.00000]], [ -1.59694, [ 3, -0.06667, 0.00000], [ 3, 0.08000, 0.00000]], [ -1.59694, [ 3, -0.08000, 0.00000], [ 3, 0.05333, 0.00000]], [ -1.59694, [ 3, -0.05333, 0.00000], [ 3, 0.00000, 0.00000]]])

names.append("LHand")
times.append([ 0.24000, 0.40000, 0.56000, 0.72000, 0.88000, 1.04000, 1.24000, 1.44000, 1.64000, 1.88000, 2.04000])
keys.append([ [ 0.00028, [ 3, -0.08000, 0.00000], [ 3, 0.05333, 0.00000]], [ 0.00028, [ 3, -0.05333, 0.00000], [ 3, 0.05333, 0.00000]], [ 0.00028, [ 3, -0.05333, 0.00000], [ 3, 0.05333, 0.00000]], [ 0.00028, [ 3, -0.05333, 0.00000], [ 3, 0.05333, 0.00000]], [ 0.00028, [ 3, -0.05333, 0.00000], [ 3, 0.05333, 0.00000]], [ 0.00028, [ 3, -0.05333, 0.00000], [ 3, 0.06667, 0.00000]], [ 0.00028, [ 3, -0.06667, 0.00000], [ 3, 0.06667, 0.00000]], [ 0.00028, [ 3, -0.06667, 0.00000], [ 3, 0.06667, 0.00000]], [ 0.00028, [ 3, -0.06667, 0.00000], [ 3, 0.08000, 0.00000]], [ 0.00028, [ 3, -0.08000, 0.00000], [ 3, 0.05333, 0.00000]], [ 0.00028, [ 3, -0.05333, 0.00000], [ 3, 0.00000, 0.00000]]])

names.append("LShoulderPitch")
times.append([ 0.24000, 0.40000, 0.56000, 0.72000, 0.88000, 1.04000, 1.24000, 1.44000, 1.64000, 1.88000, 2.04000])
keys.append([ [ 1.50635, [ 3, -0.08000, 0.00000], [ 3, 0.05333, 0.00000]], [ 1.50635, [ 3, -0.05333, 0.00000], [ 3, 0.05333, 0.00000]], [ 1.50635, [ 3, -0.05333, 0.00000], [ 3, 0.05333, 0.00000]], [ 1.50635, [ 3, -0.05333, 0.00000], [ 3, 0.05333, 0.00000]], [ 1.51248, [ 3, -0.05333, 0.00000], [ 3, 0.05333, 0.00000]], [ 1.51095, [ 3, -0.05333, 0.00114], [ 3, 0.06667, -0.00142]], [ 1.50481, [ 3, -0.06667, 0.00000], [ 3, 0.06667, 0.00000]], [ 1.50635, [ 3, -0.06667, 0.00000], [ 3, 0.06667, 0.00000]], [ 1.50635, [ 3, -0.06667, 0.00000], [ 3, 0.08000, 0.00000]], [ 1.51555, [ 3, -0.08000, -0.00215], [ 3, 0.05333, 0.00143]], [ 1.51708, [ 3, -0.05333, 0.00000], [ 3, 0.00000, 0.00000]]])

names.append("LShoulderRoll")
times.append([ 0.24000, 0.40000, 0.56000, 0.72000, 0.88000, 1.04000, 1.24000, 1.44000, 1.64000, 1.88000, 2.04000])
keys.append([ [ 0.13955, [ 3, -0.08000, 0.00000], [ 3, 0.05333, 0.00000]], [ 0.12268, [ 3, -0.05333, 0.00153], [ 3, 0.05333, -0.00153]], [ 0.12114, [ 3, -0.05333, 0.00000], [ 3, 0.05333, 0.00000]], [ 0.12268, [ 3, -0.05333, 0.00000], [ 3, 0.05333, 0.00000]], [ 0.12114, [ 3, -0.05333, 0.00000], [ 3, 0.05333, 0.00000]], [ 0.12114, [ 3, -0.05333, 0.00000], [ 3, 0.06667, 0.00000]], [ 0.12114, [ 3, -0.06667, 0.00000], [ 3, 0.06667, 0.00000]], [ 0.12268, [ 3, -0.06667, 0.00000], [ 3, 0.06667, 0.00000]], [ 0.12114, [ 3, -0.06667, 0.00000], [ 3, 0.08000, 0.00000]], [ 0.12421, [ 3, -0.08000, 0.00000], [ 3, 0.05333, 0.00000]], [ 0.12268, [ 3, -0.05333, 0.00000], [ 3, 0.00000, 0.00000]]])

names.append("LWristYaw")
times.append([ 0.24000, 0.40000, 0.56000, 0.72000, 0.88000, 1.04000, 1.24000, 1.44000, 1.64000, 1.88000, 2.04000])
keys.append([ [ 0.02450, [ 3, -0.08000, 0.00000], [ 3, 0.05333, 0.00000]], [ 0.02450, [ 3, -0.05333, 0.00000], [ 3, 0.05333, 0.00000]], [ 0.02450, [ 3, -0.05333, 0.00000], [ 3, 0.05333, 0.00000]], [ 0.02450, [ 3, -0.05333, 0.00000], [ 3, 0.05333, 0.00000]], [ 0.02297, [ 3, -0.05333, 0.00000], [ 3, 0.05333, 0.00000]], [ 0.02450, [ 3, -0.05333, 0.00000], [ 3, 0.06667, 0.00000]], [ 0.02450, [ 3, -0.06667, 0.00000], [ 3, 0.06667, 0.00000]], [ 0.02297, [ 3, -0.06667, 0.00000], [ 3, 0.06667, 0.00000]], [ 0.02450, [ 3, -0.06667, 0.00000], [ 3, 0.08000, 0.00000]], [ 0.02450, [ 3, -0.08000, 0.00000], [ 3, 0.05333, 0.00000]], [ 0.02450, [ 3, -0.05333, 0.00000], [ 3, 0.00000, 0.00000]]])

names.append("RElbowRoll")
times.append([ 0.24000, 0.40000, 0.56000, 0.72000, 0.88000, 1.04000, 1.24000, 1.44000, 1.64000, 1.88000, 2.04000])
keys.append([ [ 0.48172, [ 3, -0.08000, 0.00000], [ 3, 0.05333, 0.00000]], [ 0.22401, [ 3, -0.05333, 0.01534], [ 3, 0.05333, -0.01534]], [ 0.20867, [ 3, -0.05333, 0.00000], [ 3, 0.05333, 0.00000]], [ 0.21634, [ 3, -0.05333, -0.00767], [ 3, 0.05333, 0.00767]], [ 0.69188, [ 3, -0.05333, -0.11454], [ 3, 0.05333, 0.11454]], [ 0.90357, [ 3, -0.05333, -0.08977], [ 3, 0.06667, 0.11221]], [ 1.29781, [ 3, -0.06667, -0.09869], [ 3, 0.06667, 0.09869]], [ 1.49569, [ 3, -0.06667, 0.00000], [ 3, 0.06667, 0.00000]], [ 1.49416, [ 3, -0.06667, 0.00153], [ 3, 0.08000, -0.00184]], [ 1.38678, [ 3, -0.08000, 0.03313], [ 3, 0.05333, -0.02209]], [ 1.32849, [ 3, -0.05333, 0.00000], [ 3, 0.00000, 0.00000]]])

names.append("RElbowYaw")
times.append([ 0.24000, 0.40000, 0.56000, 0.72000, 0.88000, 1.04000, 1.24000, 1.44000, 1.64000, 1.88000, 2.04000])
keys.append([ [ 1.56617, [ 3, -0.08000, 0.00000], [ 3, 0.05333, 0.00000]], [ 2.08567, [ 3, -0.05333, 0.00000], [ 3, 0.05333, 0.00000]], [ 2.08567, [ 3, -0.05333, 0.00000], [ 3, 0.05333, 0.00000]], [ 2.08567, [ 3, -0.05333, 0.00000], [ 3, 0.05333, 0.00000]], [ 2.06933, [ 3, -0.05333, 0.00000], [ 3, 0.05333, 0.00000]], [ 2.06933, [ 3, -0.05333, 0.00000], [ 3, 0.06667, 0.00000]], [ 2.08567, [ 3, -0.06667, 0.00000], [ 3, 0.06667, 0.00000]], [ 2.08567, [ 3, -0.06667, 0.00000], [ 3, 0.06667, 0.00000]], [ 1.94660, [ 3, -0.06667, 0.06848], [ 3, 0.08000, -0.08218]], [ 1.63367, [ 3, -0.08000, 0.00000], [ 3, 0.05333, 0.00000]], [ 1.68889, [ 3, -0.05333, 0.00000], [ 3, 0.00000, 0.00000]]])

names.append("RHand")
times.append([ 0.24000, 0.40000, 0.56000, 0.72000, 0.88000, 1.04000, 1.24000, 1.44000, 1.64000, 1.88000, 2.04000])
keys.append([ [ 0.00034, [ 3, -0.08000, 0.00000], [ 3, 0.05333, 0.00000]], [ 0.00551, [ 3, -0.05333, 0.00000], [ 3, 0.05333, 0.00000]], [ 0.00551, [ 3, -0.05333, 0.00000], [ 3, 0.05333, 0.00000]], [ 0.00551, [ 3, -0.05333, 0.00000], [ 3, 0.05333, 0.00000]], [ 0.00551, [ 3, -0.05333, 0.00000], [ 3, 0.05333, 0.00000]], [ 0.00551, [ 3, -0.05333, 0.00000], [ 3, 0.06667, 0.00000]], [ 0.00551, [ 3, -0.06667, 0.00000], [ 3, 0.06667, 0.00000]], [ 0.00551, [ 3, -0.06667, 0.00000], [ 3, 0.06667, 0.00000]], [ 0.00551, [ 3, -0.06667, 0.00000], [ 3, 0.08000, 0.00000]], [ 0.00543, [ 3, -0.08000, 0.00000], [ 3, 0.05333, 0.00000]], [ 0.00543, [ 3, -0.05333, 0.00000], [ 3, 0.00000, 0.00000]]])

names.append("RShoulderPitch")
times.append([ 0.24000, 0.40000, 0.56000, 0.72000, 0.88000, 1.04000, 1.24000, 1.44000, 1.64000, 1.88000, 2.04000])
keys.append([ [ 1.50490, [ 3, -0.08000, 0.00000], [ 3, 0.05333, 0.00000]], [ 1.40979, [ 3, -0.05333, 0.00000], [ 3, 0.05333, 0.00000]], [ 1.52484, [ 3, -0.05333, -0.00153], [ 3, 0.05333, 0.00153]], [ 1.52637, [ 3, -0.05333, 0.00000], [ 3, 0.05333, 0.00000]], [ 1.48035, [ 3, -0.05333, 0.02020], [ 3, 0.05333, -0.02020]], [ 1.40519, [ 3, -0.05333, 0.02318], [ 3, 0.06667, -0.02898]], [ 1.32388, [ 3, -0.06667, 0.06801], [ 3, 0.06667, -0.06801]], [ 0.99714, [ 3, -0.06667, 0.00000], [ 3, 0.06667, 0.00000]], [ 0.99714, [ 3, -0.06667, 0.00000], [ 3, 0.08000, 0.00000]], [ 0.94805, [ 3, -0.08000, 0.00000], [ 3, 0.05333, 0.00000]], [ 0.96493, [ 3, -0.05333, 0.00000], [ 3, 0.00000, 0.00000]]])

names.append("RShoulderRoll")
times.append([ 0.24000, 0.40000, 0.56000, 0.72000, 0.88000, 1.04000, 1.24000, 1.44000, 1.64000, 1.88000, 2.04000])
keys.append([ [ -0.07674, [ 3, -0.08000, 0.00000], [ 3, 0.05333, 0.00000]], [ -0.23474, [ 3, -0.05333, 0.06085], [ 3, 0.05333, -0.06085]], [ -0.44183, [ 3, -0.05333, 0.08054], [ 3, 0.05333, -0.08054]], [ -0.71795, [ 3, -0.05333, 0.00000], [ 3, 0.05333, 0.00000]], [ -0.57836, [ 3, -0.05333, 0.00000], [ 3, 0.05333, 0.00000]], [ -0.69801, [ 3, -0.05333, 0.03454], [ 3, 0.06667, -0.04318]], [ -0.81153, [ 3, -0.06667, 0.00000], [ 3, 0.06667, 0.00000]], [ -0.06600, [ 3, -0.06667, -0.11198], [ 3, 0.06667, 0.11198]], [ 0.04598, [ 3, -0.06667, -0.03928], [ 3, 0.08000, 0.04714]], [ 0.19324, [ 3, -0.08000, -0.03559], [ 3, 0.05333, 0.02373]], [ 0.22392, [ 3, -0.05333, 0.00000], [ 3, 0.00000, 0.00000]]])

names.append("RWristYaw")
times.append([ 0.24000, 0.40000, 0.56000, 0.72000, 0.88000, 1.04000, 1.24000, 1.44000, 1.64000, 1.88000, 2.04000])
keys.append([ [ 0.02910, [ 3, -0.08000, 0.00000], [ 3, 0.05333, 0.00000]], [ -0.95112, [ 3, -0.05333, 0.00000], [ 3, 0.05333, 0.00000]], [ -0.95112, [ 3, -0.05333, 0.00000], [ 3, 0.05333, 0.00000]], [ -0.95112, [ 3, -0.05333, 0.00000], [ 3, 0.05333, 0.00000]], [ -0.98334, [ 3, -0.05333, 0.00000], [ 3, 0.05333, 0.00000]], [ -0.98334, [ 3, -0.05333, 0.00000], [ 3, 0.06667, 0.00000]], [ -0.95112, [ 3, -0.06667, 0.00000], [ 3, 0.06667, 0.00000]], [ -1.70892, [ 3, -0.06667, 0.00000], [ 3, 0.06667, 0.00000]], [ -1.70892, [ 3, -0.06667, 0.00000], [ 3, 0.08000, 0.00000]], [ -1.69511, [ 3, -0.08000, -0.01381], [ 3, 0.05333, 0.00920]], [ -1.16742, [ 3, -0.05333, 0.00000], [ 3, 0.00000, 0.00000]]])

try:
  # uncomment the following line and modify the IP if you use this script outside Choregraphe.
  # motion = ALProxy("ALMotion", IP, 9559)
  motion = ALProxy("ALMotion")
  motion.angleInterpolationBezier(names, times, keys);
except BaseException, err:
  print err
