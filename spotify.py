from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
options = webdriver.ChromeOptions()
options.headless = True
driver = webdriver.Chrome(PATH)

driver.get("https://open.spotify.com/")


def login():
    login_button = driver.find_element_by_xpath(
        '//*[@id="main"]/div/div[2]/div[1]/header/div[5]/button[2]')
    login_button.click()
    time.sleep(2)
    username_field = driver.find_element_by_xpath('//*[@id="login-username"]')
    username_field.send_keys("tomek@pulkiewicz.com")
    password_field = driver.find_element_by_xpath('//*[@id="login-password"]')
    password_field.send_keys("Agnieszka123")
    submit_button = driver.find_element_by_xpath('//*[@id="login-button"]')
    submit_button.click()
    time.sleep(3)
    cookies_button = driver.find_element_by_xpath(
        '//*[@id="onetrust-accept-btn-handler"]')
    cookies_button.click()


def play():
    play_button = driver.find_element_by_xpath(
        '//*[@id="main"]/div/div[2]/div[2]/footer/div/div[2]/div/div[1]/button[3]')
    play_button.click()


def stop():
    play_button = driver.find_element_by_xpath(
        '//*[@id="main"]/div/div[2]/div[2]/footer/div/div[2]/div/div[1]/button[3]')
    play_button.click()


def quit():
    driver.quit()
