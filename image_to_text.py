import pytesseract
import cv2


pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
print(pytesseract.image_to_string(r'image.jpg'))

img = cv2.imread('image.jpg')
text = pytesseract.image_to_string(img)
print(text)
