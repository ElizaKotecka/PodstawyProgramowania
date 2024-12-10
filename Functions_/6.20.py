# Returns the n-th prime number.
# A prime number is a natural number greater than 1,
# divisible by 1 and that number.

def is_prime(num):
    for x in range(2, num):
        if num % x  == 0:
            return False
    if num < 2:
        return False
    return True

def f(n):
    count = 0
    candidate = 1
    while count < n:
        candidate += 1
        if is_prime(candidate):
            count += 1
    return candidate


if __name__ == '__main__':
    print(f(1))
    print(f(5))
