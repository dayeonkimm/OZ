import requests 
from bs4 import BeautifulSoup

header_user = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36"}

base_url = "https://www.melon.com/chart/index.htm"
req = requests.get(base_url, headers=header_user)

html = req.text
soup = BeautifulSoup(html, "html.parser")

# lst50 = soup.select(".lst50")
# lst100 = soup.select(".lst100")

# lst_all = lst50 + lst100

lst_all = soup.find_all(class_=["lst50","lst100"])

for rank, i in enumerate(lst_all, 1):
    title = i.select_one(".ellipsis.rank01 a")
    artist = i.select_one(".ellipsis.rank02 a")
    album = i.select_one(".ellipsis.rank03 a")
    print(f"[순위] {rank}")
    print(f"제목 : {title.text}")
    print(f"가수 : {artist.text}")
    print(f"앨범 : {album.text}")
    print()
    