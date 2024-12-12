# Create a program that calculates and prints 
# the array and the arithmetic mean of array values. 
# Use the “while” loop statement.

arr = [15, 8, 31, 47, 2, 19]
values = 0
i = 0

while i < len(arr):
    values += arr[i]
    i += 1


mean = values/len(arr)

print(mean)

