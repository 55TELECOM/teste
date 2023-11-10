import tkinter as tk
from selenium.webdriver import Chrome
from time import sleep

window = tk.Tk()
greeting = tk.Label(
        text="Spider man 2 goty",
        foreground='blue',
        background='white'
        )
# text_duende_verde = [
#     ['Verde', 'Planador', 'Duende'],
#     ['Bomba', 'Odeia homem aranha', 'filho'],
#     ['Drogado', 'Cientista', 'Capitão américa']
# ]
#
# for i in range(3):
#     for j in range(3):
#         frame = tk.Frame(
#             master=window,
#             relief=tk.RAISED,
#             borderwidth=1
#         )
#         frame.grid(row=i, column=j, padx=5, pady=5)
#         label = tk.Label(master=frame, text=f"{text_duende_verde[i][j]}")
#         label.pack(padx=5, pady=5)


def openTabGoogle():
    service = Chrome()
    tab = service.get("https://pt.wikipedia.org/wiki/Duende_Verde")
    sleep(10)
    tab.quit()


button = tk.Button(window, text="Spider man 3", command=openTabGoogle)
button.place(x=50, y=50)

greeting.pack()

window.mainloop()

