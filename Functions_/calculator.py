#Program that calculates how many times the given letter appears in any text

def calculator(x):
    letter_list=[]

    for char in x:
        letter_list.append(char)

    counter = letter_list.count("e")

    return counter

if __name__ == "__main__":
    print(calculator("eee"))