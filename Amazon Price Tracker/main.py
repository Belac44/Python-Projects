from bs4 import BeautifulSoup
import requests

product_url="https://www.amazon.com/ELEGOO-Project-Tutorial-Controller-Projects/dp/B01D8KOZF4/ref=sr_1_5?crid=1NQC903D30WVG&keywords=Arduino+Uno+r3&qid=1661334707&sprefix=arduino+uno+r%2Caps%2C930&sr=8-5"
headers = {
    "Accept-Language": "en-US,en;q=0.9",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 Edg/104.0.1293.63",
}
response = requests.get(url=product_url, headers=headers)

soup = BeautifulSoup(response.text, "html.parser")

price = soup.select_one(selector="span.a-offscreen")
price = float(price.getText().split("$")[1])
print(price)
