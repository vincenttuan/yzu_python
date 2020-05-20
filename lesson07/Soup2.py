from bs4 import BeautifulSoup
import requests
import time
from selenium import webdriver

url = 'https://www.104.com.tw/jobs/main/'

driver = webdriver.Chrome() #開啟Chrome

driver.get(url) #前往這個網址
time.sleep(1)

driver.find_element_by_id("ijob").click()
time.sleep(1)

driver.find_element_by_class_name('category-item.category-item--focus.category-item--level-two').click()
time.sleep(1)

try:
    for item in driver.find_elements_by_class_name('category-item.category-item--level-three'):
        item.click()
        time.sleep(1)
except:
    pass

time.sleep(1)

# 以 BeautifulSoup 解析 HTML 程式碼
soup = BeautifulSoup(driver.page_source, 'html.parser')
# print(soup.prettify())
stories = soup.find_all('span', attrs={'class':'children'})
# print(stories)

for s in stories:
    print(s.text.strip())

driver.close()#關閉瀏覽器