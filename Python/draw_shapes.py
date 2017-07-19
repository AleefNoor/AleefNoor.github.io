from turtle import *
import math

# Name your Turtle.
t = Turtle()
sides= int(input("Number of sides?"))
# Set Up your screen and starting position.
setup(500,300)
x_pos = 0
y_pos = 0
t.setposition(0, 0)

### Write your code below:
for x in range(sides):
	forward(100)
	right(360/sides)


# Close window on click.
exitonclick()
