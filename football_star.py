import Quartz.CoreGraphics as CG
from PIL import Image
import time
import numpy as np
from pymouse import PyMouse
from time import sleep

def ImageGrab(region):
    # Create screenshot as CGImage
    image = CG.CGWindowListCreateImage(
        region,
        CG.kCGWindowListOptionOnScreenOnly,
        CG.kCGNullWindowID,
        CG.kCGWindowImageDefault)

    width = CG.CGImageGetWidth(image)
    height = CG.CGImageGetHeight(image)
    bytesperrow = CG.CGImageGetBytesPerRow(image)

    pixeldata = CG.CGDataProviderCopyData(CG.CGImageGetDataProvider(image))
    image = np.frombuffer(pixeldata, dtype=np.uint8)
    image = image.reshape((height, bytesperrow//4, 4))
    image = image[:,:width,:]
    return image



# Initialize some basic variables
m = PyMouse()           # mouse
ball = [4, 3, 1] # branch color in RGB

# Range was set because when I first ran the code - taking the screenshot time and
# the "branch" comparing time was not matching. Therefore the code needs to restart
# the game couple of times till the memory is filled up a little and our code gets
# a little slower. Plus, if the code doesn't work, we have to stop at some point and
# not run into an infinite loop.
for i in range(500):
    reg = CG.CGRectMake(210, 110, 5, 490)
    region = ImageGrab(reg)
    # Check for branch inside the numpy array, if found flip the isLeft switch
    for i in range(0, 490):
        for j in range(0,5):
            if 170 <= region[i,j,1] & 220 > region[i,j,1]:
                print((region[i, j, 0]))
                m.click(320, 320, 1)
                break
    sleep(0.5)
