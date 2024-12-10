# Returns a sentence with spaces removed.

def f(sentence):
    sentence_without_spaces = ""
    for char in sentence:
        if char == ' ':
            continue
        else:
            sentence_without_spaces += char
    return sentence_without_spaces

if __name__ == '__main__':
    print(f('integrated development environment'))
    print(f("A programming language is a system of notation for writing computer programs"))
