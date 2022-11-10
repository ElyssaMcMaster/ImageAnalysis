from PIL import Image 
import glob
import BorgheseGUI
from pathlib import Path



image_list = []
resized_images = []
filenames=[]
destdir=BorgheseGUI.path2
newfilenames=[]


for filename in glob.glob(BorgheseGUI.path1 + "/*.jpg"):
    #print(filename)
    img = Image.open(filename)
    print(img.size)
    image_list.append(img)
    filenames.append(filename)


savedims = image_list[0].size
#print(filenames)
#print(savedims)


for item in image_list:
    if item.size < savedims:
        savedims = item.size


for filename in filenames:
    filename=filename.strip(BorgheseGUI.path1)
    newfilenames.append(str(filename))
    
#print(newfilenames)

print("The lowest number of pixels in this batch of images is", savedims)

for image in image_list:
    #image.show()
    image = image.resize((savedims))

    #print(type(image))
    resized_images.append(image)

for i in resized_images:
    for item in newfilenames:
        resized_images[-1].save(destdir+'/'+'resized_'+ item)

