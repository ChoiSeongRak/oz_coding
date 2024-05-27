from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import requests
import time

user = "Mozilla/5.0 (IPhone; CPU iPhone OS 13_3 like Mac OS X) AppleWebKit/605.1.15(KHTML, like Gecko) CriOS/80.0.3987.95 Mobile/15E148 Safari/604.1"

options_ = Options()
options_.add_argument(f"user-agent={user}")
options_.add_experimental_option("detach", True)
options_.add_experimental_option("excludeSwitches", ["enable-automation"])



#크롬 드라이버 매니저를 자동으로 설치되도록 실행시키는 코드
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options_)

url = "https://m2.melon.com/index.htm"
driver.get(url)
time.sleep(0.5) #너무 빠르게 클릭하면 이벤트 페이지 스킵이 안됨
driver.find_element(By.CSS_SELECTOR, ".img-logo").click()
# 멜론차트 메뉴 클래스 네임이 중복이라 다 꺼내서 text가 멜론차트인 요소를 가져와 클릭
time.sleep(2)
nav_items = driver.find_elements(By.CSS_SELECTOR, ".nav_item")
for item in nav_items:
    if item.text == "멜론차트":
        item.click()
        break

# 스크롤 5번
for _ in range(5):
    driver.find_element(By.CSS_SELECTOR, "body").send_keys(Keys.PAGE_DOWN)
    time.sleep(0.3)

# 더보기 버튼 onclick 속성이 hasMore2()인 더보기 클릭
has_items = driver.find_elements(By.CSS_SELECTOR, "button#moreBtn.service_list_more.noline.sprite.hide")
for item in has_items:
    if item.get_attribute("onclick") == "hasMore2();":
        item.click()
        break

# 스크롤 5번
time.sleep(0.5)
for _ in range(5):
    driver.find_element(By.CSS_SELECTOR, "body").send_keys(Keys.PAGE_DOWN)
    time.sleep(0.3)
time.sleep(1)

# 데이터 가져와서 변수에 넣기
html = driver.page_source
soup = BeautifulSoup(html, "html.parser")
songs = soup.select(".list_item")

for song in songs:
    ranking_element = song.select_one(".ranking_num")
    titles = song.select_one(".title.ellipsis").text
    singers = song.select_one(".name.ellipsis").text


    if ranking_element:  # 요소가 존재하는지 확인
        print(f"순위:{ranking_element.text}")
        print(f"노래 제목:{titles.strip()}")
        print(f"가수 이름:{singers}")
    else:
        pass



#아래 순서대로 스크래핑한 자료를 출력해주세요
#순위 :
#노래 제목 :
#가수 이름 :
