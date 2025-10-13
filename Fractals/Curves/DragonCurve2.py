import turtle
import tkinter as tk
import math

root = tk.Tk()
root.title("Dragon Curve Controls")

canvas = tk.Canvas(root, width=800, height=600)
canvas.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

screen = turtle.TurtleScreen(canvas)
screen.tracer(0, 0)
functionsUsed = 0

t = turtle.RawTurtle(screen)
t.hideturtle()
t.speed(0)

iteration_slider = tk.Scale(root, from_=0, to=14, resolution=1, orient="horizontal", label="Iterations")
iteration_slider.set(10)
iteration_slider.pack()

functionCounter = tk.Label(root, text=f"Functions used: {functionsUsed}")
functionCounter.pack()

previousIteration = iteration_slider.get()

def drawCurve(deg, lenght, iteration, startX, startY, turningState):
    global functionsUsed

    if iteration != 0:

        new_lenght = lenght / math.sqrt(2)

        t.penup()
        t.setpos(startX, startY)
        t.pendown()

        t.right(deg / 2 * turningState)
        drawCurve(deg, new_lenght, iteration-1, t.xcor(), t.ycor(), 1)
        t.left(deg * turningState)
        drawCurve(deg, new_lenght, iteration-1, t.xcor(), t.ycor(), -1)
        t.right(deg / 2 * turningState)

    else:
        functionsUsed += 1
        functionCounter.config(text=f"Functions used: {functionsUsed}")
        t.penup()
        t.setpos(startX, startY)
        t.pendown() 
        t.forward(lenght)
        t.penup()
        
        return
def redraw():
    global functionsUsed
    functionsUsed = 0
    t.clear()
    t.penup()
    drawCurve(deg=90, lenght=400, iteration=iteration_slider.get(), startX=-200, startY=0, turningState=1)

def hasIterationChanged():
    global previousIteration
    current = iteration_slider.get()
    if current != previousIteration:
        redraw()
        previousIteration = current
    root.after(100, hasIterationChanged)


drawCurve(deg=90, lenght=400, iteration=10, startX=-200, startY=0, turningState=1)

screen.update()
hasIterationChanged()
root.mainloop()
