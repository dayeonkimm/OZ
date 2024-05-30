import requests
from bs4 import BeautifulSoup

header_user = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}

url = "http://www.cgv.co.kr/movies/?lt=1&ft=0"
req = requests.get(url, headers=header_user)

html = req.text
soup = BeautifulSoup(html, "html.parser")

title = soup.select(".title")
rate = soup.select(".percent span")
date = soup.select(".txt-info")

for rank, i in enumerate(zip(title,rate,date), 1):
    print(f"[순위] {rank}위")
    print(f"제목 : {i[0].text}")
    print(f"예매율 : {i[1].text}")
    print(f"개봉일자 : {i[2].text.split()[0]}")
    print()