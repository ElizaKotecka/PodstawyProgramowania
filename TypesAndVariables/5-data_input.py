#1
# A program that reads your first and last name from the keyboard.
# Store this data in two separate variables.
# Then, print your full name i.e. first and last name separated by a single space.

first_name = input('Enter your first name: ')
last_name = input('Enter your last name: ')
full_name = first_name + ' ' + last_name
print(f'Your first name is {first_name} and your last name is {last_name}')
print(f'And your full name is {full_name}')

#2
###
# A program to calculate the volume and surface area of ​​a cube.
# a = 4 --> volume = 64, surface area = 96
# a = 7 --> volume = 343, surface area = 294

cube_side_string = input('Enter cube side: ')
cube_side = int(cube_side_string)
cube_volume = cube_side**3
cube_surface_area = 6*cube_side**2
print(f'The volume of a cube with side {cube_side} is {cube_volume}.')
print(f'The surface area of a cube with side {cube_side} is {cube_surface_area}.')

#3
###
# A program that calculates the volume
# and surface area of ​​a cuboid with sides a, b, and c.
# Read the dimensions of the cuboid from the keyboard.
# a = 3, b = 4, c = 5 --> volume = 60, surface area = 94
# a = 8, b = 1, c = 2 --> volume = 16, surface area = 52

a = input('a=')
b = input('b=')
c = input('c=')
cuboid_volume = int(a)*int(b)*int(c)
cuboid_surface_area = 2*int(a)*int(b) + 2*int(b)*int(c) + 2*int(a)*int(c)
print(f'The volume of a cuboid with a={a}, b={b}, c={c} is {cuboid_volume}.')
print(f'The surface area of a cuboid with a={a}, b={b}, c={c} is {cuboid_surface_area}.')

#4
# Write a program that reads an amount from the keyboard. Then, it calculates and prints both the amount and its VAT.
# Amount  : 15.84
# VAT 23% :  3.64

amount_str = input("Enter amount:")
amount = float(amount_str)
vat_23 = amount*23/100
print(f"23% VAT from {amount} is {round(vat_23, 2)}.")

#5
# Write a program that allows you to enter the product price and discount.
# Enter price: 24.72
# Enter discount %: 15
# Price with discount: 21.01
# Reduction: 3.71

price_str = input("Enter price of the product: ")
price = float(price_str)
discount_str = input("Enter discount [%]: ")
discount = int(discount_str)
reduction = price*discount/100
price_with_discount = price-reduction


print(f"Price of the product: {round(price,2)}. Given discount %: {discount}. Price with discount: {round(price_with_discount,2)}. Reduction: {round(reduction,2)}.")