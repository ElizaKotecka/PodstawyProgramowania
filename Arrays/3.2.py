# An array contains natural numbers: 
# 15, 8, 31, 47, 2, 19. 
# Create a program that prints the contents of the array 
# in reverse order. Use any loop statement. Sample result:
# existed array: 15 8 31 47 2 19 
# reverse array: 19 2 47 31 8 15

array = [1,20,323,4423,55,66,7]
reversed = array[::-1]

print("existed array: ", end="")
for i in array:
    print(i, end=" ")

print()

print("reverse array: ", end="")
for i in reversed:
    print(i, end=" ")
