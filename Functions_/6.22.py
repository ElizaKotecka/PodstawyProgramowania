# A text contains any number of words. 
# Returns the acronym (first letters of all words).

def f(name):
    counter = 0
    acronym = ""
    acronym += name[0]
    for char in name[1:]:
        counter += 1
        if char == ' ':
            acronym += name[counter+1]
    return acronym

if __name__ == '__main__':
    print(f("Python"))
    print(f("For Your Information"))
    print(f("Internet of Things"))