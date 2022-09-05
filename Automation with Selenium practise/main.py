from selenium import webdriver
from selenium.webdriver.chrome.service import Service

s = Service("C://Users/user//Downloads//Compressed//chromedriver_win32//chromedriver.exe")
browser = webdriver.Chrome(service=s)

url = 'https://www.google.com'
browser.get(url)
