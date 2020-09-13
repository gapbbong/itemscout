import requests
from bs4 import BeautifulSoup
url = "https://comic.naver.com/webtoon/weekday.nhn"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")
# print(soup.title)
# print(soup.find(attrs = {"class":"Nbtn_upload"}))

rank1 = soup.find("li", attrs={"class":"rank01"})
# print(rank1.a)

print(rank1.find_next_siblings("li"))