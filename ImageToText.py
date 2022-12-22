import pytesseract  as tess
tess.pytesseract.tesseract_cmd=r'C:\\Program Files\Tesseract-OCR\\tesseract.exe'
from PIL import Image
imgpath=("C:\\Users\\Zainab\\Desktop\\samplecv.png")
img=Image.open(imgpath)
text=tess.image_to_string(img)
print(text)
print("Hello")