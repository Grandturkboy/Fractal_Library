import turtle

permut = int(input("Enter the number of iterations(dont use more than 4): "))
size = int(input("Enter the size of the carpet (suggested 243): "))
points = [[size, -size], [-size, -size], [-size, size], [size, size]]

myTurtle = turtle.Turtle()
myTurtle.hideturtle()
myTurtle.speed(0)
myWin = turtle.Screen()
turtle.tracer(0, 0)

def roundPoints(points):
    return [[round(x), round(y)] for x, y in points]

def drawSquare(points, color):
    points = roundPoints(points)
    turtle.up()
    turtle.goto(points[0][0], points[0][1])
    turtle.down()
    turtle.fillcolor(color)
    turtle.begin_fill()
    for p in points[1:] + [points[0]]:
        turtle.goto(p[0], p[1])
    turtle.end_fill()
    turtle.up()

def innerSquare(points):
    x0, y0 = points[0]
    x1, y1 = points[1]
    x2, y2 = points[2]
    x3, y3 = points[3]

    width = x1 - x0
    height = y3 - y0

    new_points = [
        [x0 + width / 3, y0 + height / 3],
        [x1 - width / 3, y1 + height / 3],
        [x2 - width / 3, y2 - height / 3],
        [x3 + width / 3, y3 - height / 3]
    ]

    return new_points
def subdivideSquare(points):
    x0, y0 = points[0]
    x1, y1 = points[1]
    x2, y2 = points[2]
    x3, y3 = points[3]

    width = (x1 - x0) / 3
    height = (y3 - y0) / 3 

    squares = []
    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1:
                continue
            bl = [x0 + i*width, y0 + j*height]
            br = [bl[0] + width, bl[1]]
            tr = [br[0], br[1] + height]
            tl = [bl[0], bl[1] + height]
            
            squares.append([bl, br, tr, tl])
    return squares

def carpet(points, permut, myTurtle):
    if permut == 0:
        drawSquare(innerSquare(roundPoints(points)), "white")
        return
    else:
        drawSquare(innerSquare(roundPoints(points)), "white")
        new_points = subdivideSquare(roundPoints(points))
        for p in new_points:
            carpet(p, permut - 1, myTurtle)

drawSquare(points, "black")
drawSquare(innerSquare(points), "white")
carpet(points, permut, myTurtle)
turtle.update()
myWin.exitonclick()