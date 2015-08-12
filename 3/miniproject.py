import turtle

def drawTurtles():
    window = turtle.Screen()
    brad = turtle.Turtle()
    brad.shape("classic")
    brad.speed(0)
    brad.goto(-100,-100)
    startLocation = brad.position()
    xlocation = startLocation[0]
    ylocation = startLocation[1]
    drawTriangle(brad,100,5,xlocation,ylocation)
    window.exitonclick()



def drawTriangle(turtle,length,levels,xLocation,yLocation):
    if levels == 0:
        return
    else:
        turtle.setposition(xLocation,yLocation)
        turtle.pendown()
        levels = levels - 1
        point1 = turtle.position()
        x1location = float(point1[0])
        y1location = float(point1[1])
        turtle.forward(100)
        turtle.right(120)
        point2 = turtle.position()
        x2location = float(point2[0])
        y2location = float(point2[1])
        turtle.forward(100)
        turtle.right(120)
        point3 = turtle.position()
        x3location = float(point3[0])
        y3location = float(point3[1])
        turtle.forward(100)
        turtle.penup()
        turtle.setheading(90)
        drawTriangle(turtle,float(length/2),levels,x1location/2,y1location/2)
        drawTriangle(turtle,float(length/2),levels,x2location/2,y2location/2)
        drawTriangle(turtle,float(length/2),levels,x3location/2,y3location/2)

drawTurtles()