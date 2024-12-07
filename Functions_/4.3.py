###
# Calculates the area of a triangle based on the lengths
# of the triangle's sides

# 3, 4, 5 (result is 6)
# 5, 12, 13 (result is 30)
# 7, 24, 25 (result is 84)

import math

def triangle_area(a,b,c):
    s = (a + b + c)/2
    area = math.sqrt(s*(s-a)*(s-b)*(s-c))
    return area

a = int(input('Enter side "a" of the triangle: '))
b = int(input('Enter side "b" of the triangle: '))
c = int(input('Enter side "c" of the triangle: '))

triangle = triangle_area(a,b,c)

print(f'The area of a triangle with sides a = {a}, b = {b}, c = {c}  is {triangle:.0f}.')