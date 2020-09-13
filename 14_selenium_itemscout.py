from selenium import webdriver
import requests
from bs4 import BeautifulSoup
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

#res = requests.get("http://naver.com")
#print(res.status_code)

browser = webdriver.Chrome("C:\python\chromedriver.exe")
#browser.maximize_window() # 창 최대화

#url = "https://flight.naver.com/flights/" # 항공권 예약
url = "https://www.itemscout.io/category" # 아이템 스카웃
browser.get(url) # url 로 이동


# 가는 날 선택 클릭
#browser.find_element_by_link_text("1차 분류").click()
# 1차 분류 선택
browser.find_element_by_xpath("//*[@id='container']/div[1]/table[1]/tr/td[2]/div/div[2]/div[1]/span").click()

soup = BeautifulSoup(browser.page_source, "lxml")  #bp-dropdown__body itemscout-category-dropdown-bp__body fade-enter-active fade-enter-to
movies = soup.find_all("div", attrs={"class":"main-container"})
# title = movie.find("div", attrs={"class":"bp-dropdown__body itemscout-category-dropdown-bp__body"}).get_text()
#print(len(movies))

# with open("movie.html", "w", encoding="utf8") as f:
#     f.write(soup.prettify())

for movie in movies:
    title = movie.find("div", attrs={"class":"bp-dropdown__body itemscout-category-dropdown-bp__body fade-enter-active fade-enter-to"}).get_text()
    print(title)
# 항공권 검색 클릭
#browser.find_element_by_link_text("항공권 검색").click()

#try:
    #elem = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='content']/div[2]/div/div[4]/ul/li[1]")))
    # 성공했을 때 동작 수행    
#print(elem.text) # 첫번째 결과 출력
#finally:
browser.quit()