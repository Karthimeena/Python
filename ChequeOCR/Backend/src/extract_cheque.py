import cv2
import numpy as np
from PIL import Image
from Backend.src.readCheque import read_cheque
from Backend.src.readmicr import read_micr
import pytesseract
import uuid
import os

def extractdata(chequeFile):
    # cheque_img = Image.open(r'C:\pythonProject\ChequeOCR\Backend\jupyter\cheque2.jpg')
    cheque_img = Image.open(chequeFile)

    processed_img = preprocess(chequeFile)
    cheque_text = readCheque(processed_img, 'eng')
    print(cheque_text)
    data = read_cheque(cheque_text).parse()
    print(data)

    mcrdata = cropMICR(chequeFile)
    # print(mcrdata)
    mcr_data = read_micr(mcrdata).parse()
    # read MICR
    print("MICR VALUE", mcr_data)
    data.update(mcr_data)
    return data

def readCheque(file_path,language):
    pytesseract.pytesseract.tesseract_cmd = r'C:\Users\pirat\AppData\Local\Tesseract-OCR\tesseract.exe'
    text = pytesseract.image_to_string(file_path, lang=language)
    return text

def preprocess(chequeFile):
    image = cv2.imread(chequeFile)
    # r'C:\pythonProject\ChequeOCR\Backend\jupyter\cheque2.jpg')
    image = cv2.cvtColor(np.array(image), cv2.COLOR_BGR2GRAY)

    new_img = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 61, 31)
    return new_img

def cropMICR(chequeFile):
    cheque_img = Image.open(chequeFile)
    # r'C:\pythonProject\ChequeOCR\Backend\jupyter\cheque2.jpg')
    mcr_file = "../crop/" + str(uuid.uuid4()) + ".jpg"
    cheque_mcr = cheque_img.crop((31, 550, 1104, 613))
    cheque_mcr.save(mcr_file, quality=95)

    # read MICR file
    mcr_data = readCheque(cheque_mcr, 'mcr')

    if os.path.exists(mcr_file):
        os.remove(mcr_file)

    return mcr_data