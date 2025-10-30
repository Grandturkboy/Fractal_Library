import turtle
import tkinter as tk


root = tk.Tk()
root.title("Peano Curve Controls")

canvas = tk.Canvas(root, width=600, height=600)
canvas.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

screen = turtle.TurtleScreen(canvas)
screen.tracer(0, 0)
functionsUsed = 0
t = turtle.RawTurtle(screen)
t.hideturtle()
t.speed(0)

iteration_slider = tk.Scale(root, from_=0, to=14, resolution=1, orient="horizontal", label="Iterations")
iteration_slider.set(1)
iteration_slider.pack()

size_slider = tk.Scale(root, from_=0, to=500, resolution=10, orient="horizontal", label="Size")
size_slider.set(400)
size_slider.pack()

angle_slider = tk.Scale(root, from_=0, to=180, resolution=3, orient="horizontal", label="Angle")
angle_slider.set(90)    
angle_slider.pack()

previousIter = iteration_slider.get()
previousSize = size_slider.get()
previousAngle = angle_slider.get()

def toggleRainbow():
    global rainbow
    rainbow = not rainbow
    redraw()

rainbow = False
rainbowButton = tk.Checkbutton(root, text="Rainbow", command=toggleRainbow, width=20)
rainbowButton.pack()
colors = ["#FF0000","#FF1900","#FF3300","#FF4C00","#FF6600","#FF7F00","#FF9900","#FFB200","#FFCC00","#FFE500","#FFFF00","#E5FF00","#CCFF00","#B2FF00","#99FF00","#7FFF00","#66FF00","#4CFF00","#33FF00","#19FF00","#00FF00","#00FF19","#00FF33","#00FF4C","#00FF66","#00FF7F","#00FF99","#00FFB2","#00FFCC","#00FFE5","#00FFFF","#00E5FF","#00CCFF","#00B2FF","#0099FF","#007FFF","#0066FF","#004CFF","#0033FF","#0019FF","#0000FF","#1900FF","#3300FF","#4C00FF","#6600FF","#7F00FF","#9900FF","#B200FF","#CC00FF","#E500FF","#FF00FF"]


functionCounter = tk.Label(root, text=f"Functions used: {functionsUsed}")
functionCounter.pack()

def PeanoIt(iter, angle, length):
    global functionsUsed

    if iter == 0:
        return
    
    if rainbow:
        t.pencolor(colors[functionsUsed % len(colors)])
        t.pensize(3)
    else:
        t.pencolor("black")
        t.pensize(1)

    functionsUsed += 1
    functionCounter.config(text=f"Functions used: {functionsUsed}")

    PeanoIt(iter - 1, angle, length)
    t.forward(length / 3)
    PeanoIt(iter - 1, -angle, length)
    t.forward(length / 3)
    PeanoIt(iter - 1, angle, length)
    t.right(angle)
    t.forward(length / 3)

    t.right(angle)
    PeanoIt(iter - 1, -angle, length)
    t.forward(length / 3)
    PeanoIt(iter - 1, angle, length)
    t.forward(length / 3)
    PeanoIt(iter - 1, -angle, length)
    t.left(angle)
    t.forward(length / 3)
    
    t.left(angle)
    PeanoIt(iter - 1, angle, length)
    t.forward(length / 3)
    PeanoIt(iter - 1, -angle, length)
    t.forward(length / 3)
    PeanoIt(iter - 1, angle, length)

def redraw():
    global functionsUsed
    functionsUsed = 0
    t.clear()
    t.penup()
    t.setpos(-200, -200)
    t.setheading(90)
    t.pendown()

    PeanoIt(iter = iteration_slider.get(), angle = angle_slider.get(), length = 3 * (size_slider.get() / ((3 ** iteration_slider.get()) - 1)))
    screen.update()

def hasIterationChanged():
    global previousIter, previousSize, previousAngle
    currentIter = iteration_slider.get()
    currentSize = size_slider.get()
    currentAngle = angle_slider.get()
    if currentIter != previousIter or currentSize != previousSize or currentAngle != previousAngle:
        redraw()
        previousIter = currentIter
        previousSize = currentSize
        previousAngle = currentAngle
    root.after(100, hasIterationChanged)

redraw()
hasIterationChanged()
root.mainloop()
