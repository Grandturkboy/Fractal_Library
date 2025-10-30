import turtle
import tkinter as tk
from tkinter import ttk
import math
import time

root = tk.Tk()
root.title("Ultimate Curve Controls")

canvas = tk.Canvas(root, width=600, height=600)
canvas.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

screen = turtle.TurtleScreen(canvas)
screen.tracer(0, 0)
functionsUsed = 0
t = turtle.RawTurtle(screen)
t.hideturtle()
t.speed(0)

var = tk.IntVar(value=1)
PeanoSelect = ttk.Radiobutton(root, text="Peano Curve", variable=var,value=1)
PeanoSelect.pack(anchor="w", padx=30, pady=(20, 0))

HilbertSelect = ttk.Radiobutton(root, text="Hilbert Curve", variable=var,value=2)
HilbertSelect.pack(anchor="w", padx=30)

DragonSelect = ttk.Radiobutton(root, text="Dragon Curve", variable=var,value=3)
DragonSelect.pack( anchor="w", padx=30)

LevyCSelect = ttk.Radiobutton(root, text="Levy C Curve", variable=var,value=4)
LevyCSelect.pack( anchor="w", padx=30)

KochCSelect = ttk.Radiobutton(root, text="Koch Curve", variable=var,value=5)
KochCSelect.pack( anchor="w", padx=30)

KochSSelect = ttk.Radiobutton(root, text="Koch Snowflake", variable=var,value=6)
KochSSelect.pack( anchor="w", padx=30)

MinkowskiSSelect = ttk.Radiobutton(root, text="Minkowski Sausage", variable=var,value=7)
MinkowskiSSelect.pack( anchor="w", padx=30)

MinkowskiISelect = ttk.Radiobutton(root, text="Minkowski Island", variable=var,value=8)
MinkowskiISelect.pack(  anchor="w", padx=30)

iteration_slider = tk.Scale(root, from_=0, to=14, resolution=1, orient="horizontal", label="Iterations")
iteration_slider.set(1)
iteration_slider.pack(pady=(20, 0))

size_slider = tk.Scale(root, from_=0, to=500, resolution=10, orient="horizontal", label="Size")
size_slider.set(400)
size_slider.pack()

angle_slider = tk.Scale(root, from_=0, to=180, resolution=3, orient="horizontal", label="Angle")
angle_slider.set(90)    
angle_slider.pack()

def toggleRainbow():
    global rainbow
    rainbow = not rainbow
    redraw()

rainbow = False
rainbowButton = tk.Checkbutton(root, text="Rainbow", command=toggleRainbow)
rainbowButton.pack(anchor="w", padx=30, pady=(20, 0))
colors = ["#FF0000","#FF1900","#FF3300","#FF4C00","#FF6600","#FF7F00","#FF9900","#FFB200","#FFCC00","#FFE500","#FFFF00","#E5FF00","#CCFF00","#B2FF00","#99FF00","#7FFF00","#66FF00","#4CFF00","#33FF00","#19FF00","#00FF00","#00FF19","#00FF33","#00FF4C","#00FF66","#00FF7F","#00FF99","#00FFB2","#00FFCC","#00FFE5","#00FFFF","#00E5FF","#00CCFF","#00B2FF","#0099FF","#007FFF","#0066FF","#004CFF","#0033FF","#0019FF","#0000FF","#1900FF","#3300FF","#4C00FF","#6600FF","#7F00FF","#9900FF","#B200FF","#CC00FF","#E500FF","#FF00FF"]

def toggleCrashProt():
    global crashProt
    crashProt = not crashProt
    redraw()
crashProt = False
crashProtButton = tk.Checkbutton(root, text="Crash Protection", command=toggleCrashProt)
crashProtButton.pack( anchor="w", padx=30)

functionCounter = tk.Label(root, text=f"Functions used: {functionsUsed}")
functionCounter.pack(anchor="w", padx=35, pady=(20, 0))

start = float(0)
end = float(0)
timeElapsed = float(0)
elapsedCounter = tk.Label(root, text=f"Time elapsed: {timeElapsed}", width=20)
elapsedCounter.pack(anchor="w", padx=10)

