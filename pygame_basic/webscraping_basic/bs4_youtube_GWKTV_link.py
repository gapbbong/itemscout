from selenium import webdriver
browser = webdriver.Chrome()
from selenium.webdriver.common.keys import Keys
#browser.maximize_window()

# 페이지 이동
url = "https://www.youtube.com/channel/UCSic0lS4ndOdP3ysdt05iVA/videos"  #GWKTV
# url = "https://play.google.com/store/movies/top"
browser.get(url)

driver = webdriver.Chrome('chromedriver.exe')
# 지정한 위치로 스크롤 내리기
# 모니터(해상도) 높이인 1080 위치로 스크롤 내리기
#browser.execute_script("window.scrollTo(0, 1080)") # 1920 x 1080
#browser.execute_script("window.scrollTo(0, 2080)")

# 화면 가장 아래로 스크롤 내리기
# browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")

import time
interval = 3 # 2초에 한번씩 스크롤 내림

# 현재 문서 높이를 가져와서 저장
prev_height = browser.execute_script("return document.body.scrollHeight")


import time
SCROLL_PAUSE_TIME = 0.5
# 한번 스크롤 하고 멈출 시간 설정

body = driver.find_element_by_tag_name('body')
# body태그를 선택하여 body에 넣음

for idx in range(1,4):
    last_height = driver.execute_script('return document.documentElement.scrollHeight')
    # 현재 화면의 길이를 리턴 받아 last_height에 넣음
    for i in range(10):
        body.send_keys(Keys.END)
        # body 본문에 END키를 입력(스크롤내림)
        time.sleep(SCROLL_PAUSE_TIME)
    new_height = driver.execute_script('return document.documentElement.scrollHeight')
    if new_height == last_height:
        break;

# 반복 수행
#for idx in range(1,4):
    # 스크롤을 가장 아래로 내림
    #browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")

    # 페이지 로딩 대기
    #time.sleep(interval)

    # 현재 문서 높이를 가져와서 저장
    #curr_height = browser.execute_script("return document.body.scrollHeight")
    #if curr_height == prev_height:
        #break

    #prev_height = curr_height

#print("스크롤 완료")


import requests
from bs4 import BeautifulSoup

soup = BeautifulSoup(browser.page_source, "lxml")

#movies = soup.find_all("div", attrs={"class":["ImZGtf mpg5gc", "Vpfmgd"]})
#title = movies.find(/watch?v=")
movies = soup.find_all("a", attrs={"id":"video-title"})
#print(movies)
for movie in movies: 
    link = "https://www.youtube.com/"+ movie["href"]
    title = movie["title"]
    print(link)

    #with open("movieGWKTVlink.txt", "w", encoding="utf8") as f:
        #f.write(title+" "+link)
    #f.write(soup.prettify())
#title = []
#titles =str(movies)
#for movie in movies:
#index = str(movies).index("href")
#index = str(movies).index("href", index + 1)
#print(str(movies)[index:110])
 #   sum += hrefStr


#for movie in movies:
    #title = movie.find(id='video-title')
    #print(title)
    #title = movie.find("a", attrs={"class":"yt-simple-endpoint style-scope ytd-grid-video-renderer"}).get_text()
    #title = movie.find(id='video-title')
    # title = movie.find_all().get_text()
    
     # 링크
    #link = movie.find("a", attrs={"class":"yt-simple-endpoint style-scope ytd-grid-video-renderer"})["href"]
    # 올바른 링크 : https://www.youtube.com/watch?v= + link

    #print(str(title))
    #print(movies)
    #print(str(link))
    # print("-" * 100)

browser.quit()