import turtle

class turtleObjects(turtle.Turtle):
    def square(self):
        for i in range(4):
            self.forward(100)
            self.right(90)
    def design(self, color = "black"):
        self.color(color)
        self.shape("turtle")
    def triangle(self):
        for i in range (3):
            self.forward(100)
            self.right(120)


def drawTurtles():
    window = turtle.Screen()
    #turtle makes a square
    brad = turtleObjects()
    brad.design()
    brad.square()

    #turtle makes a circle

    angie = turtleObjects()
    angie.speed(2)
    angie.circle(100)

    #turtle makes a triangle
    desmond = turtleObjects()
    desmond.triangle()

drawTurtles()