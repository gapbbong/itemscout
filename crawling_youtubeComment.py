from bs4 import BeautifulSoup
from selenium import webdriver
import time
import requests
import re

driver = webdriver.Chrome()
driver.set_window_size(800, 600)

# Url = 'https://www.youtube.com/watch?v=2XcCE84TYKw'
Url = 'https://www.youtube.com/watch?v=5XPsNhiuqHg'
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"}
res = requests.get(Url, headers=headers)
res.raise_for_status()
driver.get(Url)
time.sleep(6)

last_page_height = driver.execute_script("return document.documentElement.scrollHeight")
while True:
    driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
    time.sleep(3.0)
    new_page_height = driver.execute_script("return document.documentElement.scrollHeight")

    if new_page_height == last_page_height:
        break
    last_page_height = new_page_height
    
    elements = driver.find_elements_by_css_selector("#more-replies")
for element in elements :
    driver.execute_script("arguments[0].click();", element)
    
    html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

comments = soup.find_all("ytd-comment-thread-renderer", class_ = "style-scope ytd-item-section-renderer")
for comment in comments :
    comment_text = comment.find("yt-formatted-string", id="content-text").text
    try :
        print(comment_text)
    except :
        print("이모티콘 출력에 문제가 있음.")

    replies = comment.find("div", id="replies").find_all("yt-formatted-string", id="content-text")
    for replie in replies :
        replie_text = replie.text
        try :
            print("     대댓 : ", replie_text)
        except :
            print("이모티콘 출력에 문제가 있음.")
            