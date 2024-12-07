###
# Program for testing built-in functions
#
max_number = max(7,5,6,3,8,2)
print('Max number of 7,5,6,3,8,2 is', max_number)

min_number = min(4,7,2,3,9,8)
print('Min number of 4,7,2,3,9,8 is', min_number)

str_length = len("computer science")
print('The number of characters in "computer science" is', str_length)

letter = input("Enter a letter: ")
print('The letter you entered is', letter)

number_from_string = int("20303")
print('The number from the string "20303" is', number_from_string)

binary_rep = bin(304)
print('Decimal number 304 in binary is', binary_rep)

hex_rep = hex(304)
print('Decimal number 304 in hexadecimal is', hex_rep)

# Integer representing the Unicode code of the € sign
unicode_euro = ord('€')
print('Integer representing the Unicode code of the € sign is', unicode_euro)

# Absolute value of -17
absolute_value = abs(-17)
print('The absolute value of -17 is', absolute_value)