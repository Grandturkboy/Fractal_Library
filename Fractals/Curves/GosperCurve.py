import turtle
import tkinter as tk
import math

root = tk.Tk()
root.title("Gosper Curve Controls")

canvas = tk.Canvas(root, width=600, height=600)
canvas.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

screen = turtle.TurtleScreen(canvas)
screen.tracer(0, 0)
functionsUsed = 0
t = turtle.RawTurtle(screen)
t.hideturtle()
t.speed(0)

iteration_slider = tk.Scale(root, from_=0, to=14, resolution=1, orient="horizontal", label="Iterations")
iteration_slider.set(2)
iteration_slider.pack()

size_slider = tk.Scale(root, from_=1, to=500, resolution=10, orient="horizontal", label="Size")
size_slider.set(400)
size_slider.pack()

angle_slider = tk.Scale(root, from_=0, to=360, resolution=3, orient="horizontal", label="Angle")
angle_slider.set(60)
angle_slider.pack()

def toggleRainbow():
    global rainbow
    rainbow = not rainbow
    redraw()

rainbow = False
rainbowButton = tk.Checkbutton(root, text="Rainbow", command=toggleRainbow, width=20)
rainbowButton.pack()
colors = ["#FF0000","#FF1900","#FF3300","#FF4C00","#FF6600","#FF7F00","#FF9900","#FFB200","#FFCC00","#FFE500","#FFFF00","#E5FF00","#CCFF00","#B2FF00","#99FF00","#7FFF00","#66FF00","#4CFF00","#33FF00","#19FF00","#00FF00","#00FF19","#00FF33","#00FF4C","#00FF66","#00FF7F","#00FF99","#00FFB2","#00FFCC","#00FFE5","#00FFFF","#00E5FF","#00CCFF","#00B2FF","#0099FF","#007FFF","#0066FF","#004CFF","#0033FF","#0019FF","#0000FF","#1900FF","#3300FF","#4C00FF","#6600FF","#7F00FF","#9900FF","#B200FF","#CC00FF","#E500FF","#FF00FF"]


previousIter = iteration_slider.get()
previousSize = size_slider.get()
previousAngle = angle_slider.get()

functionCounter = tk.Label(root, text=f"Functions used: {functionsUsed}")
functionCounter.pack()

def GosperCurve( iteration, size, angle, isA):
    global functionsUsed
    functionsUsed += 1
    functionCounter.config(text=f"Functions used: {functionsUsed}")

    if iteration <= 0:
        t.forward(size)
        return
    
    if rainbow:
        t.pencolor(colors[round(functionsUsed / 7) % len(colors)])
        t.pensize(3)
    else:
        t.pencolor("black")
        t.pensize(1)

    if isA:
        GosperCurve(iteration - 1, size, angle, True)
        t.right(angle)
        GosperCurve(iteration - 1, size, angle, False)
        t.right(2 * angle)
        GosperCurve(iteration - 1, size, angle, False)
        t.left(angle)
        GosperCurve(iteration - 1, size, angle, True)
        t.left(2 * angle)
        GosperCurve(iteration - 1, size, angle, True)
        GosperCurve(iteration - 1, size, angle, True)
        t.left(angle)
        GosperCurve(iteration - 1, size, angle, False)
        t.right(angle)
    else:
        t.left(angle)
        GosperCurve(iteration - 1, size, angle, True)
        t.right(angle)
        GosperCurve(iteration - 1, size, angle, False)
        GosperCurve(iteration - 1, size, angle, False)
        t.right(2 * angle)
        GosperCurve(iteration - 1, size, angle, False)
        t.right(angle)
        GosperCurve(iteration - 1, size, angle, True)
        t.left(2 * angle)
        GosperCurve(iteration - 1, size, angle, True)
        t.left(angle)
        GosperCurve(iteration - 1, size, angle, False)


def redraw():
    global functionsUsed
    functionsUsed = 0
    t.clear()
    t.penup()
    t.setpos(-size_slider.get() / 2, size_slider.get() * math.sqrt(3) / 6)
    t.setheading(0 + iteration_slider.get() * angle_slider.get() / 3)
    t.pendown()

    scale = 1 / (2 * math.cos(math.radians(angle_slider.get() / 2)) + 1)
    length = size_slider.get() * (scale ** iteration_slider.get())

    GosperCurve(iteration_slider.get(), length, angle_slider.get(), True)
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
