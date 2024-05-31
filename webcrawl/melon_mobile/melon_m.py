from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

user = "Mozilla/5.0 (IPhone; CPU iPhone OS 13_3 like Mac OS X) AppleWebKit/605.1.15(KHTML, like Gecko) CriOS/80.0.3987.95 Mobile/15E148 Safari/604.1"

options_ = Options()
options_.add_argument(f"user-agent={user}")
options_.add_experimental_option("detach", True)
options_.add_experimental_option("excludeSwitches", ["enable-logging"])


#크롬 드라이버 매니저를 자동으로 설치되도록 실행시키는 코드
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options_)

url = "https://m2.melon.com/index.htm"
driver.get(url)
time.sleep(0.5)

driver.find_element(By.CSS_SELECTOR, ".inner-btn").click()
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, ".menu_side.sprite.menu.hide").click()
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, ".sprite.chart").click()
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, '.service_list_more.noline.sprite.hide[onclick="hasMore2();"]').click()
time.sleep(2)

html = driver.page_source
soup = BeautifulSoup(html,"html.parser")

music_list = soup.select(".service_list.list_music .list_item")
print(len(music_list))


for i in music_list[:100]:
    rank = i.select_one(".ranking_num")
    title = i.select_one(".title.ellipsis")
    artist = i.select_one(".name.ellipsis")
    
    print(f"순위 : {rank.text}")
    print(f"노래 제목 : {title.text.strip()}")
    print(f"가수 이름 : {artist.text}")
    print()
    

driver.quit()