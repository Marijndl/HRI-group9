import numpy as np
import matplotlib.pyplot as plt


read_data = np.genfromtxt('data.csv', delimiter=',')

sonar_left = read_data[:,0]
sonar_right = read_data[:,1]
sonar_reference = read_data[:,2]

t = np.linspace(0, 0.05*len(sonar_reference), num=len(sonar_reference))

plt.figure()
plt.plot(t, sonar_left, label='Left sonar')
plt.plot(t, sonar_right, label='Right sonar')
plt.plot(t, sonar_reference, label='Reference sonar')
plt.legend()
plt.show()