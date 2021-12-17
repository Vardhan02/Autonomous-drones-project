import cv2
from matplotlib import pyplot as plt

cam = cv2.VideoCapture(0)

cv2.namedWindow("test")

img_counter = 0

#def denoise (img)

while True:
    ret, frame = cam.read()
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
        key = int(input("Enter your choice:\n1. Plot the original image and the denoised image\n2. Exit\n"))
        if(key == 1):
            # Reading image from folder where it is stored
            img = cv2.imread('opencv_frame_0.png')
            rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

            # denoising of image saving it into dst image
            dst = cv2.fastNlMeansDenoisingColored(rgb_img, None, 10, 10, 7, 21)

            # Plotting of source and destination ion image
            plt.subplot(121), plt.imshow(rgb_img)
            plt.subplot(122), plt.imshow(dst)

            plt.show()
        else:
            break

cam.release()

cv2.destroyAllWindows()