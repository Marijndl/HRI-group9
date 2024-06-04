names = list()
times = list()
keys = list()

names.append("LWristYaw")
times.append([ 1.33333])
keys.append([ [ 0.00052, [ 3, -0.44444, 0.00000], [ 3, 0.00000, 0.00000]]])

names.append("RShoulderPitch")
times.append([ 1.33333, 2.20000, 3.00000, 3.13333, 3.53333, 3.66667])
keys.append([ [ 0.50290, [ 3, -0.44444, 0.00000], [ 3, 0.28889, 0.00000]], [ 0.39095, [ 3, -0.28889, 0.08717], [ 3, 0.26667, -0.08046]], [ 0.00000, [ 3, -0.26667, 0.00000], [ 3, 0.04444, 0.00000]], [ 0.00000, [ 3, -0.04444, 0.00000], [ 3, 0.13333, 0.00000]], [ 0.57421, [ 3, -0.13333, 0.00000], [ 3, 0.04444, 0.00000]], [ 0.57421, [ 3, -0.04444, 0.00000], [ 3, 0.00000, 0.00000]]])

names.append("RShoulderRoll")
times.append([ 1.33333, 2.20000, 3.00000, 3.13333])
keys.append([ [ -0.00873, [ 3, -0.44444, 0.00000], [ 3, 0.28889, 0.00000]], [ -0.00873, [ 3, -0.28889, 0.00000], [ 3, 0.26667, 0.00000]], [ -0.00873, [ 3, -0.26667, 0.00000], [ 3, 0.04444, 0.00000]], [ -0.00873, [ 3, -0.04444, 0.00000], [ 3, 0.00000, 0.00000]]])

names.append("RElbowYaw")
times.append([ 1.33333, 2.20000, 3.00000, 3.13333])
keys.append([ [ 0.00052, [ 3, -0.44444, 0.00000], [ 3, 0.28889, 0.00000]], [ 0.54629, [ 3, -0.28889, -0.04538], [ 3, 0.26667, 0.04189]], [ 0.58818, [ 3, -0.26667, 0.00000], [ 3, 0.04444, 0.00000]], [ 0.58818, [ 3, -0.04444, 0.00000], [ 3, 0.00000, 0.00000]]])

names.append("RElbowRoll")
times.append([ 1.33333, 2.20000, 3.00000, 3.13333, 3.53333, 3.66667])
keys.append([ [ 0.31847, [ 3, -0.44444, 0.00000], [ 3, 0.28889, 0.00000]], [ 1.56207, [ 3, -0.28889, 0.00000], [ 3, 0.26667, 0.00000]], [ 1.56207, [ 3, -0.26667, 0.00000], [ 3, 0.04444, 0.00000]], [ 1.56207, [ 3, -0.04444, 0.00000], [ 3, 0.13333, 0.00000]], [ 1.30900, [ 3, -0.13333, 0.00000], [ 3, 0.04444, 0.00000]], [ 1.30900, [ 3, -0.04444, 0.00000], [ 3, 0.00000, 0.00000]]])

names.append("RWristYaw")
times.append([ 1.33333, 2.20000, 3.00000, 3.13333, 3.53333, 3.66667])
keys.append([ [ 0.00070, [ 3, -0.44444, 0.00000], [ 3, 0.28889, 0.00000]], [ 1.13097, [ 3, -0.28889, 0.00000], [ 3, 0.26667, 0.00000]], [ 0.21468, [ 3, -0.26667, 0.00000], [ 3, 0.04444, 0.00000]], [ 0.21468, [ 3, -0.04444, 0.00000], [ 3, 0.13333, 0.00000]], [ 0.98262, [ 3, -0.13333, 0.00000], [ 3, 0.04444, 0.00000]], [ 0.98262, [ 3, -0.04444, 0.00000], [ 3, 0.00000, 0.00000]]])

names.append("RHand")
times.append([ 1.33333, 2.20000])
keys.append([ [ 0.745, [ 3, -0.44444, 0.00000], [ 3, 0.28889, 0.00000]], [ 0.873, [ 3, -0.28889, 0.00000], [ 3, 0.00000, 0.00000]]])

try:
  motion = ALProxy("ALMotion")
  moveId = motion.post.angleInterpolationBezier(names, times, keys);
except BaseException, err:
  pass
