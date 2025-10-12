import turtle
ratio = 0.75
iterations = 10*(ratio**-1)**int(input("Enter the number of iterations: "))
length = 100*(ratio**-1)**float(input("Enter the initial branch length(~1): "))
deg = int(input("Enter the turning degree per iteration(~30): "))

myTurtle = turtle.Turtle()
myTurtle.hideturtle()
myTurtle.speed(0)
myTurtle.left(90)
myTurtle.up()
myTurtle.setposition(0, -250)
myTurtle.down()

myWin = turtle.Screen()
turtle.tracer(0, 0)

def drawBranch(n,length, myTurtle):
    if n < 11:
        return
    else:
        myTurtle.forward(length)
        drawBranch(n * (ratio), length * ratio, myTurtle)
        myTurtle.left(deg)
        drawBranch(n * (ratio), length * ratio, myTurtle)
        myTurtle.right(2 * deg)
        drawBranch(n * (ratio), length * ratio, myTurtle)
        myTurtle.left(deg)
        myTurtle.backward(length)

drawBranch(iterations, length, myTurtle)
turtle.update()
myWin.exitonclick()
