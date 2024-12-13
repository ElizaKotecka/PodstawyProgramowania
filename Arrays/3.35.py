# Create a function transpose_matrix(m) that returns transposed matrix
# Then, create a program that prints transposed matrices, 
# in rows and columns, for the following matrices.

def transpose_matrix(m):
    total_rows = len(m)
    total_col = len(m[0])
    
    transposed = []
    
    for col_nb in range(total_col): #nr kolumny
        transposed_row = []
        for row_nb in range(total_rows): #nr wiersza
            transposed_row.append(m[row_nb][col_nb])
        transposed.append(transposed_row)
    
    return transposed

def print_matrix(m):
    for row in m:
        for elem in row:
            print(elem, end=" ")
        print()


mat1 = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]]
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

