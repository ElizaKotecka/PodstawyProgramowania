# The vending machine accepts 1, 2 and 5 PLN coins. 
# Define a function f(amount_to_pay) that returns the minimum number of coins
# that can be used to pay for the purchased product.

def f(amount_to_pay):
    count = 0

    count += amount_to_pay // 5
    amount_to_pay %= 5

    count += amount_to_pay // 2
    amount_to_pay %= 2

    count += amount_to_pay

    return count


if __name__ == '__main__':
    print(f(23))
    print(f(8))
    print(f(2))
    print(f(0))
