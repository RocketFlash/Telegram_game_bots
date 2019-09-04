import time
import base64
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
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
driver.get('https://www.gameeapp.com/game/FGM7TVW2Ma-d520ec15f3dcece0de783c382699b43461e06919#tgShareScoreUrl=tg%3A%2F%2Fshare_game_score%3Fhash%3DSaYeB3goOZkxQWn_it0Yv_WvPxOgKOncv9N1tBArtd0')

iframe = driver.find_elements_by_class_name('gameFrame')[0]

driver.switch_to.frame(iframe)
while True:
    png_url = driver.execute_script(
            "return document.getElementById('pane').toDataURL('image/png');")
        # Parse the URI to get only the base64 part
    str_base64 = re.search(r'base64,(.*)', png_url).group(1)

        # Convert it to binary
    str_decoded = base64.b64decode(str_base64)
    nparr = np.fromstring(str_decoded, np.uint8)
    image_data = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    cv2.imshow('newWin',image_data)
    print(nparr.shape)
    cv2.waitKey(5)

time.sleep(10000)
# cv2.namedWindow('images')
# element1 = driver.find_element_by_class_name('this-bg')
# iframe = driver.find_elements_by_name('name-js-app')[0]
# el = driver.find_element_by_class_name('this-border')


driver.quit()