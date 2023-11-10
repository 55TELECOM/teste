import tkinter as tk
from selenium.webdriver import Chrome
from time import sleep

window = tk.Tk()

greeting = tk.Label(
        text="Spider man 2 goty",
        foreground='blue',
        background='white'
        )

def openTabGoogle():
    service = Chrome()
    tab = service.get("https://pt.wikipedia.org/wiki/Duende_Verde")
    sleep(10)
    tab.quit()
    
button = tk.Button(window,text="Spider man 3", command=openTabGoogle )
button.place(x=50, y=50)

greeting.pack()

window.mainloop()

