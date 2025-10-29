import turtle
import tkinter as tk

root = tk.Tk()
root.title("Mandelbrod Set Controls")

CANVAS_SIZE = 400
canvas = tk.Canvas(root, width=CANVAS_SIZE, height=CANVAS_SIZE)
canvas.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

screen = turtle.TurtleScreen(canvas)
screen.tracer(0, 0)
functionsUsed = 0
t = turtle.RawTurtle(screen)
t.hideturtle()
t.speed(0)
t.penup()

zoomSlider = tk.Scale(root, from_=1, to=10, resolution=0.1, orient="horizontal", label="Zoom")
zoomSlider.set(1)
zoomSlider.pack()

xOffsetSlider = tk.Scale(root, from_=-4, to=4, resolution=0.1, orient="horizontal", label="X Offset")
xOffsetSlider.set(0)
xOffsetSlider.pack()

yOffsetSlider = tk.Scale(root, from_=-4, to=4, resolution=0.1, orient="horizontal", label="Y Offset")
yOffsetSlider.set(0)
yOffsetSlider.pack()

detailSlider1 = tk.Scale(root, from_=1, to=100, resolution=1, orient="horizontal", label="Detail")
detailSlider1.set(40)
detailSlider1.pack()

detailSlider2 = tk.Scale(root, from_=2, to=10, resolution=1, orient="horizontal", label="Detail")
detailSlider2.set(5)
detailSlider2.pack()

pointsCounter = tk.Label(root, text=f"Points drawn: {functionsUsed}", width=20)
pointsCounter.pack()

radius = 2.0
tries = detailSlider1.get()
detail = round(CANVAS_SIZE / detailSlider2.get())
functionsUsed = 0

PrevousZoom = zoomSlider.get()
PreviousxOffset = xOffsetSlider.get()
PreviousyOffset = yOffsetSlider.get()

def drawMandelbrot(minX, maxX, minY, maxY, xOffset, yOffset):
    global functionsUsed
    functionsUsed = 0

    xUnit = (maxX - minX) / detail
    yUnit = (maxY - minY) / detail

    screenScaleX = CANVAS_SIZE / (maxX - minX) 
    screenScaleY = CANVAS_SIZE / (maxY - minY)

    for i in range(detail):
        y = minY + (i + 0.5) * yUnit
        for j in range(detail):
            x = minX + (j + 0.5) * xUnit
            c = complex(x, y)
            z = 0 + 0j
            for a in range(tries):
                z = z * z + c
                if abs(z) > radius:
                    break
            else:
                screenX = (x - xOffset) * screenScaleX
                screenY = (y - yOffset) * screenScaleY
                t.goto(screenX, screenY)
                t.dot(screenScaleX / (zoomSlider.get() * detail / 5), "#000000")
                functionsUsed += 1

    screen.update()
    pointsCounter.config(text=f"Points drawn: {functionsUsed}")

def redraw():
    Zoom = zoomSlider.get()
    xOffset = xOffsetSlider.get()
    yOffset = yOffsetSlider.get()

    viewWidth = 4 / Zoom
    viewHeight = 4 / Zoom

    minX = xOffset - viewWidth / 2
    maxX = xOffset + viewWidth / 2
    minY = yOffset - viewHeight / 2
    maxY = yOffset + viewHeight / 2

    t.clear()

    drawMandelbrot(minX, maxX, minY, maxY, xOffset, yOffset)

def sliderCheck():
    global PrevousZoom, PreviousxOffset, PreviousyOffset, tries, detail

    if zoomSlider.get() != PrevousZoom or xOffsetSlider.get() != PreviousxOffset or yOffsetSlider.get() != PreviousyOffset or detailSlider1.get() != tries or detailSlider2.get() != detail:
        PrevousZoom = zoomSlider.get()
        PreviousxOffset = xOffsetSlider.get()
        PreviousyOffset = yOffsetSlider.get()
        tries = detailSlider1.get()
        detail = round(CANVAS_SIZE / detailSlider2.get())
        redraw()
    root.after(30, sliderCheck)

redraw()
sliderCheck()
root.mainloop()

        
