# Author: Caleb A. Moura

import turtle

# Create turtle window with grey background.
window = turtle.Screen()
window.bgcolor("grey")

# Rename turtle window to lab number in cycle.
window.title("Lab 3")

# Create turtle, and set color to my favorite.
Pau = turtle.Turtle()
Pau.shape("turtle")
Pau.color("blue")

# Draw equilateral triangle with 200 unit sides.
for _ in range(3):
    Pau.forward(200)
    Pau.left(120)

# Keep window open until closed by user.
turtle.done()