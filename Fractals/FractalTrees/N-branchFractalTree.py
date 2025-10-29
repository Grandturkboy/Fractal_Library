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
up = True

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

def CrashToggle():
    global canCrash
    canCrash = not canCrash
    redraw()

canCrash = False
crashButton = tk.Checkbutton(root, text="Crash Prevention", width=20, command=CrashToggle)
crashButton.pack()


def animateToggle():
    global animate
    animate = not animate
    redraw()

animate = False
animateButton = tk.Checkbutton(root, text=" Animate it ", command=animateToggle, width=20)
animateButton.pack()

def wideToggle():
    global wide
    wide = not wide
    redraw()

wide = False
wideButton = tk.Checkbutton(root, text="Wide", command=wideToggle, width=20)
wideButton.pack()

def rainbowToggle():
    global rainbow
    rainbow = not rainbow
    redraw()

rainbow = False
rainbowButton = tk.Checkbutton(root, text="Rainbow", command=rainbowToggle, width=20)
rainbowButton.pack()
colors = ["#FF0000","#FF1900","#FF3300","#FF4C00","#FF6600","#FF7F00","#FF9900","#FFB200","#FFCC00","#FFE500","#FFFF00","#E5FF00","#CCFF00","#B2FF00","#99FF00","#7FFF00","#66FF00","#4CFF00","#33FF00","#19FF00","#00FF00","#00FF19","#00FF33","#00FF4C","#00FF66","#00FF7F","#00FF99","#00FFB2","#00FFCC","#00FFE5","#00FFFF","#00E5FF","#00CCFF","#00B2FF","#0099FF","#007FFF","#0066FF","#004CFF","#0033FF","#0019FF","#0000FF","#1900FF","#3300FF","#4C00FF","#6600FF","#7F00FF","#9900FF","#B200FF","#CC00FF","#E500FF","#FF00FF"]


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

def drawBranch(length, t, angle, shrink, branches, iter):
    global functionsUsed, start, end, timeElapsed, max_iter

    if iter < 1:
        end = time.time()
        timeElapsed = end - start
        elapsedCounter.config(text=f"Time elapsed: {round(timeElapsed, 3)}")
        return

    if canCrash == True and functionsUsed > 10000:
        t.penup()
        return
    
    if rainbow == True:
        max_iter = iteration_slider.get()
        color_index = int((max_iter - iter) / max_iter * (len(colors) - 1))
        t.pencolor(colors[color_index])
    else:
        t.pencolor("black")

    if wide == True:
        t.pensize(max(2, iter / max_iter * 16))
    else:
        t.pensize(1)
        
    totalAngle = (branches - 1) * angle
    saved = t.heading()
    
    t.forward(length)
    t.left(totalAngle / 2)
    
    for i in range(branches):
        drawBranch(length * shrink, t, angle, shrink, branches, iter-1)
        t.right(angle)

    t.setheading(saved)
    t.penup()  
    t.backward(length)
    t.pendown()

    functionsUsed += 1
    functionCounter.config(text=f"Functions used: {functionsUsed}")
def sliderCheck():
    global prevousBranch, prevousAngle, prevousCrashPos, prevousIter, prevousLength, prevousShrink
    currentIter = iteration_slider.get()
    currentAngle = angle_slider.get()
    currentShrink = shrink_slider.get()
    currentLength = length_slider.get()
    currentBranch = branch_slider.get()
    if (currentIter != prevousIter or currentAngle != prevousAngle or
        currentShrink != prevousShrink or currentLength != prevousLength or
        currentBranch != prevousBranch):
        prevousIter = currentIter
        prevousAngle = currentAngle
        prevousShrink = currentShrink
        prevousLength = currentLength
        prevousBranch = currentBranch
        redraw()
    root.after(10, sliderCheck)



def redraw():
    global functionsUsed, start, max_iter, up
    functionsUsed = 0
    t.clear()
    t.penup()
    t.goto(0, -200)
    t.setheading(90)
    t.pendown()
    
    max_iter = iteration_slider.get()
    start = time.time()
    drawBranch(length_slider.get(), t, angle_slider.get(), shrink_slider.get(), branch_slider.get(), iteration_slider.get())

    if animate:
        if up == True:
            angle_slider.set(angle_slider.get() + 2)
            if angle_slider.get() >= 180:
                up = False
        else:
            angle_slider.set(angle_slider.get() - 2)
            if angle_slider.get() <= 0:
                up = True
    screen.update()

redraw()
sliderCheck()
root.mainloop()
