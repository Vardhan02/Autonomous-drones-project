import cv2
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

cap = cv2.VideoCapture(0)

cv2.namedWindow("test")

img_counter = 0

while True:
    ret, frame = cap.read()
    if not ret:
        print("failed to grab frame")
        break
    cv2.imshow("test", frame)

    k = cv2.waitKey(1)
    if k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
    elif k%256 == 32:
        # SPACE pressed
        img_name = "opencv_frame_{}.png".format(img_counter)
        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))
        img_counter += 1
        img = mpimg.imread("opencv_frame_0.png")
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        imgplot = plt.imshow(imgRGB)
        plt.show()
        # image path
        path = r'opencv_frame_0.png'

        # using imread()
        img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
        cv2.imshow('opencv_frame_{}.png', img)

        dst = cv2.calcHist(img, [0], None, [256], [0, 256])

        plt.hist(img.ravel(), 256, [0, 256])
        plt.title('Histogram for gray scale image')
        plt.show()

cap.release()

cv2.destroyAllWindows()