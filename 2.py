import cv2
from pyzbar.pyzbar import decode
import numpy as np

def extract_qr_code(image_path):
    # Read the image
    image = cv2.imread(image_path)

    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Use the zbar library to decode the QR code
    qr_codes = decode(gray)
    print(qr_codes)

    if qr_codes:
        # Iterate through all the QR codes found in the image
        for qr_code in qr_codes:
            # Extract the data from the QR code
            qr_data = qr_code.data.decode('utf-8')

            # Draw a rectangle around the QR code on the original image
            rect_points = qr_code.polygon
            if len(rect_points) == 4:
                rect_points = [(point.x, point.y) for point in rect_points]
                rect_points = [(int(x), int(y)) for x, y in rect_points]

                # Draw rectangle on the original image
                # cv2.polylines(image, [np.array(rect_points)], isClosed=True, color=(0, 255, 0), thickness=2)

                # Extract and crop the region of interest (ROI) from the original image
                roi_corners = np.array(rect_points, dtype=np.int32)
                roi_corners = roi_corners.reshape(4, -1)
                roi = image[min(roi_corners[:, 1]):max(roi_corners[:, 1]),
                            min(roi_corners[:, 0]):max(roi_corners[:, 0])]

                # Save the cropped image
                cv2.imwrite('cropped_qr_code.png', roi)

            # Print the extracted data
            print("QR Code Data:", qr_data)

        # Display the image with the QR code highlighted
        cv2.imshow('Image with QR Code', image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print("No QR codes found in the image.")

# Specify the path to your image
image_path = '4.jpg'

# Call the function to extract QR code from the image
extract_qr_code(image_path)
