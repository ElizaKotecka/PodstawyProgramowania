# Define a function occurs(number, array) that returns 
# True if a given number is present in an array. 
# Then create a program that checks whether the number 
# entered from the keyboard is present in the 
# array [15, 38, 7, 23, 14]. 

# Sample result:
# Number: 23
# Array: 15 38 7 23 14
# Result: number 23 appears in the array

def occurs(number, array):
    if number in array:
        return True
    else:
        return False

array = [15, 38, 7, 23, 14]
number = int(input("Number: "))
print("Array: ", array)
if occurs(number, array):
    print("Result: number", number, "appears in the array")
else:
    print("Result: number", number, "does not appear in the array")