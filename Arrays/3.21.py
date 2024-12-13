# Write a program that checks whether 
# the first array is a subset of the second one 
# (whether all elements of the first array appear in the second array).

arr1 = [5, 15, 25]
arr2 = [10, 20, 30, 5, 15, 25]

for elem in arr1:
    if elem not in arr2:
        print('First array is not a subset of the second one.')
        break
else:
    print('First array is a subset of the second one.')

