# Returns numbers from 1 to n as a string.

def f(n):
    nb_str = ''
    for nb in range(1,n+1):
        nb_str += str(nb)
    return nb_str

if __name__=='__main__':
    print(f(11))
    print(f(4))




