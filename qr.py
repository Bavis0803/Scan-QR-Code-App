import cv2
import numpy as np
from pyzbar.pyzbar import decode
def qr(img_path):
    img = cv2.imread(img_path)
    for code in decode(img):
        decode_data = code.data.decode("utf-8")
        return decode_data
print(qr("5.jpg"))