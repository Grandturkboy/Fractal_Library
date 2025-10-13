import turtle
import tkinter as tk

# --- setup tkinter window ---
root = tk.Tk()
root.title("Fractal Tree Controls")

# --- create a Canvas ---
canvas = tk.Canvas(root, width=800, height=600)
canvas.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

# --- create turtle screen ---
screen = turtle.TurtleScreen(canvas)
screen.tracer(0, 0)

t = turtle.RawTurtle(screen)
t.hideturtle()
t.speed(0)
t.left(90)

# --- sliders ---
ratio_slider = tk.Scale(root, from_=0.5, to=0.9, resolution=0.01,
                        orient="horizontal", label="Shrink Ratio")
ratio_slider.set(0.75)
ratio_slider.pack()

deg_slider = tk.Scale(root, from_=5, to=180, resolution=1,
                      orient="horizontal", label="Turning Angle")
deg_slider.set(30)
deg_slider.pack()

length_slider = tk.Scale(root, from_=50, to=300, resolution=1,
                         orient="horizontal", label="Branch Length")
length_slider.set(100)
length_slider.pack()

iter_slider = tk.Scale(root, from_=3, to=8, resolution=1,
                       orient="horizontal", label="Depth")
iter_slider.set(5)
iter_slider.pack()


# --- drawing function ---
def drawBranch(n, length, t, ratio, deg):
    if n < 1:
        return
    t.forward(length)
    t.right(deg / 2)
    drawBranch(n - 1, length * ratio, t, ratio, deg)
    t.right(deg)
    drawBranch(n - 1, length * ratio, t, ratio, deg)
    t.left(2 * deg)
    drawBranch(n - 1, length * ratio, t, ratio, deg)
    t.left(deg)
    drawBranch(n - 1, length * ratio, t, ratio, deg)
    t.right(deg * 1.5)
    t.backward(length)


# --- continuous redraw ---
def continuous_redraw():
    t.clear()
    t.penup()
    t.goto(0, -250)
    t.setheading(90)
    t.pendown()

    ratio = ratio_slider.get()
    deg = deg_slider.get()
    length = length_slider.get()
    iterations = iter_slider.get()

    drawBranch(iterations, length, t, ratio, deg)
    screen.update()

    root.after(10, continuous_redraw)  # redraw every 10 ms


# --- start ---
continuous_redraw()
root.mainloop()
