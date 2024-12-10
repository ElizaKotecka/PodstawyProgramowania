# Returns a sentence with spaces removed.

def f(sentence: str):
    return sentence.replace(" ", "")

if __name__ == '__main__':
    print(f('integrated development environment'))
    print(f("A programming language is a system of notation for writing computer programs"))
