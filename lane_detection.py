import cv2
import numpy as np

# Load the image
image = cv2.imread("images/road.jpg")

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Gaussian blur
blurred = cv2.GaussianBlur(gray, (5, 5), 0)

# Detect edges
edges = cv2.Canny(blurred, 50, 150)

# Define a region of interest (ROI) to focus only on the road
mask = np.zeros_like(edges)
height, width = edges.shape
polygon = np.array([[(100, height), (width-100, height), (width//2, height//2)]], np.int32)
cv2.fillPoly(mask, polygon, 255)
roi = cv2.bitwise_and(edges, mask)

# Detect lines using Hough Transform
lines = cv2.HoughLinesP(roi, 1, np.pi/180, 50, minLineLength=50, maxLineGap=200)

# Draw the detected lines
if lines is not None:
    for line in lines:
        x1, y1, x2, y2 = line[0]
        cv2.line(image, (x1, y1), (x2, y2), (0, 255, 0), 5)

# Show the final image
cv2.imshow("Lane Detection", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
