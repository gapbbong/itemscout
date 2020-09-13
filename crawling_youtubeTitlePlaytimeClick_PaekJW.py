from selenium import webdriver
import requests
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('chromedriver.exe')
# url = 'https://www.youtube.com/channel/UCyn-K7rZLXjGl7VXGweIlcA/videos'
url = "https://www.youtube.com/channel/UCSic0lS4ndOdP3ysdt05iVA/videos"  #GWKTV
driver.get(url)
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"}
res = requests.get(url, headers=headers)
res.raise_for_status()

import time
SCROLL_PAUSE_TIME = 0.5
# 한번 스크롤 하고 멈출 시간 설정

body = driver.find_element_by_tag_name('body')
# body태그를 선택하여 body에 넣음

# while True:
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
    # print(idx)

from bs4 import BeautifulSoup

page = driver.page_source
soup = BeautifulSoup(page, 'lxml')

# all_videos = soup.find_all(id='dismissable')
all_videos = soup.find_all("a", attrs={"id":"video-title"})

title_list = []
for video in all_videos:
    # title = video.find(id='video-title')
    # if len(title.text.strip())>0:
    #     title_list.append(title.text)

    link = "https://www.youtube.com/"+ video["href"]
    title = video["title"]
    with open("GWKTVmovieLink.txt", "w", encoding="utf8") as f:
        f.write(link)
    #print(link)

    # 공백을 제거하고 글자수가 0보다 크면 append    

# print(title_list)
# print(len(title_list))

# video_time_list = []
# for video in all_videos:
#     video_time = video.find('span',{'class' : 'style-scope ytd-thumbnail-overlay-time-status-renderer'})
#     video_time_list.append(video_time.text.strip())

# print(video_time_list)    
# print(len(video_time_list))

# def stime(text):
#     time = text.split(':')
#     if len(time) == 1:
#         return int(time[0])
#     elif len(time) == 2:
#         return int(time[0])*60 + int(time[1])
#     else:
#         return int(time[0])*3600 + int(time[1]*60 + int(time[2]))
    
# video_time_seperate_list = []
# for time in video_time_list:
#     video_time_seperate_list.append(stime(time))

# print(video_time_seperate_list)

# import re

# view_num_list = []
# view_num_regexp = re.compile(r'조회수')
# for video in all_videos:
#     view_num = video.find('span',{'class':'style-scope ytd-grid-video-renderer'})
#     if view_num_regexp.search(view_num.text):
#         # view_num.text 에 '조회수' 문자열이 있으면 True
#         view_num_list.append(view_num.text)
# view_num_list

# def nview(text):
#     view = text.replace('조회수','')
#     num = float(view[:-2])
#     danwee = view[-2:]
#     if danwee == '만회':
#         return int(num*10000)
#     else:
#         int(num*1000)
        
# view_number_type_list = []
# for view in view_num_list:
#     view_number_type_list.append(nview(view))

# view_number_type_list

# dict_youtube = {'title':title_list, 'video_time':video_time_seperate_list, 'view_num':view_number_type_list}

# import pandas as pd
# youtube = pd.DataFrame(dict_youtube)
# youtube.head()

page.quit()






