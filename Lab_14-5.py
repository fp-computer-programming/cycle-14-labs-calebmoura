# Author: Caleb A. Moura

import turtle

# Set up turtle and window.
turtle.setup(400, 400)
window = turtle.Screen()
window.title("Turtle Controller")
window.bgcolor("lightgrey")

Pau = turtle.Turtle()

# Function to move turtle forward.
def move_forward():
    Pau.forward(10)

# Function to move turtle backward.
def move_backward():
    Pau.backward(10)

# Function to turn turtle left.
def turn_left():
    Pau.left(90)

# Function to turn turtle right.
def turn_right():
    Pau.right(90)

# Set key binds for movement to arrow keys.
window.listen()
window.onkey(move_forward, "Up")
window.onkey(move_backward, "Down")
window.onkey(turn_left, "Left")
window.onkey(turn_right, "Right")

# Keep window open after sequence ended.
window.mainloop()