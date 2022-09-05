from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

FORM_LINK = 'https://docs.google.com/forms/d/e/1FAIpQLScE4dDiWpB5gNICZgMtT5r' \
          'AexRy4NhNqNLd8uWsQBOZl2_MAQ/viewform?usp=sf_link'

ZILLOW_URL = 'https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C' \
             '%22usersSearchTerm%22%3Anull%2C%22mapBounds%22%3A%7B%22west%22%3A-122.56276167822266%2C%22east%22%3A' \
             '-122.30389632177734%2C%22south%22%3A37.69261345230467%2C%22north%22%3A37.857877098316834%7D%2C%22isMap' \
             'Visible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22val' \
             'ue%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22c' \
             'msn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value' \
             '%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%2' \
             '2mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22' \
             '%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome104.0.5112.102 Safari/537.36 Edg/104.0.1293.70'
}


class AppartmentSearch:
    
    def __init__(self):
        self.driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
        self.response = requests.get(ZILLOW_URL, headers=headers)
        self.prices = []
        self.property_links = []
        self.address = []

    def find_appartments(self):
        while len(self.prices) == 0:

            soup = BeautifulSoup(self.response.text, "html.parser")

            prices = soup.find_all(name='div', class_='list-card-price')
            prices = [price.text.split('+')[0] for price in prices]
            self.prices = prices

            property_links = soup.select(".list-card-top a")
            self.property_links = [link["href"] for link in property_links]

            addresses = soup.select(".list-card-info address")
            self.address = [address.getText() for address in addresses]


    def fill_form(self):
        self.driver.get(FORM_LINK)
        print(len(self.prices))

        for i in range(len(self.prices)):
            addr = WebDriverWait(self.driver, 15).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, "input.whsOnd.zHQkBf")))

            addr[0].send_keys(self.address[i])
            addr[1].send_keys(self.prices[i])

            if not self.property_links[i].startswith("https"):
                self.property_links[i] = "https://www.zillow.com" + self.property_links[i]

            addr[2].send_keys(self.property_links[i])

            submit = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div'))
            )

            submit.click()

            another_response = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.LINK_TEXT, "Submit another response"))
            )

            another_response.click()


bot = AppartmentSearch()
bot.find_appartments()
bot.fill_form()
