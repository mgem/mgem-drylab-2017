import cv2
from PIL import Image
import numpy as np

#import image to numpy array
im_original = cv2.imread("May26 3.tif")
im_background = cv2.imread("May26 1.tif")

#matrix subtraction
diff_BGR = np.subtract(im_original, im_background)
#since open_cv reads image in BGR, we must convert it back to RGB using this line below
diff_RGB = cv2.cvtColor(diff_BGR, cv2.COLOR_BGR2RGB)

#save the difference numpy array as an image
im_diff = Image.fromarray(diff_RGB)
im_diff.save("difference.tif")