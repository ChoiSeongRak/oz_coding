import requests
from bs4 import BeautifulSoup

header_user = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}

base_url = "https://search.naver.com/search.naver?ssc=tab.blog.all&sm=tab_jum&query="
keyword = input("검색어를 하나만 입력해주세요")

url = base_url + keyword
req = requests.get(url, headers=header_user)

html = req.text
soup = BeautifulSoup(html, "html.parser")

blog_ad = soup.select(".user_box")
blog_author = soup.select(".title_link")
blog_name = soup.select(".name")

for ad, author, name in zip(blog_ad, blog_author, blog_name):
    if not ad.find(class_="spblog ico_ad"):
        print(f" 작성자 : {name.text}")
        print(f" 제목 : {author.text}")

# 아무것도 없는 경우는 어떤 값이 들어가는지 확인해주세요
# btn_save _keep_trigger

# if문의 참과 거짓일 경우 어떻게 작동하는지에 대한 원리를 상기시켜보세요
# 광고가 없을 경우 코드 작동, 있을 경우 아무 일도 일어나지 않음