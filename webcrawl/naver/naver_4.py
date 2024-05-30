import requests 
from bs4 import BeautifulSoup

header_user = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36"}

base_url = "https://search.naver.com/search.naver?ssc=tab.blog.all&sm=tab_jum&query="
keyword = input("검색어를 하나만 입력해주세요")

url = base_url + keyword
req = requests.get(url, headers=header_user)

html = req.text
soup = BeautifulSoup(html, "html.parser")

results = soup.select(".view_wrap")


for i in results:
    title = i.select_one(".title_link")
    writer = i.select_one(".name")
    if "ad" not in i.text:
        print(f"검색키워드 : {keyword}")
        print(f"블로그 제목 : {title.text}")
        print(f"블로그 작성자 : {writer.text}")
        print()
        
        
        
        