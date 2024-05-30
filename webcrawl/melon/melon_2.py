import requests 
from bs4 import BeautifulSoup

header_user = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36"}

base_url = "https://www.melon.com/chart/index.htm"
req = requests.get(base_url, headers=header_user)

html = req.text
soup = BeautifulSoup(html, "html.parser")

# print(soup.title)
# print(soup.h1)

# find 방식
# h1 = soup.find("h1")
# print(h1)

# logo = soup.find(class_="page_header")
# print(logo)

# nav = soup.find(class_="button_rbox", text="담기")
# print(nav)

navs = soup.find_all(class_="button_rbox")
print(len(navs))

for i in navs:
    print(i.text)