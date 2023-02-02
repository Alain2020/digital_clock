
from tkinter import *
from time import *

def update():
    time_string = strftime("%I%M%S")
    time_label.config(text=time_string)
window = Tk()

time_label = Label(window,font=("Arial",50),fg="#00FF00",bg="black")
time_label.pack()

update()

window.mainloop()