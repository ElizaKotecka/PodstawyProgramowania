###
# Functions to read any data type from the keyboard

# input_string() that returns a string entered from the keyboard
# input_integer() that returns an integer number entered from the keyboard
# input_real() that returns a real number entered from the keyboard
# input_boolean() that returns a boolean value depending on the pressed y/n key

def input_string(message):
    string = input(message)
    return string

def input_integer(message):
    integer = int(input(message))
    return integer

def input_real(message):
    real = float(input(message))
    return real

def input_boolean(message):
    answer = input(message)
    if answer == "y":
        return True
    elif answer == 'n':
        return False
    else:
        return 'Unexpected answer.'
