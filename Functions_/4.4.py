###
# Calculates the sum of the digits in a number
#

def sum_digits(number):
    result = 0
    abs_number = abs(any_number)
    number = str(abs_number)

    for char in number:
        result += int(char)

    return result

any_number = int(input('Enter integer number: '))
result = sum_digits(any_number)
print(f'The sum of the digits in the number {any_number} is {result}.')