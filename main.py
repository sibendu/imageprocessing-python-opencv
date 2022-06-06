import numpy as np
import imageio
import cv2
import scipy.ndimage

img = "image/m.jpg"
output = "image/m1.png"

def rgb2gray(rgb):
    # 2 dimensional array to convert image to sketch
    return np.dot(rgb[..., :3], [0.2989, 0.5870, .1140])

def dodge(front, back):
    # if image is greater than 255 (which is not possible) it will convert it to 255
    final_sketch = front * 255 / (255 - back)
    final_sketch[final_sketch > 255] = 255
    final_sketch[back == 255] = 255

    # to convert any suitable existing column to categorical type we will use aspect function
    # and uint8 is for 8-bit signed integer
    return final_sketch.astype('uint8')


print(f'Starting to proces')

ss = imageio.imread(img)
gray = rgb2gray(ss)
i = 255 - gray
# to convert into a blur image
blur = scipy.ndimage.filters.gaussian_filter(i, sigma=13)

# calling the function
r = dodge(blur, gray)

cv2.imwrite( output, r)
print(f'Completed processing')
