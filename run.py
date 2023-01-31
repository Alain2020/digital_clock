# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
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