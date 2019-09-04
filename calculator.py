import time
import base64
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import numpy as np
import cv2
from PIL import Image
import pytesseract
import re
import random

cv2.namedWindow('buttons')
cv2.namedWindow('equation')

DRIVER = 'chromedriver'
driver = webdriver.Chrome(DRIVER)
driver.get('https://www.gameeapp.com/game/KQsrLTZp-6625a43a382a1e8e5e7d7d800ff7d7b0967fe1ce#tgShareScoreUrl=tg%3A%2F%2Fshare_game_score%3Fhash%3DSPFzLTQpIimoctHFqPouq3UzgOgOr6Pu0i8wb8FfauM')

iframe = driver.find_elements_by_class_name('gameFrame')[0]
gme = driver.find_elements_by_class_name('b_content-leftAppWrap')[0]

time.sleep(3)

while True:
    driver.switch_to.frame(iframe)
    png_url = driver.execute_script(
        "return document.getElementById('equation').toDataURL('image/png');")
    # Parse the URI to get only the base64 part
    str_base64 = re.search(r'base64,(.*)', png_url).group(1)
    # Convert it to binary
    str_decoded = base64.b64decode(str_base64)
    nparr = np.fromstring(str_decoded, np.uint8)
    image_data = cv2.imdecode(nparr, cv2.IMREAD_GRAYSCALE)
    image_data = np.array(image_data)

    img = Image.fromarray(image_data[400:600,:])
    txt = pytesseract.image_to_string(img)
    print(txt)
    answer = eval(txt.split("=")[0].split(":")[0])
    print(answer)

    xpos = int(image_data.shape[1]/2)

    if answer == 1:
        ypos = 600
    elif answer ==2:
        ypos = 670
    else:
        ypos = 740

    driver.switch_to.default_content()
    xEl = gme.location['x']
    yEl = gme.location['y']

    coeff = 540/1024

    action = webdriver.common.action_chains.ActionChains(driver)
    action.move_to_element_with_offset(gme,coeff*xpos, coeff*ypos)
    action.click()
    action.perform()

    cv2.imshow('equation', image_data[400:600,:])
    cv2.waitKey(1)
    time.sleep(1)

driver.quit()