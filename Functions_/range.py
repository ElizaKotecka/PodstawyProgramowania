# Checks if the number is within the range <x, y>.

def check_range(n, x, y):
    return x <= n <= y


if __name__ == '__main__':
    print(check_range(7,2,7))
