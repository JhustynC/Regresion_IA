import numpy as np
import matplotlib.pyplot as plt

#*---------------------------------------------
x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
y = np.array([2, 3.5, 2, 5, 3, 7, 4, 6, 5, 8])
m = len(x)
theta_0 = 0
delta = 0.5  #! Factor de aprendizaje
#*---------------------------------------------

def cost_function(theta, x, y):
    temp = 0
    for i in range(m):
        temp += (theta * x[i] - y[i]) ** 2
    return temp / (2 * m)

def find_theta():
    theta_1 = 0
    cost = cost_function(theta_1, x, y)
    
    while True:
        candidates = [theta_1 + delta, theta_1 - delta]
        new_costs = [cost_function(candidate, x, y) for candidate in candidates]
        
        min_index = np.argmin(new_costs)
        if new_costs[min_index] < cost:
            theta_1 = candidates[min_index]
            cost = new_costs[min_index]
        else:
            break
    
    return theta_1

xs = np.arange(-5, 5, step=delta)
ys = [cost_function(theta, x, y) for theta in xs]
theta_1 = find_theta()

#----Parametros para grafica-----
plt.figure(figsize=(10, 8))
plt.subplot(2, 1, 1)
plt.scatter(x, y)
h = lambda x: theta_1 * x + theta_0
plt.plot(x, h(x), color='red')
plt.subplot(2, 1, 2)
plt.plot(xs, ys)
plt.scatter(xs[np.argmin(ys)], min(ys), color='green')
plt.show()
