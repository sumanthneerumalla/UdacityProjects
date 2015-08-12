import turtle
import random

def drawSquare():
    window = turtle.Screen()
    window.bgcolor("red")

    brad = turtle.Turtle()
    brad.shape("classic")
    brad.color("black")
    brad.speed(2)



    while True :
        distance = random.randint(20,100)
        direction = random.randint(0,100)
        brad.forward(distance)
        brad.right(direction)





drawSquare()