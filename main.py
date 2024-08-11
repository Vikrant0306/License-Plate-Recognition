import cv2
import numpy as np
import matplotlib.pyplot as plt
import pytesseract
image = cv2.imread('sample_car.jpg')
cv2.imshow('Car Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)
edged_image = cv2.Canny(blurred_image, 50, 200)
cv2.imshow('Grayscale Image', gray_image)
cv2.imshow('Blurred Image', blurred_image)
cv2.imshow('Edged Image', edged_image)
cv2.waitKey(2000)
cv2.destroyAllWindows()
contours, _ = cv2.findContours(edged_image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
contours = sorted(contours, key=cv2.contourArea, reverse=True)[:10]
license_plate_contour = None

for contour in contours:
    # Approximate the contour
    perimeter = cv2.arcLength(contour, True)
    approx = cv2.approxPolyDP(contour, 0.018 * perimeter, True)

    # If the contour has 4 vertices, we assume it's the license plate
    if len(approx) == 4:
        license_plate_contour = approx
        break
if license_plate_contour is not None:
    cv2.drawContours(image, [license_plate_contour], -1, (0, 255, 0), 3)
    cv2.imshow('License Plate Detected', image)
    cv2.waitKey(2000)  # Display for 2 seconds
    cv2.destroyAllWindows()
else:
    print("License plate contour not found")

if license_plate_contour is not None:
    # Get the bounding box coordinates of the license plate
    x, y, w, h = cv2.boundingRect(license_plate_contour)
    license_plate = gray_image[y:y+h, x:x+w]

    # Display the cropped license plate
    cv2.imshow('Cropped License Plate', license_plate)
    cv2.waitKey(2000)  # Display for 2 seconds
    cv2.destroyAllWindows()

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


if license_plate_contour is not None:
    # Extract the license plate area as before
    x, y, w, h = cv2.boundingRect(license_plate_contour)
    license_plate = gray_image[y:y+h, x:x+w]

    # Perform OCR on the cropped license plate
    text = pytesseract.image_to_string(license_plate, config='--psm 8')
    print("Detected License Plate Number:", text.strip())

    # Optionally, display the extracted text on the image
    cv2.putText(image, text.strip(), (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
    cv2.imshow('License Plate with Text', image)
    cv2.waitKey(2000)  # Display for 2 seconds
    cv2.destroyAllWindows()
