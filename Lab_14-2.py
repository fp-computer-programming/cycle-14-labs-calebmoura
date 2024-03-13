# Author: Caleb A. Moura

import turtle

# Create turtle window.
window = turtle.Screen()
window.setup(width=500, height=500)
window.title("Lab 2")

# Create turtle (Pau)
Pau = turtle.Turtle()

# Draw equilateral triangle starting at 0,0 that moves by 200 units.
Pau.penup()
Pau.goto(0, 0)
Pau.pendown()
for _ in range(3):
    Pau.forward(100)
    Pau.left(120)

# Keep window open until closed by user.
window.mainloop()