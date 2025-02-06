import cv2
import numpy as np

# Load the image
image = cv2.imread("images/road.jpg")

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Gaussian blur to reduce noise
blurred = cv2.GaussianBlur(gray, (5, 5), 0)

# Use Canny Edge Detection to find lane edges
edges = cv2.Canny(blurred, 50, 150)

# Show the result
cv2.imshow("Lane Edges", edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
