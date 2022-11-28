import tkinter as tk
from tkinter import messagebox
from tkinter.filedialog import askdirectory

root=tk.Tk()
root.title='Pick a file type'
root.geometry('600x400+50+50')
filetype = ''

jpgbutton = tk.Button(root, text = '.jpg',
                    command=lambda: pickjpg(), height = 10, width = 10)

jpgbutton.pack()

tifbutton = tk.Button(root, text = '.tif', 
                        command=lambda:picktif(), height = 10, width = 10)
tifbutton.pack()


def picktif():
    # output message to terminal to show button is working
    print("tif selected")
    filetype = '.tif'
    root.destroy()
    return filetype
    

def pickjpg():
    print('jpg selected')
    filetype = '.jpg'
    root.destroy()
    return filetype
    
print(filetype)




root.mainloop()

print("select the folder of images to resize them")
path1 = askdirectory()
print("select the folder to save the resized images to")
path2 = askdirectory()

