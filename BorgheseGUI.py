import tkinter
from tkinter import messagebox
from tkinter import ttk
import os
import shutil

from tkinter.filedialog import askdirectory

'''
#window.mainloop()
win= tkinter.Tk()

# Set the size of the tkinter window
win.geometry("700x350")


ttk.Button(win, text= "Click Here").pack(pady= 20)
path1 = askdirectory()
win.mainloop()

'''
print("select the folder of images to resize them")
path1 = askdirectory()
print("select the folder to save the resized images to")
path2 = askdirectory()