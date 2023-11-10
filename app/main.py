import tkinter as tk


window = tk.Tk()

greeting = tk.Label(
        text="Hello, Tkinter",
        foreground='blue',
        background='white'
        )
greeting.pack()

window.mainloop()

