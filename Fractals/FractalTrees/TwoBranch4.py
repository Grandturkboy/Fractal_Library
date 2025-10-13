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
angle_slider = tk.Scale(root, from_=0, to=180, resolution=1,
                        orient="horizontal", label="Branch Angle")
angle_slider.set(30)
angle_slider.pack()

shrink_slider = tk.Scale(root, from_=0.5, to=0.8, resolution=0.01,
                         orient="horizontal", label="Shrink Factor")
shrink_slider.set(0.75)
shrink_slider.pack()

length_slider = tk.Scale(root, from_=50, to=150, resolution=1,
                         orient="horizontal", label="Initial Length")
length_slider.set(100)
length_slider.pack()

# --- recursive drawing function ---
def drawBranch(n, t, angle, shrink):
    if n < 5:
        return
    t.forward(n)
    t.left(angle)
    drawBranch(n * shrink, t, angle, shrink)
    t.right(2 * angle)
    drawBranch(n * shrink, t, angle, shrink)
    t.left(angle)
    t.backward(n)

# --- update function (called repeatedly) ---
def continuous_redraw():
    t.clear()
    t.penup()
    t.goto(0, -200)
    t.setheading(90)
    t.pendown()
    drawBranch(length_slider.get(), t, angle_slider.get(), shrink_slider.get())
    screen.update()
    # Schedule next redraw in 100 ms
    root.after(10, continuous_redraw)

# --- start continuous rendering ---
continuous_redraw()

root.mainloop()
