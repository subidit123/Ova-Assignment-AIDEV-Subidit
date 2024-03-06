import cv2

# Read the image
image = cv2.imread(r"C:\Users\Subidit Chakraborty\Downloads\pexels-tobi-620337.jpg")

# Display the image
cv2.imshow('Uploaded Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()