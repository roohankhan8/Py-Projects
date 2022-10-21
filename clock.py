import imp
from tk import *
from tk import font
from tk.ttk import *

from time import strftime

root = Tk()
root.title = 'Clock'

def time():
    string = strftime('%H:%M:%S %p')
    label.config(text=string)
    label.after(1000, time)


label = Label(root, foreground='cyan',background='black')
label.pack(anchor='center')

time()

mainloop()