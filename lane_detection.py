import cv2

# Load an image
image = cv2.imread("images/road.jpg")  # Make sure you have a sample image named road.jpg

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Show both original and grayscale images
cv2.imshow("Original Image", image)
cv2.imshow("Grayscale Image", gray)

cv2.waitKey(0)  # Wait for a key press
cv2.destroyAllWindows()  # Close all image windows.
