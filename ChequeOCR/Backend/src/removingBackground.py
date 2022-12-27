from PIL import Image
import numpy as np

# Opening the image and converting
# it to RGB color mode
# IMAGE_PATH => Path to the image
img = Image.open(r'C:\pythonproject\ChequeOCR\Backend\jupyter\hdfc_b.jpg').convert('RGB')

# Extracting the image data &
# creating an numpy array out of it
img_arr = np.array(img)

# Turning the pixel values of the 400x400 pixels to black
img_arr[81: 172, 605: 243] = (0, 0, 0)

# Creating an image out of the previously modified array
img = Image.fromarray(img_arr)

# Displaying the image
img.show()