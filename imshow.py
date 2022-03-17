import cv2

img = cv2.imread('f1.png', 0)

cv2.imshow("f1",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
