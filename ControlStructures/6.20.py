# Write a program that converts a decimal number into a binary number.

decimal_number = int(input("Enter decimal number: "))
original_decimal_number = decimal_number
binary = ""

while decimal_number > 0:
    remainder = decimal_number % 2
    binary += str(remainder) # Add the remainder to the list
    decimal_number = decimal_number // 2  # Update the decimal number

print(f"{original_decimal_number}(10) = {binary[::-1]}(2)")