previousFunction = var.get()
previousIter = iteration_slider.get()
previousSize = size_slider.get()
previousAngle = angle_slider.get()

def redraw():
    global functionsUsed
    functionsUsed = 0
    t.clear()
    t.penup()
    start = time.time()

    if var.get() == 1:
        t.setpos(-size_slider.get() / 2.0, -size_slider.get() / 2.0)
        t.setheading(90)
        t.pendown()

        PeanoCurve(iteration_slider.get(),3 * (size_slider.get() / ((3 ** (iteration_slider.get()) - 1))), angle_slider.get())

    elif var.get() == 2:
        t.setpos(-size_slider.get() / 2.0, size_slider.get() / 2.0)
        t.setheading(0)
        t.pendown()

        HilbertCurve(iteration_slider.get(), size_slider.get() / ((2 ** iteration_slider.get()) - 1), angle_slider.get())

    elif var.get() == 3:
        t.setpos(-size_slider.get() / 2.0 + 30, size_slider.get() / 2.0 - 100)
        t.setheading(0)
        t.pendown()

        DragonCurve(iteration_slider.get(), size_slider.get(), angle_slider.get(), 1)
    elif var.get() == 4:
        size = size_slider.get() * 2/3
        t.setpos(-size / 2.0, size / 2.0)
        t.setheading(0)
        t.pendown()

        DragonCurve(iteration_slider.get(), size, angle_slider.get(), 1)

    elif var.get() == 5:
        t.setpos(-size_slider.get() / 2.0, 0)
        t.setheading(0)
        t.pendown()

        KochCurve(iteration_slider.get(), size_slider.get(), angle_slider.get())

    elif var.get() == 6:
        t.setpos(0, -size_slider.get() * math.sqrt(2) / 2 + 50)
        t.setheading(120)
        t.pendown()

        for i in range(3):
            KochCurve(iteration_slider.get(),size_slider.get(), angle_slider.get())
            t.right(120)

    elif var.get() == 7:
        t.setpos(-size_slider.get() / 2, 0)
        t.setheading(0)
        t.pendown()

        MinkowskiSausage(iteration_slider.get(), size_slider.get(), angle_slider.get())
    elif var.get() == 8:
        size = size_slider.get() * 3/4
        t.setpos(-size / 2, size / 2)
        t.setheading(0)
        t.pendown()

        for i in range (4):
            MinkowskiSausage(iteration_slider.get(), size, angle_slider.get())
            t.right(90)

    end = time.time()
    timeElapsed = end - start
    elapsedCounter.config(text=f"Time elapsed: {round(timeElapsed, 3)}")
    screen.update()
def sliderCheck():
    global previousFunction, previousIter, previousSize, previousAngle

    if var.get() != previousFunction or iteration_slider.get() != previousIter or size_slider.get() != previousSize or angle_slider.get() != previousAngle:
        previousFunction = var.get()
        previousIter = iteration_slider.get()
        previousSize = size_slider.get()
        previousAngle = angle_slider.get()
        redraw()

    root.after(20, sliderCheck)

def PeanoCurve(iteration, size, angle):
    global functionsUsed
    functionsUsed += 1
    functionCounter.config(text=f"Functions used: {functionsUsed}")

    if iteration == 0:
        t.dot(0, "black")
        return
    
    if crashProt and functionsUsed > 10000:
        return

    if rainbow:
        t.pencolor(colors[round(functionsUsed / 9) % len(colors)])
        t.pensize(3)
    else:
        t.pencolor("black")
        t.pensize(1)

    PeanoCurve(iteration - 1, size, angle)
    t.forward(size / 3)
    PeanoCurve(iteration - 1, size, -angle)
    t.forward(size / 3)
    PeanoCurve(iteration - 1, size, angle)
    t.right(angle)
    t.forward(size / 3)

    t.right(angle)
    PeanoCurve(iteration - 1, size, -angle)
    t.forward(size / 3)
    PeanoCurve(iteration - 1, size, angle)
    t.forward(size / 3)
    PeanoCurve(iteration - 1, size, -angle)
    t.left(angle)
    t.forward(size / 3)

    t.left(angle)
    PeanoCurve(iteration - 1, size, angle)
    t.forward(size / 3)
    PeanoCurve(iteration - 1, size, -angle)
    t.forward(size / 3)
    PeanoCurve(iteration - 1, size, angle)

