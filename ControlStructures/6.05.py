###
# Program that simulates the operation of an electronic thermometer.
#

temperature = -2

if temperature > 35:
    print("It is extremely hot.")
elif temperature > 30:
    print("It is ho.")
elif temperature >= 15:
    print("It is warm.")
elif temperature >= 0:
    print("It is cold.")
else:
    print("Warning, frost.")