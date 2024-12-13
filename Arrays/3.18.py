# Create a module MyArrays containing functions  to operate on an array of numbers.

# Then, write a program that for the sequence of numbers:

# 7,3,8,5,2
# calculates and prints results. Sample result:

# Numbers: 7,3,8,5,2
# Second largest number: 7 
# Median: 5
# Smallest and largest number: 2,8
# Numbers as a string: 7-3-8-5-2

from MyArrays import second_largest, difference, median, smallest_largest, arr_to_str

arr = [7, 3, 8, 5, 2]
print(f'Numbers: {",".join([str(i) for i in arr])}')
print(f'Second largest number: {second_largest(arr)}')
print(f'Largest smallest diference: {difference(arr)}')
print(f'Median: {median(arr)}')
smallest, largest = smallest_largest(arr)
print(f'Smallest and largest number: {smallest},{largest}')
print(f'Numbers as a string: {arr_to_str(arr)}')