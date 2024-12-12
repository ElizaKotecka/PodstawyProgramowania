# Write a program that draws the function y = sin(x) 
# for an angle value in the range 0-360 degrees.

import matplotlib.pyplot as plt
import numpy as np

x = [i for i in range(0,361)]
y = []

for i in range(len(x)):
    y.append(np.sin(np.radians(x[i]))) #from deegrees to radiants
    
plt.plot(x,y)
plt.show()
