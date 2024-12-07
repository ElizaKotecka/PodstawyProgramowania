###
# Draws each of the figures (square, triangle, rectangle) twice,
# in different locations
#

import turtle

def draw_square(length):
    # Draw a square
    for i in range(4):
        pen.forward(length)
        pen.right(90)

def draw_triangle(length):
    for i in range(3):
        pen.forward(length)
        pen.left(120)

def draw_rectangle(length_a, length_b):
    for i in range(2):
        pen.forward(length_a)
        pen.left(90)
        pen.forward(length_b)
        pen.left(90)

def teleport(x,y):
    pen.penup()
    pen.goto(x,y)
    pen.pendown()

if __name__ == "__main__":
    # Set up the screen
    window = turtle.Screen()
    window.bgcolor("lightgreen")

    # Create the turtle
    pen = turtle.Turtle()
    pen.speed(5)

    draw_square(100)
    
    teleport(150, 0)
    draw_square(100)

    teleport(0, 150)
    draw_triangle(100)

    teleport(150, 150)
    draw_triangle(100)

    teleport(0, 300)
    draw_rectangle(100,50)

    teleport(150, 300)
    draw_rectangle(100,50)

    pen.hideturtle()
    window.mainloop()
    