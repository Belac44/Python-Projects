from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))

driver.get("https://www.python.org/")

event_list = driver.find_elements(By.CSS_SELECTOR, ".event-widget .menu li a")
event_periods = driver.find_elements(By.CSS_SELECTOR, ".event-widget .menu li time")

events = {}
for item, date, i in zip(event_list, event_periods, range(len(event_list))):
    item_name = item.text
    date = date.get_attribute("datetime").split("T")[0]
    events[i] = {"event": item_name, "Date": date}

print(events)
driver.quit()