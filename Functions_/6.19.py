# Returns the sum of repeated digits in a number.

def f(number):
    number_list = []
    str_number = str(number)
    for char in str_number:
        number_list += char
    for element in number_list:
        counter = number_list.count(element)
        if counter > 1:
            return int(element)*counter
    else:
        return 0
        
if __name__ == '__main__':

    print(f(1027))
    print(f(230335))
    print(f(513553007))