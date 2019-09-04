import time
import base64
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.touch_actions import TouchActions
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import cv2
import numpy as np
import re
import random

cv2.namedWindow('newWin')
DRIVER = 'chromedriver'
driver = webdriver.Chrome(DRIVER)
driver.get('https://www.gameeapp.com/game/v37BLBHQr-120dd1d738bb411305d45b37ef247501682225c8#tgShareScoreUrl=tg%3A%2F%2Fshare_game_score%3Fhash%3D8jYWGK2l3a5fOAM5h8xB4oX1_r0F2TX14bnMpcfGKO0')
iframe = driver.find_elements_by_class_name('gameFrame')[0]
el = driver.find_element_by_class_name('this-border')


while True:
    prev_score = int(el.text.split()[1])



    driver.switch_to.frame(iframe)
    touch_actions = TouchActions(driver)

    time.sleep(1)
    png_url = driver.execute_script(
            "return document.getElementById('canvas').toDataURL();")
        # Parse the URI to get only the base64 part
    str_base64 = re.search(r'base64,(.*)', png_url).group(1)

        # Convert it to binary
    str_decoded = base64.b64decode(str_base64)
    nparr = np.fromstring(str_decoded, np.uint8)
    touch_actions.tap_and_hold(200,200)
    touch_actions.move(200,100)
    touch_actions.perform()
    image_data = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    print("Cycle")
    driver.switch_to.default_content()

    # cv2.imshow('newWin',image_data)
    # cv2.waitKey(5)

# cv2.namedWindow('images')
# element1 = driver.find_element_by_class_name('this-bg')
# iframe = driver.find_elements_by_name('name-js-app')[0]
# el = driver.find_element_by_class_name('this-border')


driver.quit()