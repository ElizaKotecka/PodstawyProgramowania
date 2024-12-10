# Returns a string of n asterisks, separated by a slash sign.

def f(n):
    result = "*"
    if n == 1:
        return result
    elif n > 0:
        for _ in range(n-1):
            result += '/*'
        return result
    else:
        return "Wrong number or format"
        

if __name__=='__main__':
    print(f(1))
    print(f(4))
