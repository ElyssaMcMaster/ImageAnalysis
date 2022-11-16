from PIL import Image 
import glob
import BorgheseGUI



image_list = []
resized_images = []


for filename in glob.glob(BorgheseGUI.path1 + "/*.jpg"):
    #print(filename)
    img = Image.open(filename)
    print(img.size)
    image_list.append(img)

savedims = image_list[0].size
#print(savedims)

for item in image_list:
    if item.size < savedims:
        savedims = item.size

#print(savedims)

for image in image_list:
    #image.show()
    image = image.resize((savedims))
    #print(type(image))
    resized_images.append(image)

for (i, new) in enumerate(resized_images):
    new.save('{}{}{}'.format(BorgheseGUI.path2, i+1, '.jpg'))
