import numpy as np
import matplotlib.pyplot as plt


read_data = np.genfromtxt('data.csv', delimiter=',')

sonar_left = read_data[:,0]
sonar_right = read_data[:,1]
sonar_reference = read_data[:,2]
uncertainty_left = np.abs(read_data[:,3])
uncertainty_right = np.abs(read_data[:,4])

t = np.linspace(0, 0.05*len(sonar_reference), num=len(sonar_reference))

plt.figure()
plt.plot(t, sonar_left, 'o-', label='Left sonar')
plt.plot(t, sonar_right, 'v-', label='Right sonar')
plt.plot(t, sonar_reference, 's-', label='Reference sonar')
plt.xlabel('time (s)')
plt.ylabel('sonar distnace (m)')
plt.legend()
plt.show()