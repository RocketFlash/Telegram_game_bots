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
driver.get('https://tbot.xyz/math/#eyJ1IjoxMjEwNTg2OTMsIm4iOiJSYXVmIFlhZ2Zhcm92IiwiZyI6Ik1hdGhCYXR0bGUiLCJjaSI6IjYxNjEzMjA5NTc4NTUzMzY2NzkiLCJpIjoiQWdBQUFPLUhBd0NGTlRjSFBfdDAxOUx6eWFrIn00ZTQyMjJlMzg4MjNkMTg0Mzc3NDEyMmMxZDk5ZDU0MA==&tgShareScoreUrl=tg%3A%2F%2Fshare_game_score%3Fhash%3DZQB37YM-E8jyXD59EH07RtSxfOOP-SnN9eurLE97hKI')
task_x = driver.find_element_by_id('task_x')
task_y = driver.find_element_by_id('task_y')
task_op = driver.find_element_by_id('task_op')
task_res = driver.find_element_by_id('task_res')
button_wrong = driver.find_element_by_id('button_wrong')
button_correct = driver.find_element_by_id('button_correct')
button_correct.click()
while True:
    print(str(task_x.text+task_op.text+task_y.text)+" = "+task_res.text)
    if len(task_x.text) != 0:
        a = int(task_x.text)
        b = int(task_y.text)
        op = str(task_op.text)

        if op == '/':
            answer = a/b
        elif op == '–':
            answer = a-b
        elif op == '+':
            answer = a+b
        else:
            answer = a*b

        if answer==int(task_res.text):
            button_correct.click()
        else:
            button_wrong.click()
        time.sleep(0.001)
    pass

driver.quit()