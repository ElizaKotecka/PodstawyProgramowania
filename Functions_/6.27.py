# Define a function f(product_code) that returns True if the product code is correct
# or False otherwise.

def f(product_code):
    sum = 0

    for i in range(3):
        sum += int(product_code[i])
    result = sum % 7
    return result == int(product_code[3])

if __name__ == '__main__':
    print(f("1082"))
    print(f("2035"))
    print(f("1114"))
    print(f("7071"))

    