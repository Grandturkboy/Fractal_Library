import turtle
import tkinter as tk


root = tk.Tk()
root.title("Hilbert Curve Controls")

canvas = tk.Canvas(root, width=600, height=600)
canvas.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

screen = turtle.TurtleScreen(canvas)
screen.tracer(0, 0)
functionsUsed = 0
t = turtle.RawTurtle(screen)
t.hideturtle()
t.speed(0)

iteration_slider = tk.Scale(root, from_=0, to=14, resolution=1, orient="horizontal", label="Iterations")
iteration_slider.set(4)
iteration_slider.pack()

size_slider = tk.Scale(root, from_=1, to=500, resolution=10, orient="horizontal", label="Size")
size_slider.set(400)
size_slider.pack()

angle_slider = tk.Scale(root, from_=0, to=360, resolution=3, orient="horizontal", label="Angle")
angle_slider.set(90)
angle_slider.pack()

previousIter = iteration_slider.get()
previousSize = size_slider.get()
previousAngle = angle_slider.get()

functionCounter = tk.Label(root, text=f"Functions used: {functionsUsed}")
functionCounter.pack()

def hilbertIt(iter, angle, length):
    global functionsUsed

    if iter == 0:
        return
    functionsUsed += 1
    functionCounter.config(text=f"Functions used: {functionsUsed}")

    t.right(angle)
    hilbertIt(iter - 1, -angle, length)

    t.forward(length)
    t.left(angle)
    hilbertIt(iter - 1, angle, length)

    t.forward(length)
    hilbertIt(iter - 1, angle, length)

    t.left(angle)
    t.forward(length)
    hilbertIt(iter - 1, -angle, length)
    t.right(angle)

def redraw():
    global functionsUsed
    functionsUsed = 0
    t.clear()
    t.penup()
    t.setpos(-size_slider.get() / 2.0, size_slider.get() / 2.0)
    t.pendown()

    hilbertIt(iter = iteration_slider.get(), angle = angle_slider.get(), length = size_slider.get() / (2 ** iteration_slider.get()))
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
