# Create a program that computes the second power of each array element. Sample result:

arr = [8, 2, 5, 1, 9]
power = []

print('Array: ', end="")
for elem in arr:
    print(elem, end=' ')

print()

print('2nd power: ', end="")
for elem in arr:
    power = elem ** 2
    print(power, end= " ")

# Array: 8 2 5 1 9
# 2nd power: 64 4 25 1 81