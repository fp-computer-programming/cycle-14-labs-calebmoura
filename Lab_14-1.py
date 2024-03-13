# Author: Caleb A. Moura

import turtle

# Create turtle window.
window = turtle.Screen()
window.title("Lab 1")
window.setup(width=1000, height=1000)

# Create turtle object (Pau).
Pau = turtle.Turtle()

# Using goto to draw rectangle.
Pau.penup()
Pau.goto(0, 0)
Pau.pendown()
Pau.forward(250)
Pau.left(90)
Pau.forward(100)
Pau.left(90)
Pau.forward(250)
Pau.left(90)
Pau.forward(100)

# Keep window open until closed by user.
window.mainloop()