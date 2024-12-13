# Write a program that draws the function y = sin(x) 
# for an angle value in the range 0-360 degrees.

import matplotlib.pyplot as plt
import numpy as np

x = [i for i in range(0,361)]
y = []
x_radians = [np.radians(i) for i in x] #convert from deegrees to radians

for i in x_radians:
    y.append(np.sin(i))
    
plt.plot(x,y)
plt.show()
