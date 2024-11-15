# 1
company = "ABC Data"            #name = company, value = "ABC Data", value type = str
phone = "555-123-009"           #name = phone, value = "555-123-009", value type = str
employees = 25                  #name = empluyees, value = 25, value type = int
remote_work = True              #name = remote_work, value = True, value type = bool
big_company = employees > 100   #name = big_company, value = employees > 100, value type = bool
income = 4500000                #name = income, value = 4500000, value type = int
income_per_person = income / employees  #name = income_per_person, value = income / employees, value type = float/int

#2
###
# Modify the program to calculate the sum of three numbers.
#
number1 = 71
number2 = 14
number3 = 33
result = number1 + number2 + number3
print('Number 1: ', number1)
print('Number 2: ', number2)
print('Number 3: ', number3)
print('The result of summation: ', result)

# 3
###
# A program for swapping two varable values
#
x = 7
y = 34
z = 0 # additional, auxiliary variable
print("Before swapping: x=", x, "y=", y)

# swap the values
z = x
x = y
y = z
print("After swapping: x=", x, "y=", y)

# 4
###
# A program that, for a given speed in km/h,
# prints the speed in m/s
#
speed_kmh = 70
speed_ms = speed_kmh*1000/3600
print(speed_kmh, "km/h = ", speed_ms, "m/s")

#5
###
# A program that calculates the length of the diagonal
# of a rectangle with sides a and b.
#
import math
a = 5
b = 8
diagonal = math.sqrt(a**2 + b**2)
print(diagonal)

#6
# A program thah calculates the distance to the horion from a height given in meters from the keyboard

height = input("Height in meters: ")
d = 3.57 * math.sqrt(int(height))
print("Distance to the horizon is:", d, 'km')

# A program thah calculates the distance to the horion from a my height

my_height = 1.6
d = 3.57 * math.sqrt(my_height)
print("Distance to the horizon from beach is:", d, 'km')

# A program thah calculates the distance to the horion from a height of the hotel window

window_height = 20
d = 3.57 * math.sqrt(window_height)
print("Distance to the horizon from hotel window is:", d, "km")

#7
###
# A program that calculates and prints:
# - the number of people and percentage of the total
#   population living in the Northern Hemisphere
# - the number of people and percentage of the total
#   population living in the Southern Hemisphere
#
total = 8000000000
north = 7200000000
south = total - north
print("World population: ", total)
print("Northern Hemisphere: ", north)
print("Northern Hemisphere in %: ", north/total*100)

print("Southern Hemisphere: ", south)
print("Southern Hemisphere in %: ", south/total*100)

#8
###
# A program that calculates and prints
# the average grade of a student
#
math_grade = 5
art = 4
music = 5
history = 3
average = math_grade + art - music + history / 4
print("Average grade is", average)