from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

user = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"

options = Options()
options.add_argument(f"User-Agent={user}")
options.add_experimental_option("detach", True)
options.add_experimental_option("excludeSwitches", ["enable-automation"])

Service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=Service,options=options)

url = "https://kream.co.kr/"
driver.get(url)
time.sleep(3)

driver.find_element(By.CSS_SELECTOR, ".nav-search.icon.sprite-icons").click()
time.sleep(2)

driver.find_element(By.CSS_SELECTOR, ".input_search.show_placeholder_on_focus").send_keys("슈프림")
time.sleep(2)

driver.find_element(By.CSS_SELECTOR, ".input_search.show_placeholder_on_focus").send_keys(Keys.ENTER)
time.sleep(2)

for i in range(20):
    driver.find_element(By.TAG_NAME, "body").send_keys(Keys.PAGE_DOWN)
    time.sleep(0.3)
    
html = driver.page_source

soup = BeautifulSoup(html, "html.parser")

items = soup.select(".item_inner")

for i in items:
    product_name = i.select_one(".translated_name")
    if "후드" in product_name.text:
        product_brand = i.select_one(".product_info_brand.brand")
        product_price = i.select_one(".amount")
        print(product_brand.text)
        print(product_name.text)
        print(product_price.text)
        print()
        


# driver.quit()