import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
img = cv2.imread('test.JPG')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
var = [pytesseract.image_to_string(img)]
print(var)
print(pytesseract.image_to_string(img))
cv2.imshow('Result', img)
cv2.waitKey(0)


