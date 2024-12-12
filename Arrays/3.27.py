# A two-dimensional array of size 2 by 4 contains integer numbers. 
# Create a program that prints array values in rows and columns.

arr = [
    [1,2,3,4],
    [5,6,7,8]
    ]

print('Rows: ')
for row in arr:
    for elem in row:
        print(elem, end = ' ')
    print()

print('Columns: ')
for col in range(len(arr[0])):
    for elem in arr:
        print(elem[col], end= ' ')    
    print()


