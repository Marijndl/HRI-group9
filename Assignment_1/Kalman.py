import numpy as np

def kalman_filter(mu, sigma, sonar_left, sonar_right):
    states = mu.shape[0]
   
    z = np.array([[sonar_left], [sonar_right]])                                         #New measurement
    Q = np.array([[np.random.normal(scale=0.1), 0],[0, np.random.normal(scale=0.1)]])   #Measurement noise
    C = np.identity(states)                                                             #Measurement matrix
    
    #Update parameters using measurement
    K = sigma * C.T * np.inverse(C * sigma * C.T + Q)                                   #Kalman gain
    mu = mu + K * (z - C * mu)
    sigma = (np.identity(states) - K * C) * sigma

