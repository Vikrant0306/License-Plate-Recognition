import cv2
import numpy as np
import matplotlib.pyplot as plt
image = cv2.imread('sample_car.jpg')
cv2.imshow('Car Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
