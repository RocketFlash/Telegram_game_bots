#-- include('examples/showgrabfullscreen.py') --#
import pyscreenshot as ImageGrab
import cv2
import numpy as np

if __name__ == "__main__":
    # fullscreen
    cv2.namedWindow("hello")
    for i in range(0,100):
        im=np.array(ImageGrab.grab((100,100,500,500)))

        cv2.imshow("hello",im)
        cv2.waitKey(1)
        print(type(im))
#-#