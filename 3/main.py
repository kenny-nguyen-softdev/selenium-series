import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

os.environ['PATH'] += r"C:/SeleniumDrivers"
driver = webdriver.Chrome()

driver.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')
driver.implicitly_wait(5)

try:
    no_button = driver.find_element(By.CLASS_NAME, 'at-cm-no-button')
    no_button.click()
except NoSuchElementException:
    print('No element with this class name. Skipping ....')

sum1 = driver.find_element_by_id('sum1')
sum2 = driver.find_element_by_id('sum2')

sum1.send_keys(Keys.NUMPAD1, Keys.NUMPAD5)
sum2.send_keys(15)

btn = driver.find_element_by_css_selector('button[onclick="return total()"]')
btn.click()
