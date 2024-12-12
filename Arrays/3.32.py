# Create a program that swaps the first and the last row. 
# Print array values in rows and columns before and after changes.

arr = [
    [1,2,3,4,5],
    [6,7,8,9,0],
    [5,4,3,2,1]
]

print('Before changes:')
for row in arr:
    print(row)

arr[0], arr[-1] = arr[-1], arr[0]

print('After changes:')
for row in arr:
    print(row)