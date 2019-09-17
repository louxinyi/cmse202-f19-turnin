
import math
import numpy as np
import random
import matplotlib.pyplot as plt

N_points = 16
points_in = 0
points_out = 0
plt.figure(figsize=(5,5))

for loop in range(N_points):
	x = random.uniform(-1,1)
	y = random.uniform(-1,1)
	if x**2 +y**2 > (0.5)**2 and x**2 + y**2 <1:
		plt.scatter(x,y,color = "g")
		points_in += 1
	else:
		plt.scatter(x,y,color='g')
		points_out -= 1

r1 = 0.5
r2 = 1
a, b = (0.,0.)
theta = np.arange(0, 2 * np.pi,0.01)
x1 = a + r1 * np.cos(theta)
y1 = b + r1 * np.sin(theta)
x2 = a + r2 * np.cos(theta)
y2 = b + r2 * np.sin(theta)
plt.plot(x1, y1,'b')
plt.plot(x2, y2,'b')
plt.axis('equal')

my_area = points_in/N_points
true_area = (math.pi*(1-0.5**2))/2**2
print("My area is:", np.round(my_area,2))
print("The real area is:" ,np.round(true_area,2))
print("The error value is:", abs(my_area - true_area)/true_area)

