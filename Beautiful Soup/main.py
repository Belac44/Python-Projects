import requests
from bs4 import BeautifulSoup

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")

soup = BeautifulSoup(response.text, "html.parser")

title_tags = soup.find_all(name="h3", class_="title")
titles = [title.getText() for title in title_tags]

for i in range(len(titles) - 1, -1, -1 ):
    with open("movies.txt", "a") as file:
        file.write(f"{titles[i].encode('utf-8')}\n")
    print(titles[i])


















