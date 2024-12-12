import random

arr1 = [3,7,1,0,4]
arr2 = [[2,3],[7,1],[0,4]]
arr3 = [7 for i in range(5)]
arr4 = [i for i in range(1,10)]
arr5 = [i*2 for i in range(1,10)]
arr6 = [random.randint(1,20) for i in range(10)]
arr7 = [[] for i in range(5)]
arr8 = [[1 for i in range(2)] for j in range(4)]
arr9 = [[random.randint(1,20) for i in range(3)] for j in range(5)]

# an array with values: 4,0,3
arr10 = [4,0,3]
print(arr10)

# 15-element array filled with zeros
arr11 = [0 for i in range(15)]
print(arr11)

# an array with integer values in the range of <1,30>
arr12 = [i for i in range(1,31)]
print(arr12)

# 20-element array filled with 0 or 1 randomly
arr13 = [random.randint(0,1) for i in range(20)]
print(arr13)

# two dimensional array with five rows and two columns filled with False
arr14 = [[False for i in range(2)] for j in range(5)]
print(arr14)