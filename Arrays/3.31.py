# Create a program that finds the smallest and largest values in the array 
# and in which row and column they are located.


arr = [
    [-38, 19], 
    [5,40],
    [-7,11],
    [29,16],
]

min_val = arr[0][0]
max_val = arr[0][0]
min_row = 0
min_col = 0
max_row = 0
max_col = 0

for i in range(len(arr)):  # Loop over rows (in column)
    for j in range(len(arr[i])):  # Loop over elem in row
        if arr[i][j] < min_val:
            min_val = arr[i][j]
            min_row = i
            min_col = j
        if arr[i][j] > max_val:
            max_val = arr[i][j]
            max_row = i
            max_col = j

print(f"Min value: {min_val} at row {min_row} and column {min_col}")
print(f"Max value: {max_val} at row {max_row} and column {max_col}")