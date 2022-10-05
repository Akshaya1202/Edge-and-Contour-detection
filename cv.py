import cv2

image = cv2.imread("obj.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (3, 3), 0)
edged = cv2.Canny(blurred, 10, 100)

kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
dilate = cv2.dilate(edged, kernel, iterations=1)
contours, _ = cv2.findContours(dilate, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
image_copy = image.copy()
cv2.drawContours(image_copy, contours, -1, (255, 0, 0), 2)
print(len(contours), "objects were found in this image.")

cv2.imshow("Dilated image", dilate)
cv2.imshow("contours", image_copy)
cv2.waitKey(0)
