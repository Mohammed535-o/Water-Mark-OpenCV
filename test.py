import cv2 as cv

img = cv.imread("Photos/cat.jpg")

cv.putText(img, "WaterMark", (img.shape[1]//2, img.shape[0]//2), cv.FONT_HERSHEY_PLAIN, 1.0, (255,255,255),1)


cv.imwrite("Photos/cat.jpg", img)

newImage = cv.imread("Photos/cat.jpg")

cv.imshow("new Image", newImage)

cv.waitKey(0)