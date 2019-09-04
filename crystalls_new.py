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
driver.get('https://www.gameeapp.com/game/JUHY2Pt-802319dc8a989eaa143e49b3fc0dfb6930598d83#tgShareScoreUrl=tg%3A%2F%2Fshare_game_score%3Fhash%3DcgMKqnd3FjFPfbmLHoeB9xUVxDbnJVLCma3cVJil7RU')

iframe = driver.find_elements_by_class_name('gameFrame')[0]
gme = driver.find_elements_by_class_name('b_content-leftAppWrap')[0]

time.sleep(3)

while True:

    action = webdriver.common.action_chains.ActionChains(driver)
    action.move_to_element_with_offset(gme,100 + np.random.rand()*gme.size['width'], 100 + np.random.rand()*gme.size['height'])
    action.click()
    action.perform()
    time.sleep(0.2)

driver.quit()