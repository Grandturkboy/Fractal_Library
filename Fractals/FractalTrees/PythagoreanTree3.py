import turtle
import tkinter as tk
import math

# Setting up the UI
root = tk.Tk()
root.title("Pythagorean treeControls")

canvas = tk.Canvas(root, width=600, height=600)
canvas.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

screen = turtle.TurtleScreen(canvas)
screen.tracer(0, 0)
functionsUsed = 0
t = turtle.RawTurtle(screen)
t.hideturtle()
t.speed(0)

iteration_slider = tk.Scale(root, from_=0, to=13, resolution=1, orient="horizontal", label="Depth")
iteration_slider.set(6)
iteration_slider.pack()

angle_slider = tk.Scale(root, from_=0, to=360, resolution=1, orient="horizontal", label="Branch Angle")
angle_slider.set(90)
angle_slider.pack()

length_slider = tk.Scale(root, from_=0, to=100, resolution=1, orient="horizontal", label="Initial Length")
length_slider.set(50)
length_slider.pack()

functionCounter = tk.Label(root, text=f"Functions used: {functionsUsed}", width=20)
functionCounter.pack()

def toggleAnimate():
    global animateIt
    animateIt = not animateIt
    redraw()

animateIt = False
animateButton = tk.Checkbutton(root, text=" Animate it ", command=toggleAnimate, width=20)
animateButton.pack()

def toggleVisuals():
    global extras
    extras = not extras
    redraw()

extras = False
extrasButton = tk.Checkbutton(root, text="Show extras", command=toggleVisuals, width=20, )
extrasButton.pack()

prevousIter = iteration_slider.get()
prevousAngle = angle_slider.get()
prevousLength = length_slider.get()

def PythagoreanIt(p1x, p1y, p2x, p2y, p3x, p3y, p4x, p4y, depth, length, LineAngle, squareAngle):
    
    global functionsUsed, extras
    functionsUsed += 1
    #Drawing inital square
    t.penup()
    t.goto(p1x, p1y)
    t.pendown()
    t.goto(p2x, p2y)
    t.goto(p3x, p3y)
    t.goto(p4x, p4y)
    t.goto(p1x, p1y)
    t.penup()

    if depth == 0:
        return
    
    if extras:

        # Drawing the halfcicle. The path of the line.

        t.goto(p4x, p4y)
        t.pencolor("blue")
        t.setheading(squareAngle)
        t.pendown()
        t.forward((length / 18) * math.pi / 2)
        for i in range(17):
            t.right(10)
            t.forward((length / 18) * math.pi)
        t.right(10)
        t.forward((length / 18) * math.pi / 2)
        t.penup()
        t.pencolor("black")

        # Drawing the line that defines the bottoms of the squares

        t.goto((p4x + p3x) / 2, (p4y + p3y) / 2)
        t.pencolor("red")
        t.pendown()
        t.setheading(squareAngle - 90)
        t.left(LineAngle)
        t.forward(length)
        t.penup()
        t.pencolor("black")
    else:
        t.goto((p4x + p3x) / 2, (p4y + p3y) / 2)
        t.setheading(squareAngle - 90)
        t.left(LineAngle)
        t.forward(length)

    # Finding the length and angle of the squares

    cube1length = math.sqrt(((t.xcor() - p4x) ** 2) + ((t.ycor() - p4y) ** 2)) 
    cube2length = math.sqrt(((t.xcor() - p3x) ** 2) + ((t.ycor() - p3y) ** 2))

    leftHeading = squareAngle + LineAngle / 2
    rightHeading = squareAngle + LineAngle / 2 - 90

    # Defining the points of the squares

    #Bottom 2 points of fist square
    c11x = p4x
    c11y = p4y
    c12x = t.xcor()
    c12y = t.ycor()

    #Third point of first square
    t.setheading(leftHeading)
    t.forward(cube1length)
    c13x = t.xcor()
    c13y = t.ycor()

    #Fourth in relation to the third point
    t.left(90)
    t.forward(cube1length)
    c14x = t.xcor()
    c14y = t.ycor()

    #Bottom 2 points of second square
    c21x = c12x
    c21y = c12y
    c22x = p3x
    c22y = p3y
    
    #Third point of second square
    t.goto(c12x, c12y)
    t.setheading(rightHeading)
    t.forward(cube2length)
    c24x = t.xcor()
    c24y = t.ycor()

    #Fourth in relation to the third point
    t.right(90)
    t.forward(cube2length)
    c23x = t.xcor()
    c23y = t.ycor()
    
    #Initiating the recursion
    PythagoreanIt(c11x, c11y, c12x, c12y, c13x, c13y, c14x, c14y, depth - 1, cube1length / 2, LineAngle, leftHeading)
    PythagoreanIt(c21x, c21y, c22x, c22y, c23x, c23y, c24x, c24y, depth - 1, cube2length / 2, LineAngle, rightHeading)

    functionCounter.config(text=f"Functions used: {functionsUsed}")

def sliderCheck():

    #Checking if the slider values have changed, then redrawing if they did

    global prevousAngle, prevousIter, prevousLength, animateIt

    currentIter = iteration_slider.get()
    currentAngle = angle_slider.get()
    currentLength = length_slider.get()

    if (currentIter != prevousIter or currentAngle != prevousAngle or currentLength != prevousLength):
        prevousIter = currentIter
        prevousAngle = currentAngle
        prevousLength = currentLength
        redraw()

    if animateIt:
        angle_slider.set(angle_slider.get() + 2)

    root.after(10, sliderCheck)

def redraw():
    global functionsUsed, angleMid
    functionsUsed = 0
    t.clear()

    angleMid = angle_slider.get()

    if angle_slider.get() > 180:
        while angleMid > 180:
            angleMid -= 180
        if angle_slider.get() > 355:
            angle_slider.set(0)

    PythagoreanIt(-length_slider.get(), -2 * length_slider.get(), length_slider.get(), -2 * length_slider.get(), length_slider.get(), 0, -1 * length_slider.get(), 0, iteration_slider.get(), length_slider.get(), angleMid, 90)

    screen.update()

redraw()
sliderCheck()
root.mainloop()