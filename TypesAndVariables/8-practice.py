#2
# Calculation of circle area and circumference 
#

# determine radius and PI values
import math
radius = int(input("Give radius of circle in cm: "))
pi_value = math.pi
# calculate area
area = pi_value*radius**2
# calculate circumference
circumference = 2*pi_value*radius
# print results

print(f"Area: {area:.2f}. Circumference: {circumference:.2f}.")

#3
# A program that reads temperature in degrees Celsius from the keyboard.
# Use comments to briefly describe the program's algorithm.
#

celsius = int(input("Enter temperature in Celsius: "))
kelvin = celsius + 273.15
farenheit = (celsius*1.8) + 32
print(f"Same temperatures in Kelvin: {kelvin:.1f} and Farenheit {farenheit:.1f}.")

#4
# A program that prints your height both in cm and in feet and inches.
#
cm = 170
feet = (cm * 0.0328084)
inches = (cm * 0.3937007874)

print(f'I am {cm} cm tall, i.e. {feet:.2f} feet and {inches:.1f} inches.')

#5
# A program that reads a SWIFT code from the keyboard
# and prints the bank code and country code.
#BPKOPLPW, CHASUS33, DEUTDEFF

swift = input('Enter SWIFT code: ')
print(f'Bank Code: {swift[:4]}')
print(f'Country Code: {swift[4:6]}')

#6
# The program calculates the cost of transporting goods
# based on the given distance in km, fuel price per 1 liter,
# and fuel consumption in liters per 100 km.
#
distance = int(input('Enter distance in km: '))
fuel_price = float(input('Enter fuel price per liter: '))
fuel_consumption = float(input("Enter fuel consumption per 100km: "))
total_fuel_consumption = distance/100 * fuel_consumption
total_cost = total_fuel_consumption * fuel_price
print(f"Total fuel consumption: {total_fuel_consumption:.1f}.")
print(f"Total cost: {total_cost:.2f} zl.")

#7
number = int(input("Enter number: "))
print(f"Binary number: {number:#b}.")       # bin(number)
print(f"Hexadecimal number: {number:#x}.")  # hex(number)