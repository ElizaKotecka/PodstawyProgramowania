# Returns the sum of numbers in the range <x,y>
# that are completely divisible by 2 and 3 and not divisible by 4.

def f(x,y):
    sum = 0
    for nb in range(x, y+1):
        if nb % 6 == 0:
            if nb % 4 == 0:
                continue
            else:
                sum += nb
        else:
            continue
    return sum

if __name__ == '__main__':
    print(f(1,20))
    print(f(10,30))