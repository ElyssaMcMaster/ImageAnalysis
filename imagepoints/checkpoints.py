import numpy as np
import matplotlib.pyplot as plt
image = plt.imread("") ## put the path to your image here
pts = np.array([[357,782],[479,1003],[678, 494],[204,607]]) ## the points here were mashed into the computer completely randomly and should be adjusted for the points you wish to see on your image

print(image.size)
plt.imshow(image) 
plt.scatter(pts[:, 0], pts[:, 1], marker="x", color="red", s=20)
plt.show()