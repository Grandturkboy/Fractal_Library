import turtle

permut = int(input("Enter the number of iterations (Dont ask for more than nine): "))

def drawTriangle(points, myTurtle):
    myTurtle.up()
    myTurtle.goto(points[0][0], points[0][1])
    myTurtle.down()
    myTurtle.goto(points[1][0], points[1][1])
    myTurtle.goto(points[2][0], points[2][1])
    myTurtle.goto(points[0][0], points[0][1])

def sierpinski(points, permut, myTurtle):
    drawTriangle(points, myTurtle)
    if permut > 0:
        sierpinski([points[0], middle(points[0], points[1]), middle(points[0], points[2])], permut-1, myTurtle)
        sierpinski([points[1], middle(points[0], points[1]), middle(points[1], points[2])], permut-1, myTurtle)
        sierpinski([points[2], middle(points[2], points[1]), middle(points[0], points[2])], permut-1, myTurtle)

def middle(p1, p2):
    return [(p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2]

def main():
    myTurtle = turtle.Turtle()
    myTurtle.hideturtle()
    myTurtle.speed(0)

    myWin = turtle.Screen()
    turtle.tracer(0, 0)

    myPoints = [[-200, -150], [0, 200], [200, -150]]
    sierpinski(myPoints, permut, myTurtle)
    turtle.update()
    myWin.exitonclick()


main()