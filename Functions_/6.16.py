# Returns the n-th value of the Fibonacci sequence.
# The sequence is defined as follows: 
# the first value of the sequence is 0,
# the second value is 1.
# Each subsequent value is the sum of the previous two.


def f(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        a = 0
        b = 1
        for _ in range(3, n + 1):
            a, b = b, a + b
        return b

if __name__ == '__main__':
    print(f(4))
    print(f(9))