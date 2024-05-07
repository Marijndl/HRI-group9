import numpy as np


def kalman_filter(mu, sigma, sonar_left, sonar_right, v):
    states = mu.shape[0]

    z = np.array([[sonar_left], [sonar_right]])  # New measurement
    Q = np.array([[np.random.normal(scale=0.1), 0], [0, np.random.normal(scale=0.1)]])  # Measurement noise
    C = np.identity(states)  # Measurement matrix

    # Update parameters using measurement:
    K = sigma * C.T * np.linalg.inv(C * sigma * C.T + Q)  # Kalman gain
    mu = mu + np.dot(K,(z - np.dot(C,mu)))
    sigma = (np.identity(states) - K * C) * sigma

    A = np.identity(states)
    R = np.array([[np.random.normal(scale=0.1), 0], [0, np.random.normal(scale=0.1)]])  # Motion noise
    u = np.array([[v], [v]])
    dt = 0.05
    B = np.array([[-1 * dt, 0], [0, -1 * dt ]])

    # Update parameters with motion model:
    mu = np.dot(A, mu) + np.dot(B,u)
    sigma = A * sigma * A.T + R

    return mu, sigma


if __name__ == "__main__":
    mu = np.array([[2], [4]])
    sigma = np.array([[0.1, 0], [0, 0.1]])
    sonar_left = 3
    sonar_right = 3
    v = 0.75
    mu, sigma = kalman_filter(mu, sigma, sonar_left, sonar_right, v)