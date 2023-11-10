import tkinter as tk


window = tk.Tk()


text_duende_verde = [
    ['Verde', 'Planador', 'Duende'],
    ['Bomba', 'Odeia homem aranha', 'filho'],
    ['Drogado', 'Cientista', 'Capitão américa']
]

for i in range(3):
    for j in range(3):
        frame = tk.Frame(
            master=window,
            relief=tk.RAISED,
            borderwidth=1
        )
        frame.grid(row=i, column=j, padx=5, pady=5)
        label = tk.Label(master=frame, text=f"{text_duende_verde[i][j]}")
        label.pack(padx=5, pady=5)

window.mainloop()

