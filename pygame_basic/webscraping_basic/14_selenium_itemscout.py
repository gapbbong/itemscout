from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


browser = webdriver.Chrome()
browser.maximize_window() # 창 최대화

url = "https://flight.naver.com/flights/" # 항공권 예약
url = "https://www.itemscout.io/category" # 항공권 예약
browser.get(url) # url 로 이동

# 가는 날 선택 클릭
browser.find_element_by_link_text("2차 분류").click()

# 제주도 선택
#browser.find_element_by_xpath("//*[@id='recommendationList']/ul/li[1]").click()

# 항공권 검색 클릭
#browser.find_element_by_link_text("항공권 검색").click()

#try:
    #elem = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='content']/div[2]/div/div[4]/ul/li[1]")))
    # 성공했을 때 동작 수행    
print(elem.text) # 첫번째 결과 출력
#finally:
    #browser.quit()