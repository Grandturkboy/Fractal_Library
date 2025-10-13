import turtle
import tkinter as tk

permut = 4
size = 243
points = [[size, -size], [-size, -size], [-size, size], [size, size]]

functionsUsed = 0

root = tk.Tk()
root.title("Carpet Controls(lol)")

canvas = tk.Canvas(root, width=800, height=600)
canvas.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

screen = turtle.TurtleScreen(canvas)
screen.tracer(0, 0)

t = turtle.RawTurtle(screen)
t.hideturtle()
t.speed(0)

iteration_slider = tk.Scale(root, from_=0, to=4, resolution=1, orient="horizontal", label="Iterations")
iteration_slider.set(3)
iteration_slider.pack()

size_slider = tk.Scale(root, from_=90, to=729, resolution=9, orient="horizontal", label="Size")
size_slider.set(243)
size_slider.pack()

functionCounter = tk.Label(root, text=f"Functions used: {functionsUsed}")
functionCounter.pack()

previousIteration = iteration_slider.get()
previousSize = size_slider.get()

def roundPoints(points):
    return [[round(x), round(y)] for x, y in points]

def drawSquare(points, color, myTurtle):
    global functionsUsed
    functionsUsed += 1
    functionCounter.config(text=f"Functions used: {functionsUsed}")

    points = roundPoints(points)
    myTurtle.up()
    myTurtle.goto(points[0][0], points[0][1])
    myTurtle.down()
    myTurtle.fillcolor(color)
    myTurtle.begin_fill()
    for p in points[1:] + [points[0]]:
        myTurtle.goto(p[0], p[1])
    myTurtle.end_fill()
    myTurtle.up()

def innerSquare(points):
    x0, y0 = points[0]
    x1, y1 = points[1]
    x2, y2 = points[2]
    x3, y3 = points[3]

    width = x1 - x0
    height = y3 - y0

    new_points = [
        [x0 + width / 3, y0 + height / 3],
        [x1 - width / 3, y1 + height / 3],
        [x2 - width / 3, y2 - height / 3],
        [x3 + width / 3, y3 - height / 3]
    ]

    return new_points
def subdivideSquare(points):
    x0, y0 = points[0]
    x1, y1 = points[1]
    x2, y2 = points[2]
    x3, y3 = points[3]

    width = (x1 - x0) / 3
    height = (y3 - y0) / 3 

    squares = []
    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1:
                continue
            bl = [x0 + i*width, y0 + j*height]
            br = [bl[0] + width, bl[1]]
            tr = [br[0], br[1] + height]
            tl = [bl[0], bl[1] + height]
            
            squares.append([bl, br, tr, tl])
    return squares

def carpet(points, permut, myTurtle):
    if permut == 0:
        drawSquare(innerSquare(roundPoints(points)), "white",t)
        return
    else:
        drawSquare(innerSquare(roundPoints(points)), "white",t)
        new_points = subdivideSquare(roundPoints(points))
        for p in new_points:
            carpet(p, permut - 1, myTurtle)
def redraw():
    size = size_slider.get()
    permut = iteration_slider.get()
    t.clear()
    points = [[size, -size], [-size, -size], [-size, size], [size, size]]
    drawSquare(points, "black", t)
    drawSquare(innerSquare(points), "white",t )
    carpet(points, permut, t)
    screen.update()

def haveSlidersChanged():
    global previousIteration, previousSize, functionsUsed
    current_iter = iteration_slider.get()
    current_size = size_slider.get()
    if current_iter != previousIteration or current_size != previousSize:
        redraw()
        functionsUsed = 0
        previousIteration = current_iter
        previousSize = current_size
    root.after(10, haveSlidersChanged)

drawSquare(points, "black",t)
drawSquare(innerSquare(points), "white",t)
carpet(points, permut, t)

haveSlidersChanged()
root.mainloop()
