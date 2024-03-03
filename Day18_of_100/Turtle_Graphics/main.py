import random
from turtle import Turtle,Screen

Tt = Turtle()
Tt.shape("classic")
Tt.color("Black")


def draw_square():
    for _ in range(4):
        Tt.forward(100)
        Tt.left(90)


# draw_square()
# draw_incr_square()


def draw_dashed_line():
    Tt.speed(1)  # Set the speed of the turtle

    # Define the length and gap of dashes
    dash_length = 10
    gap_length = 10

    # Draw dashes
    for _ in range(10):  # Draw 10 dashes
        # Draw a dash
        Tt.forward(dash_length)
        # Move the turtle pen without drawing to create a gap
        Tt.penup()
        Tt.forward(gap_length)
        # Put down the pen to draw the next dash
        Tt.pendown()

    # Keep the window open until it's closed by the user
    # screen.mainloop()


# draw_dashed_line()

colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet", "pink", "cyan", "magenta"]


def draw_diff_shapes(no_of_sides):

    # numbers_of_sides = 3
    angle = 360 / no_of_sides

    for _ in range(no_of_sides):
        Tt.forward(100)
        Tt.right(int(angle))
        no_of_sides += 1


for shape_n in range(3,11):
    Tt.color(random.choice(colors))
    draw_diff_shapes(shape_n)

# draw_diff_shapes()

screen = Screen()
screen.exitonclick()