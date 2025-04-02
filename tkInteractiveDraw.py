import tkinter as tk

root = tk.Tk()
canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()

def draw_dot(event):
    x, y = event.x, event.y
    canvas.create_oval(x-2, y-2, x+2, y+2, fill='black')

canvas.bind('<1>', draw_dot)  # Bind left mouse button click event

root.mainloop()