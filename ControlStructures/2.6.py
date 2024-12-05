# Write a program that checks
# what number was entered from the keyboard
# and prints one of the messages below.
#  7, 1 ,0 ,-1 , -4

number = int(input("Enter a number (integer): "))

if number > 0:
    result = print(f"Number {number} is positive.")
elif number < 0:
    result = print(f"Number {number} is negative.")
else:
    result = print(f"Number is {number}.")



