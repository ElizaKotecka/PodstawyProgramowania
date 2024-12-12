# Create a function identity_matrix(n) that returns an identity matrix(2D array) of size n.
# Then, create a function that prints a 2D array in rows and columns. 
# Finally, create a program that prints three identity matrices 
# with dimensions of 3, 5 and 8. Sample result:

# 1 0 0 0 0
# 0 1 0 0 0
# 0 0 1 0 0
# 0 0 0 1 0
# 0 0 0 0 1

def identity_matrix(n):
    matrix = []
    for i in range(n):
        row = []
        for j in range(n):
            if i == j:
                row.append(1)
            else:
                row.append(0)
        matrix.append(row)
    return matrix

def print_matrix(matrix):
    for row in matrix:
        for element in row:
            print(element, end=" ")
        print()

print_matrix(identity_matrix(3))
print()
print_matrix(identity_matrix(5))
print()
print_matrix(identity_matrix(8))
print()