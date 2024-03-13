# Author: Caleb A. Moura

import turtle

# Set up turtle window and rename to lab nuber in cycle
window = turtle.Screen()
window.title("Lab 6")

# Create turtle object, and set coordinate specifics.
Pau = turtle.Turtle()
def draw_square(x, y):
    Pau.penup()
    Pau.goto(x - 50, y - 50)
    Pau.pendown()
    Pau.begin_fill()
    for _ in range(4):
        Pau.forward(100)
        Pau.right(90)
    Pau.end_fill()


def main():

    # Prompt user for color and size.
    color = Pau.textinput("Color", "Enter a color name:")
    size = Pau.numinput("Size", "Enter a size (1-5):", minval=1, maxval=5)

    # Setup turtle details.
    Pau.speed(0)
    Pau.shape("turtle")
    Pau.color(color)
    Pau.shapesize(size)

    # Set up onclick event.
    Pau.onscreenclick(draw_square)

    # Set turtle to listen for events.
    Pau.listen()
    Pau.mainloop()

if __name__ == "__main__":
    main()