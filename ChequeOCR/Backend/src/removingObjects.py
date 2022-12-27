from pdf2image import convert_from_path
import pytesseract
import cv2
import numpy as np
from PIL import Image

o_img = Image.open(r'C:\pythonproject\ChequeOCR\Backend\jupyter\hdfc_b.jpg').convert('RGB')
# image = cv2.cvtColor(np.array(o_img), cv2.COLOR_BGR2GRAY)

# rgb_image = Image.fromarray(o_img).convert('RGB')

image_array = np.array(o_img)
image_array[242: 250, 346: 353] = (0,0,0)
o_img = Image.fromarray(image_array)
o_img.show()
