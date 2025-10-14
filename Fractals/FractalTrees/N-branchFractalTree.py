import turtle
import tkinter as tk
import time

root = tk.Tk()
root.title("Fractal Tree Controls")

canvas = tk.Canvas(root, width=800, height=600)
canvas.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

screen = turtle.TurtleScreen(canvas)
screen.tracer(0, 0)

t = turtle.RawTurtle(screen)
t.hideturtle()
t.speed(0)
t.left(90)
functionsUsed = 0
start = float(0)
end = float(0)

iteration_slider = tk.Scale(root, from_=0, to=15, resolution=1,
                        orient="horizontal", label="Depth")
iteration_slider.set(10)
iteration_slider.pack()

angle_slider = tk.Scale(root, from_=0, to=180, resolution=1,
                        orient="horizontal", label="Branch Angle")
angle_slider.set(30)
angle_slider.pack()

shrink_slider = tk.Scale(root, from_=0.1, to=0.8, resolution=0.01,
                         orient="horizontal", label="Shrink Factor")
shrink_slider.set(0.75)
shrink_slider.pack()

length_slider = tk.Scale(root, from_=50, to=300, resolution=5,
                         orient="horizontal", label="Initial Length")
length_slider.set(100)
length_slider.pack()

branch_slider = tk.Scale(root, from_=1, to=10, resolution=1,
                         orient="horizontal", label="Branches")
branch_slider.set(2)
branch_slider.pack()

crashLabel = tk.Label(root, text=("Crash Prevention"))
crashLabel.pack()
crash_slider = tk.Scale(root, from_=0, to=1, orient="horizontal", length=50, )
crash_slider.set(1)
crash_slider.pack()

functionCounter = tk.Label(root, text=f"Functions used: {functionsUsed}", width=20)
functionCounter.pack()

timeElapsed = float(0)
elapsedCounter = tk.Label(root, text=f"Time elapsed: {timeElapsed}", width=20)
elapsedCounter.pack()

prevousIter = iteration_slider.get()
prevousAngle = angle_slider.get()
prevousShrink = shrink_slider.get()
prevousLength = length_slider.get()
prevousBranch = branch_slider.get()
prevousCrashPos = crash_slider.get()

def drawBranch(length, t, angle, shrink, branches, iter):
    global functionsUsed, start, end, timeElapsed

    if iter < 1:
        end = time.time()
        timeElapsed = end - start
        elapsedCounter.config(text=f"Time elapsed: {round(timeElapsed, 3)}")
        return

    if crash_slider.get() == 1 and functionsUsed > 10000:
        t.penup()
        return
    
        
    totalAngle = (branches - 1) * angle
    saved = t.heading()
    
    t.forward(length)
    t.left(totalAngle / 2)
    
    for i in range(branches):
        drawBranch(length * shrink, t, angle, shrink, branches, iter-1)
        t.right(angle)

    t.setheading(saved)
    t.backward(length)

    functionsUsed += 1
    functionCounter.config(text=f"Functions used: {functionsUsed}")
def sliderCheck():
    global prevousBranch, prevousAngle, prevousCrashPos, prevousIter, prevousLength, prevousShrink
    currentIter = iteration_slider.get()
    currentAngle = angle_slider.get()
    currentShrink = shrink_slider.get()
    currentLength = length_slider.get()
    currentBranch = branch_slider.get()
    currentCrashPos = crash_slider.get()
    if (currentIter != prevousIter or currentAngle != prevousAngle or
        currentShrink != prevousShrink or currentLength != prevousLength or
        currentBranch != prevousBranch or currentCrashPos != prevousCrashPos):
        prevousIter = currentIter
        prevousAngle = currentAngle
        prevousShrink = currentShrink
        prevousLength = currentLength
        prevousBranch = currentBranch
        prevousCrashPos = currentCrashPos
        redraw()
    root.after(10, sliderCheck)



def redraw():
    global functionsUsed, start
    functionsUsed = 0
    t.clear()
    t.penup()
    t.goto(0, -200)
    t.setheading(90)
    t.pendown()
    
    if branch_slider.get() % 2 == 0:
        start = time.time()
        drawBranch(length_slider.get(), t, angle_slider.get() * 2, shrink_slider.get(), branch_slider.get(), iteration_slider.get())
    else:
        start = time.time()
        drawBranch(length_slider.get(), t, angle_slider.get(), shrink_slider.get(), branch_slider.get(), iteration_slider.get())

    screen.update()

redraw()
sliderCheck()

root.mainloop()
