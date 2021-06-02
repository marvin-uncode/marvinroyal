# Signature: 62C352412DD831E81C8D3BF48B07E936BF12E1DC23A02AD7F64D5B7629FE253E
# Date: 6/2/2021
# Image-to-Text and GUI

# Dev Notes: image has to be super clear with wording in order for an accurate read. text
# White spaces and random characters can be cleaned up through python magic
# Image to text has varying degrees of success; determine standard for a accurate scan
# Parse date, quoted time, tip + delivery fee

import cv2
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

img = cv2.imread('ttg_image_files/IMG_7687.jpg')

text = pytesseract.image_to_string(img)

print(text)