from turtle import *
wn = Screen()

"""
forward(amount) moves turtle forward by the specified amount

backward(amount) moves turtle backward by the specified amount

right(angle) turns the turtle clockwise by an angle in degrees

left(angle) turns the turtle counterclockwise by an angle in degrees

penup() picks up the turtle, nothing will be drawn until you put the pen down but the turtle can still move

pendown() puts down the turtle

circle(radius) draws a circle at the turtle's location with a specified radius

color(color name) changes the color of the turtle pen

fillcolor(color name) changes the polygon's color

goto(x, y) moves the turtle to position (x, y)

begin_fill() starts filling with the color specified in fillcolor

end_fill() ends filling
"""

#(number of sides - 2) x 180 / number of sides
#(3 - 2) * 180 / 3 triangle
#(4 - 2) * 180 / 4 rectangle

#when drawing angles of x degrees, turn (180 - x), drawing 60 degrees will left(120)

#60 degrees
# forward(100)
# left(120)
# forward(100)
# left(120)
# forward(100)

clear()
#rectangle has 90 degree angles
# forward(100)
# left(90)
# forward(100)
# left(90)
# forward(100)
# left(90)
# forward(100)

# clear()
#pentagon has 108 degree angles
# forward(100)
# left(72)
# forward(100)
# left(72)
# forward(100)
# left(72)
# forward(100)
# left(72)
# forward(100)
# clear()

#(number of sides - 2) x 180 / number of sides: angle
numSides = int(input("Enter the amount of sides you want: "))
amount = int(input("How far you want to go forward: "))
internalAngle = (numSides - 2) * 180 / numSides
turnAngle = 180 - internalAngle
for i in range(numSides - 1):
    forward(amount)
    left(turnAngle)
forward(amount)
done()
