from PIL import Image 
import glob
import BorgheseGUI
import os


image_list = []
resized_images = []
image_names=[]
shortimagenames=[]

for filename in glob.glob(BorgheseGUI.path1 + "/*.jpg"):
    #print(filename)
    img = Image.open(filename)
    image_names.append(filename)
    print(img.size)
    image_list.append(img)
    print(filename)

savedims = image_list[0].size
#print(savedims)
#print(image_names)

for item in image_list:
    if item.size < savedims:
        savedims = item.size

print("The size of all the images will be ", savedims)

for image in image_list:
    #image.show()
    image = image.resize((savedims))
    #print(type(image))
    resized_images.append(image)


stringpath = str(BorgheseGUI.path1)

for item in image_names:
    item = item.replace(stringpath,'')
    shortimagenames.append(item)

print(shortimagenames)

'''
for (i, new) in enumerate(resized_images):
    new.save('{} {} {}'.format(BorgheseGUI.path2, i+1, '.jpg'))
'''

for (i, new) in enumerate(resized_images):
    new.save('{}{}{}'.format(BorgheseGUI.path2, shortimagenames[i], '_resized.jpg'))
    i+=1

