from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.keys import Keys
driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))

driver.get("http://secure-retreat-92358.herokuapp.com/")

# count = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
# count.click()

# links = driver.find_element(By.LINK_TEXT, "William Ruto")
# links.click()
# 
# search = driver.find_element(By.NAME, "search")
# search.send_keys("Python")
# search.send_keys(Keys.ENTER)

fname = driver.find_element(By.NAME, "fName")
fname.send_keys("CALEB")

lname = driver.find_element(By.NAME, "lName")
lname.send_keys("BOSIRE")

email = driver.find_element(By.NAME, "email")
email.send_keys("test@gmail.com")

submit = driver.find_element(By.CLASS_NAME, "btn")
submit.click()