def HilbertCurve(iteration, size, angle):
    global functionsUsed
    functionsUsed += 1
    functionCounter.config(text=f"Functions used: {functionsUsed}")

    if iteration == 0:
        t.dot(0, "black")
        return
    
    if crashProt and functionsUsed > 10000:
        return

    if rainbow:
        t.pencolor(colors[round(functionsUsed / 4) % len(colors)])
        t.pensize(3)
    else:
        t.pencolor("black")
        t.pensize(1)

    t.right(angle)
    HilbertCurve(iteration - 1, size, -angle)

    t.forward(size)
    t.left(angle)
    HilbertCurve(iteration - 1, size, angle)

    t.forward(size)
    HilbertCurve(iteration - 1, size, angle)

    t.left(angle)
    t.forward(size)
    HilbertCurve(iteration - 1, size, -angle)
    t.right(angle)

def DragonCurve(iteration, lenght, angle, turningState):
    global functionsUsed, rainbow

    if rainbow:
        t.pencolor(colors[round(functionsUsed / 3) % len(colors)])
        t.pensize(2)
    else:
        t.pencolor("black")
        t.pensize(1)

    if crashProt and functionsUsed > 10000:
        return

    if iteration != 0:

        new_lenght = lenght / math.sqrt(2)

        t.right(angle / 2 * turningState)
        DragonCurve(iteration-1, new_lenght, angle, 1)
        t.left(angle * turningState)
        if var.get() == 3:
            DragonCurve(iteration-1, new_lenght, angle, -1)
        elif var.get() == 4:
            DragonCurve(iteration-1, new_lenght, angle, 1)
        t.right(angle / 2 * turningState)

    else:
        functionsUsed += 1
        functionCounter.config(text=f"Functions used: {functionsUsed}")
        t.pendown()
        t.forward(lenght)
        t.penup()

def KochCurve(iteration, length, angle):
    global functionsUsed, kochRatio
    functionsUsed += 1
    functionCounter.config(text=f"Functions used: {functionsUsed}")

    if iteration == 0:
        t.forward(length)
        t.dot(0, "black")
        return

    if crashProt and functionsUsed > 10000:
        return
    
    kochRatio =  2 + 2 * math.sin(math.radians(angle_slider.get()))

    if rainbow:
        t.pencolor(colors[round(functionsUsed / 4) % len(colors)])
        t.pensize(3)
    else:
        t.pencolor("black")
        t.pensize(1)


    KochCurve(iteration - 1, length / kochRatio, angle)
    t.left(90- angle)
    KochCurve(iteration - 1, length / kochRatio, angle)
    t.right(180 - angle * 2)
    KochCurve(iteration - 1, length / kochRatio, angle)
    t.left(90 - angle)
    KochCurve(iteration - 1, length / kochRatio, angle)
        
def MinkowskiSausage(iter, length, angle):
    global functionsUsed
    functionsUsed += 1
    functionCounter.config(text=f"Functions used: {functionsUsed}")

    if iter == 0:
        t.forward(length)
        t.dot(0, "black")
        return
    
    if crashProt and functionsUsed > 10000:
        return
    
    if rainbow:
        t.pencolor(colors[round(functionsUsed / 8) % len(colors)])
        t.pensize(3)
    else:
        t.pencolor("black")
        t.pensize(1)

    MinkowskiSausage(iter - 1, length / 4, angle)
    t.right(angle)
    MinkowskiSausage(iter - 1, length / 4, angle)
    t.left(angle)
    MinkowskiSausage(iter - 1, length / 4, angle)
    t.left(angle)
    MinkowskiSausage(iter - 1, length / 4, angle)
    MinkowskiSausage(iter - 1, length / 4, angle)
    t.right (angle)
    MinkowskiSausage(iter - 1, length / 4, angle)
    t.right(angle)
    MinkowskiSausage(iter - 1, length / 4, angle)
    t.left(angle)
    MinkowskiSausage(iter - 1, length / 4, angle)

redraw()
sliderCheck()
root.mainloop()
