#pip install tk
import tkinter as tk

class MyGUI:
    def __init__(self, master):
        self.master = master
        master.title("Basic GUI")
        master.geometry("400x400")

        self.label = tk.Label(master, text="Hello CIS 314!")
        self.label.pack()

        self.button = tk.Button(master, text="Quit", command=master.quit)
        self.button.pack()

root = tk.Tk()
dane_gui = MyGUI(root)
root.mainloop()