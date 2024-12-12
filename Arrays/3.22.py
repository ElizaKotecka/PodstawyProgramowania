# Define a function rand_elem(array) that returns 
# a randomly selected array element. 
# Using the function, print a few randomly selected array elements.

import random

def rand_elem(array):
    return random.choice(array)

array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(rand_elem(array))
print(rand_elem(array))
print(rand_elem(array))