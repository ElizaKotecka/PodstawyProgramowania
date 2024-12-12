# Write a program that, for the given array of real numbers, 
# prints the number of elements that are greater than the given 
# value entered from the keyboard.

arr = [-3, 3.5, 1, 0, 10, 3.14, 20, -100]

value = float(input("Enter a value: "))
count = 0

for i in arr:
    if i > value:
        count += 1
        
print(count)