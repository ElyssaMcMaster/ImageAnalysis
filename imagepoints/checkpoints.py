import numpy as np
import matplotlib.pyplot as plt
image = plt.imread("img/GB_Inv204_SWIR.final.Avg_1340-1360nm_8.jpg_resized.tif") ## put the path to your image here
pts = np.array([[500,500],[1000,1000],[1500, 1500],[2000,2000]]) ## the points here were mashed into the computer completely randomly and should be adjusted for the points you wish to see on your image

print(image.size)
plt.imshow(image) 
plt.scatter(pts[:, 0], pts[:, 1], marker="x", color="red", s=20)
plt.show()