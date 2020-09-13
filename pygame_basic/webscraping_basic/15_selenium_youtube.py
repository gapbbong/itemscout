import requests
from bs4 import BeautifulSoup

url = "https://www.youtube.com/channel/UCSic0lS4ndOdP3ysdt05iVA/videos" #GWKTV
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"}
res = requests.get(url, headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

movies = soup.find_all("div", attrs={"class":{"style-scope ytd-grid-video-renderer"}})
print(len(movies))

# with open("moive.html", "w", encoding="utf8") as f:
#     f.write(soup.prettify())

for movie in movies:
    title = movie.find(id='video-title')#.get_text()
    print(title)