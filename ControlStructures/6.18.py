# Write a program that determines in which quadrant of the coordinate system the point P(x, y) is located
# or on which axis it is located, or that it is located in the position (0,0) of the coordinate system. 

x = 0
y = 0

if x == 0 and y == 0:
    print(f"Point P({x}, {y}) is located in the position (0,0) of the coordinate system.")
elif x == 0:
    print(f"Point P({x}, {y}) is on the y-axis.")
elif y == 0:
    print(f"Point P({x}, {y}) is on the x-axis.")
elif x > 0 and y > 0:
    print(f"Point P({x}, {y}) is in the first quadrant.")
elif x < 0 and y > 0:
    print(f"Point P({x}, {y}) is in the second quadrant.")
elif x < 0 and y < 0:
    print(f"Point P({x}, {y}) is in the third quadrant.")
elif x > 0 and y < 0:
    print(f"Point P({x}, {y}) is in the fourth quadrant.")