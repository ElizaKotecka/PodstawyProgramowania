# Function that computes the sum of the digits of a number.
# When the value of the even parameter is True,
# the function returns the sum of the even digits. 
# When the value of the even parameter is False,
# the function returns the sum of the odd digits.

def f(number, even):
    sum = 0
    for digit in str(number):
        digit = int(digit)
        if even:
            if digit % 2 == 0:
                sum += digit
        else:
            if digit % 2 != 0:
                sum += digit
    return sum
    
if __name__ == '__main__':
    print(f(3124, True))
    print(f(3124, False))
    print(f(20576, False))
    print(f(20576, True))
    print(f(13115, True))


