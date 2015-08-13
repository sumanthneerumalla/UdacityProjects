import turtle


brad = turtle.Turtle()
window = turtle.Screen()

brad.speed(0)
for i in range(36):
    brad.left(35)
    brad.forward(50)
    brad.right(35)
    brad.forward(50)
    brad.right(145)
    brad.forward(50)
    brad.right(35)
    brad.forward(50)
    brad.right(10)

brad.setheading(270)
brad.forward(300)

window.exitonclick()