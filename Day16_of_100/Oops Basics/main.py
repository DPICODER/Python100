# Import the Turtle and Screen classes from the turtle module
from turtle import Turtle, Screen

# Create a Turtle object named 'tt'
tt = Turtle()

# Set the shape of the turtle to 'turtle' and color to 'red'
tt.shape("turtle")
tt.color("red")

# Create a Screen object named 'my_screen'
my_screen = Screen()

# Move the turtle forward by 100 units
tt.forward(100)

# Turn the turtle left by 150 degrees
tt.left(150)

# Move the turtle forward by 100 units
tt.forward(100)

# Turn the turtle left by 150 degrees
tt.left(150)

# Move the turtle forward by 100 units
tt.forward(100)

# Turn the turtle left by 180 degrees
tt.left(180)

# Move the turtle backward by 100 units
tt.forward(100)

# Print the height of the canvas of the screen
print(my_screen.canvheight)

# Wait for the user to click on the screen before closing it
my_screen.exitonclick()


# Import the PrettyTable class from the prettytable module
from prettytable import PrettyTable

# Create a PrettyTable object named 'table'
table = PrettyTable()

# Add columns and data to the table
table.add_column("Names",["Ramesh","Suresh","Somesh","Mallesh","Komtesh","Ganopath"])
table.add_column("Job",["Dev","Assist Engg","Engg","Designer","Tester","Dev"])

# Print the table
print(table)
