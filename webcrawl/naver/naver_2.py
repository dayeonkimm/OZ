import requests 
from bs4 import BeautifulSoup

header_user = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36"}

url = "https://naver.com"

req = requests.get(url, headers=header_user)
print(req.raise_for_status)
print(req.request)

# print(req)

html = req.text
# print(html)

soup = BeautifulSoup(html, "html.parser")