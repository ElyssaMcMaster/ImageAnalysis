import tkinter as tk
from tkinter import messagebox
from tkinter.filedialog import askdirectory

root=tk.Tk()
root.withdraw()

print("select the folder of images to resize them")
path1 = askdirectory()
print("select the folder to save the resized images to")
path2 = askdirectory()