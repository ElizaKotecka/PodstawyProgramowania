# Create a function transpose_matrix(m) that returns transposed matrix
# Then, create a program that prints transposed matrices, 
# in rows and columns, for the following matrices.

def transpose_matrix(m):
    rows = len(m)
    col = len(m[0])
    
    transposed = []
    
    for i in range(col):
        transposed_row = []
        for j in range(rows):
            transposed_row.append(m[j][i])
        transposed.append(transposed_row)
    
    return transposed

def print_matrix(m):
    for row in m:
        for elem in row:
            print(elem, end=" ")
        print()


mat1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
mat2 = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 0]]
mat3 = [[5], [6], [7], [8]]


print('Matrix 1:')
print_matrix(mat1)
print('Transposed matrix 1:')
print_matrix(transpose_matrix(mat1))
print()

print('Matrix 2:')
print_matrix(mat2)
print('Transposed matrix 2:')
print_matrix(transpose_matrix(mat2))
print()

print('Matrix 3:')
print_matrix(mat3)
print('Transposed matrix 3:')
print_matrix(transpose_matrix(mat3))

