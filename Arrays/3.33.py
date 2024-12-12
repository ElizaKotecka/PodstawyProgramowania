# A two-dimensional array of the size 3 by 5 contains integer numbers. 
# Create a program that swaps the first and the last column. 
# Print array values in rows and columns before and after changes.

arr = [
    [1,2,3,4,5],
    [6,7,8,9,0],
    [5,4,3,2,1]
]

print('Before changes:')
for row in arr:
    print(row)

for row in arr:
    row[0], row[4] = row[4], row[0]

print('After changes:')
for row in arr:
    print(row)
