import turtle

def drawSquare():
    window = turtle.Screen()
    window.bgcolor("red")

    brad = turtle.Turtle()
    brad.shape("classic")
    brad.color("black")
    brad.speed(2)
    while True:
       
        brad.forward(100)
        brad.right(90)
        brad.forward(100)
        brad.right(90)
        brad.forward(100)
        brad.right(90)
        brad.forward(100)
        brad.right(90)

    window.exitonclick()

drawSquare()