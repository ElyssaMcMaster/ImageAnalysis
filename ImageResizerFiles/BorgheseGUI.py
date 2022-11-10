from tkinter import messagebox
from tkinter import ttk


from tkinter.filedialog import askdirectory

print("select the folder of images to resize them")
path1 = askdirectory()
print("select the folder to save the resized images to")
path2 = askdirectory()