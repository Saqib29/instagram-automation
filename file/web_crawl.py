import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from secure_file import *
import chrome_options
import os
import wget


def get_data():

    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("https://www.instagram.com/")

    username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
    password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))

    username.clear()
    password.clear()

    username.send_keys(user_name)
    password.send_keys(pass_word)

    log_in = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()
    not_now = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Not now')]"))).click()
    not_now2 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Not Now')]"))).click()

    searchbox = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Search']")))
    searchbox.clear()
    keyword = "#cat"
    searchbox.send_keys(keyword)
    searchbox.send_keys(Keys.ENTER)

    driver.execute_script("window.scrollTo(0, 4000)")
    images = driver.find_element(by=By.TAG_NAME, value='img')
    images = [image.get_attribute('src') for image in images]


    path = os.getcwd()
    path = os.path.join(path, "../"+keyword[1:]+"s")

    os.mkdir(path)

    counter = 0
    for image in images:
        save_as = os.path.join(path, keyword[1:] + str(counter) + ".jpg")
        wget.download(image, save_as)
        counter += 1


if __name__ == "__main__":
    get_data()