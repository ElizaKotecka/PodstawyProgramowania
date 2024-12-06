# The speed of vehicles on highways in Poland is at least 40 km/h and not more than 140 km/h.
# Write a program that prints a message when the specified car speed, read from the keyboard, has been exceeded. 

speed_limit_min = 40
speed_limit_max = 140

car_speed = int(input("Enter car speed: "))

if car_speed < speed_limit_min or car_speed > speed_limit_max:
    print("Warning: invalid car speed!!")