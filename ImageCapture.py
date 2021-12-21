from math import log10, sqrt
import cv2
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

cap = cv2.VideoCapture(0)

cv2.namedWindow("test")

img_counter = 0
def Denoise(img):

        # Reading image from folder where it is stored
        img = cv2.imread('opencv_frame_0.png')
        rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        # denoising of image, and saving it into dst image
        dst = cv2.fastNlMeansDenoisingColored(rgb_img, None, 5, 10, 7, 21)

        # Plotting of source and destination ion image
        plt.subplot(121), plt.imshow(rgb_img)
        plt.subplot(122), plt.imshow(dst)

        plt.show()

def PSNR(original, compressed):
    mse = np.mean((original - compressed) ** 2)
    if(mse == 0):  # MSE is zero means no noise is present in the signal .
                  # Therefore PSNR have no importance.
        return 100
    max_pixel = 255.0
    psnr = 20 * log10(max_pixel / sqrt(mse))
    return psnr

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
        img_name = "opencv_frame_0.png"
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
        cv2.imshow('opencv_frame_0.png', img)

        dst = cv2.calcHist(img, [0], None, [256], [0, 256])

        plt.hist(img.ravel(), 256, [0, 256])
        plt.title('Histogram for gray scale image')
        plt.show()

        original = cv2.imread("opencv_frame_0.png")
        compressed = cv2.imread("opencv_frame_0.png")
        value = PSNR(original, compressed)
        print(f"PSNR value is {value} dB")
        if value>50:
            Denoise(img)




cap.release()

cv2.destroyAllWindows()