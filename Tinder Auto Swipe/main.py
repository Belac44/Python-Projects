from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.by import By
import os
import time


driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))


driver.get("https://tinder.com")


time.sleep(15)
login = driver.find_element(By.XPATH, '//*[@id="q243527110"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a/div[2]/div[2]')
login.click()

time.sleep(15)
facebook_button = driver.find_element(By.XPATH, '//*[@id="q-1484853966"]/main/div/div[1]/div/div/div[3]/span/div[2]/button')
facebook_button.click()

#Switch windows
time.sleep(10)
fb_window = driver.window_handles[1]
driver.switch_to.window(fb_window)
print(driver.title)

#Fill Phone number
phone_input = driver.find_element(By.XPATH, '//*[@id="email"]')
phone_input.send_keys(os.environ["Phone"])

#Fill Password
password_input = driver.find_element(By.XPATH, '//*[@id="pass"]')
password_input.send_keys(os.environ["Pass"])

#Click LogIn Button

facebook_login = driver.find_element(By.NAME, 'login')
facebook_login.click()

#Agree to be Yourself
driver.switch_to.window(driver.window_handles[0])
time.sleep(45)
agree = driver.find_element(By.XPATH, '//*[@id="q-1484853966"]/main/div/div/div/div[3]/button[1]')
agree.click()


#See Dates
time.sleep(3)
profile = driver.find_element(By.XPATH, '//*[@id="q-1484853966"]/main/div/div/div/div[3]/button[1]')
profile.click()

time.sleep(3)
accept = driver.find_element(By.XPATH, '//*[@id="q243527110"]/div/div[2]/div/div/div[1]/div[1]/button')
accept.click()

#Swipe Right
time.sleep(30)
for i in range(10):
    swipe = driver.find_element(By.XPATH, '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')
    swipe.click()
    time.sleep(3)

time.sleep(10)
driver.close()
