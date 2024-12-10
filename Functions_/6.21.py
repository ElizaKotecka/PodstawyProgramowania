# Returns the difference between the largest and smallest numbers.

def f(number1, number2, number3):
    max_numer = max(number1, number2, number3)
    min_number = min(number1, number2, number3)
    return max_numer-min_number

if __name__ == '__main__':
    print(f(7,4,9))
    print(f(2,12,8))

