# Author: Caleb A. Moura

import turtle

# Create a default-size turtle window.
window = turtle.Screen()

# Set title of turtle window to lab number in cycle.
window.title("Lab 4")

# Change speed of turtle to slow, and color of turtle to my favorite color.
Pau = turtle.Turtle()
Pau.speed(1)
Pau.color("blue")

# Create stamp of turtle at origin.
Pau.stamp()

# Using goto() to create a square.
Pau.penup()
Pau.goto(100, 100)
Pau.pendown()
for _ in range(4):
    Pau.forward(100)
    Pau.right(90)

# Fill in square with teal color.
Pau.fillcolor("teal")
Pau.begin_fill()
for _ in range(4):
    Pau.forward(100)
    Pau.right(90)
Pau.end_fill()

# Keep window open until closed by user.
window.mainloop()