import cv2

img = cv2.imread("det1680196583459.jpg")
img = cv2.resize(img, (100, 100))
cv2.imshow(mat=img, winname="tt")
cv2.waitKey()
cv2.destroyAllWindows()