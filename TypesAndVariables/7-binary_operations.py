#1
###
# People up to and including 26 years of age are exempt
# from paying taxes in Poland. Write a program that,
# based on the person's age entered from the keyboard,
# prints True if the person is exempt from paying taxes
# and prints False otherwise.
# 38, 27, 26, 22, 18

age = int(input('Enter age: '))
no_tax = age <= 26
print(f'Exemption from paying taxes: {no_tax}')

# #2
# ###
# # A program that checks whether the password length
# # read from the keyboard is correct.
# #university, peter123, (passwords ok) seven, anna333 (passwords to short)

password = input('Enter password: ')
password_ok = len(password) >= 8
print(f'Password length is valid: {password_ok}')

# #3
# ###
# # A program that checks whether the number entered
# # from the keyboard is even.
# # A number is even if the remainder when divided by 2 is 0.
# # What operator do you need to use to calculate
# # the remainder of division?
# #24, 8, 31, 5

number = int(input('Enter number: '))
even = number%2 == 0
print(f'Number is even: {even}')

# #4
# # Write a program that, based on the circumference of the tree entered from the keyboard,
# # calculates and prints the value True if the tree can be cut down, or print the value False otherwise.
# # A tree may be cut down if its diameter is at least 50 cm.
# # Tree 1: 160 Tree 2: 90 Tree 3: 230 Tree 4: 120
import math
circumference = int(input("Enter tree circumference in cm: ")) 
diameter = int(circumference/math.pi)
cut_down = diameter >= 50
print(f"Tree diameter: {diameter}")
print(f"Tree can be cut down: {cut_down}.")

#5
# ###
# # Vehicle registration numbers in Krakow start
# # with the letters KR or KK. Write a program that checks
# # whether the vehicle registration number entered
# # from the keyboard means a vehicle from Krakow.
# # Print True whether a car is from Krakow or False otherwise.
# #
car_number = input('Enter car registration number: ')
is_krakow = car_number[0:2] == "KR" or car_number[0:2] == "KK"
print(f'Car is from Krakow: {is_krakow}')

# #6
# # Write a program that checks whether the vehicle speed entered from the keyboard is correct.
# # The speed of vehicles on a highway in Poland must be between 40 and 140 km/h.

vehicle_speed = int(input("Enter speed of vehicle [km/h]: "))
speed = vehicle_speed >= 40 and vehicle_speed <= 140
print(f"Speed is valid: {speed}")

# #7
# import random
# random_number = random.randint(5,10)
# print(random_number)

#8
###
# A program that prints results of three dice rolls
# and the sum of dice rolled.

import random
dice_roll_1 = random.randint(1,6)
dice_roll_2 = random.randint(1,6)
dice_roll_3 = random.randint(1,6)
total = dice_roll_1 + dice_roll_2 + dice_roll_3
print(dice_roll_1)
print(dice_roll_2)
print(dice_roll_3)
print(f"Sum of three rolls: {total}")

# #9
# #Write a program that prints the number of dice rolled and the value True if the number rolled is 1 or 6.

dice_roll_4 = random.randint(1,6)
print(f"Dice rolled: {dice_roll_4}")
special = dice_roll_4 == 1 or dice_roll_4 == 6
print(f"Special number (1 or 6): {special}")

#10
###
# A program that enables a user to challenge a computer.
# The computer throws dice. Then, the user then tries to guess
# the number from dice by entering a number from 1 to 6
# from the keyboard. If the user has guessed the number
# from the dice, the computer prints True. Otherwise,
# the computer prints False.
#
import random
# COMPUTER TURN
computer = random.randint(1,6)
# YOUR TURN
you = int(input("Guess the rolled number (1-6):"))
print(you)
right = you == computer
print(f'You won: {right}')
