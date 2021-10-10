import cv2

img = cv2.imread("./resources/galaxy.jpg", 1)
print(img.shape)
print(img.ndim)
img_resized = cv2.resize(img, (int(img.shape[1]/ 2), int(img.shape[0]/ 2)))

cv2.imshow("Galaxy", img_resized)
cv2.waitKey()
cv2.destroyAllWindows()
cv2.imwrite("./results/resized_galaxy.jpg", img_resized)