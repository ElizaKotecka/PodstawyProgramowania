# Returns the given text with all characters separated by a dash sign.

def f(text):
    if len(text) > 0:
        return '-'.join(text)
    else:
        return ' '

if __name__ == '__main__':
    print(f("Univesity"))
    print(f("UE"))
    print(f("x"))
    print(f(""))