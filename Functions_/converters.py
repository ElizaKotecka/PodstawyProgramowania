#Define the following functions in the converters.py file that allow you to:
# convert centimeters to inches
# convert feet and inches to centimeters

def m_to_cm(n):
    return n*100

def cm_to_m(n):
    return n/100

def cm_to_in(n):
    return n*0.39

def in_to_cm(n):
    return n*2.54

def ft_to_in(n):
    return n*12


if __name__ == "__main__":
    # only execute when you run this module
    # so you can test the functions in this place
    print(f'2m = {m_to_cm(2)}cm')
    print(f'532cm = {cm_to_m(532)}m')
    print(f'50cm = {cm_to_in(50)}in')
    print(f'340in = {in_to_cm(340)}cm')
    print(f'30ft = {ft_to_in(30)}in')