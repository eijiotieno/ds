import cv2


# open pic
# img = cv2.imread("download.png")

# cv2.imshow("Output", img)

# cv2.waitKey(0)

# play video
# cap = cv2.VideoCapture("12.mp4")

# while True:
#     success, img = cap.read()
#     cv2.imshow("Video", img)
#     if cv2.waitKey(1) & 0xff == ord("q"):
#         break


# open webcam

# cap = cv2.VideoCapture(0)
# cap.set(3, 640)
# cap.set(4, 480)


# while True:
#     success, img = cap.read()
#     cv2.imshow("Video", img)
#     if cv2.waitKey(1) & 0xFF == ord("q"):
#         break


# basic functions

img = cv2.imread("23.jpeg")

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 0)
imgCanny = cv2.Canny(img, 100, 100)

cv2.imshow("Gray Image", imgGray)
cv2.imshow("Blur Image", imgBlur)
cv2.imshow("Canny Image", imgCanny)

cv2.waitKey(0)
