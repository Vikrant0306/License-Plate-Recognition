import cv2
import numpy as np
import matplotlib.pyplot as plt
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
cv2.waitKey(0)
cv2.destroyAllWindows()
