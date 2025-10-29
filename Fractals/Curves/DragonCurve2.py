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

previousIteration = iteration_slider.get()

def drawCurve(deg, lenght, iteration, startX, startY, turningState):
    global functionsUsed, rainbow

    if rainbow:
        t.pencolor(colors[functionsUsed % len(colors)])
        t.pensize(2)
    else:
        t.pencolor("black")
        t.pensize(1)

    t.pensize(2)
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
