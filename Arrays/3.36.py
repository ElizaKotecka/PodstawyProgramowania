# Create a function that convert two-dimensional (2D) array into 1D. 
# Then create a program that prints 1D array for the following 2D arrays.

mat1 = [[2, 3], [1, 5]]
mat2 = [[5, 0, 3, 7, 5], [9, 0, 9, 1, 2]]
mat3 = [[2, 1], [3, 5], [7, 4], [2, 6]]

def convert_to_1d(m):
    array_1d = []
    for row in m:
        for elem in row:
            array_1d.append(elem)
    return array_1d


def print_matrix(m):
    for row in m:
        for elem in row:
            print(elem, end=' ')
        print()


print('Matrix 1:')
print_matrix(mat1)

print('1D array 1:')
print(convert_to_1d(mat1))
print()

print('Matrix 2:')
print_matrix(mat2)

print('1D array 2:')
print(convert_to_1d(mat2))
print()

print('Matrix 3:')
print_matrix(mat3)

print('1D array 3:')
print(convert_to_1d(mat3))