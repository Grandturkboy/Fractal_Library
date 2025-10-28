import turtle
import tkinter as tk
import math


root = tk.Tk()
root.title("Koch Curve Controls")

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

size_slider = tk.Scale(root, from_=0, to=1000, resolution=10, orient="horizontal", label="Size")
size_slider.set(400)
size_slider.pack()

angle_slider = tk.Scale(root, from_=0, to=180, resolution=3, orient="horizontal", label="Angle")
angle_slider.set(45)    
angle_slider.pack()

previousIter = iteration_slider.get()
previousSize = size_slider.get()
previousAngle = angle_slider.get()

functionCounter = tk.Label(root, text=f"Functions used: {functionsUsed}")
functionCounter.pack()
 
kochRatio = 2 + 2 * math.sin(math.radians(angle_slider.get()) / 2)

def KochIt(iter, angle, length):
    global functionsUsed, kochRatio

    if iter == 0:
        t.forward(length)
        return

    functionsUsed += 1
    functionCounter.config(text=f"Functions used: {functionsUsed}")

    KochIt(iter - 1, angle, length / kochRatio)
    t.left(90- angle)
    KochIt(iter - 1, angle, length / kochRatio)
    t.right(180 - angle * 2)
    KochIt(iter - 1, angle, length / kochRatio)
    t.left(90 - angle)
    KochIt(iter - 1, angle, length / kochRatio)

def redraw():
    global functionsUsed
    functionsUsed = 0
    t.clear()
    t.penup()
    t.setpos(-200, 0)
    t.setheading(0)
    t.pendown()

    kochRatio =  2 + 2 * math.sin(math.radians(angle_slider.get()))

    for i in range(3):
        KochIt(iter = iteration_slider.get(), angle = angle_slider.get(), length = (3 * size_slider.get() / kochRatio) * 0.8095 ** iteration_slider.get())
        t.right(120)
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
