# Write a program that prints:

# the array
# number of elements
# first value
# second value
# last value
# last but one value (do not use negative index values)
# sum of the first and last value
# middle value
# all array values separated by a single space (use a loop statement)

import statistics

arr = [2, 3, 7, 5, 4]

print(arr)
print('Number of elements', len(arr))
print('First value', arr[0])
print('Second value', arr[1])
print('Last value', arr[-1])
print('Last but one', arr[3])
print(f'Sum of the first and last value: {arr[0] + arr[-1]}' )
print(f'Middle value {statistics.median(arr)}')
print('All array values:')
for i in range(len(arr)):
    print(arr[i], end=' ')
