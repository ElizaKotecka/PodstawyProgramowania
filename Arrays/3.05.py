# An array contains values: 15, 8, 31, 47, 2, 19.
# Create a program that calculates and prints the array 
# and the arithmetic mean of array values. 
# Use the “for” loop statement.

arr = [15, 8, 31, 47, 2, 19]

sum = 0
for i in arr:
    sum += i
    print(i, end=' ')
print()
mean = sum / len(arr)
print(f'Arithmetic mean: {mean:.2f}')  