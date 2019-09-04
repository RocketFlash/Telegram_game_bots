import Quartz.CoreGraphics as CG
from PIL import Image
import time
from selenium import webdriver
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


# DRIVER = 'chromedriver'
# driver = webdriver.Chrome(DRIVER)
# driver.get('https://tbot.xyz/lumber/#eyJ1IjoxMjEwNTg2OTMsIm4iOiJSYXVmIFlhZ2Zhcm92IiwiZyI6Ikx1bWJlckphY2siLCJjaSI6IjYxNjEzMjA5NTc4NTUzMzY2NzkiLCJpIjoiQWdBQUFQZUhBd0NGTlRjSEFjWVNhX2oxdkI4In1kZGMzOGZiOGE0NGMyMjhjYjhiMTBjNDUzZDgzZDRjOQ==&tgShareScoreUrl=tg%3A%2F%2Fshare_game_score%3Fhash%3D0cuoVAS_p2fw-7aLLFkbFPjQw7gCuVTFrs3cdTPkeNU')
#
# button_left = driver.find_element_by_id('button_left')
# button_right = driver.find_element_by_id('button_right')

# Initialize some basic variables
m = PyMouse()           # mouse
isLeft = True           # check which side are we on
branch = [61, 115, 160] # branch color in RGB

# Range was set because when I first ran the code - taking the screenshot time and
# the "branch" comparing time was not matching. Therefore the code needs to restart
# the game couple of times till the memory is filled up a little and our code gets
# a little slower. Plus, if the code doesn't work, we have to stop at some point and
# not run into an infinite loop.
for i in range(900):
# while True:
    # Wait till we cut the tree and branch goes down a level. You may as weel play around
    # with this number. Making it smaller, makes lumberjack go faster. However you'll have
    # to change the height(95 px) to bigger number, so that your screenshot can capture
    # enough region to check for a branch. But be careful, if the region is too big, you'll
    # capture a branch before it moves into a right position.
    if isLeft:
        # Had to cut down 1 pixel down on the width, because the last pixel was catching
        # the actual tree
        reg = CG.CGRectMake(257, 305, 1, 95)
    else:
        reg = CG.CGRectMake(379, 305, 1, 95)

    region = ImageGrab(reg)
    # Check for branch inside the numpy array, if found flip the isLeft switch
    for i in range(0, 95):
        if branch[0] == region[i,0,0]:
            isLeft = not isLeft
            break
    # Since we didn't move when we found a branch, we do it now. This will also let us
    # to click on the play button if the lumberjack is dead. This way we'll be able to
    # play continuously till the speed is perfect.
    if isLeft:
        m.click(232, 685, 1)
        # button_left.click()
    else:
        m.click(400, 685, 1)
        # button_right.click()
    sleep(0.0585)