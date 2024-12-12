# Create a program that prints all unique elements in an array. Sample result:

arr = [2, 3, 2, 5, 8, 1, 9, 8]

unique = []
for elem in arr:
    if arr.count(elem) == 1:
        unique.append(elem)
      

print('Array: ', end="")
for elem in arr:
    print(elem, end=' ')

print()

print('Unique elements: ', end="")
for elem in unique:
    print(elem, end= " ")
    
# Array: 2 3 2 5 8 1 9 8
# Unique elements: 3 5 1 9