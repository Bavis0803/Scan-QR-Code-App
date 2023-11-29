import cv2
import numpy as np
from pyzbar.pyzbar import decode
frame = cv2.imread("5.jpg")
for code in decode(frame):
    decode_data = code.data.decode("utf-8")
    print(decode_data)
    rect_pts = code.rect
    if decode_data:
        pts = np.array([code.polygon],np.int32)
        cv2.polylines(frame,[pts],True,(255,0,0),3)
cv2.imshow("Output",frame)
cv2.waitKey()