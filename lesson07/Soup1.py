import time
from selenium import webdriver

url = 'https://www.104.com.tw/jobs/main/'

driver = webdriver.Chrome() # 開啟Chrome

driver.get(url) # 前往這個網址
print(driver.page_source)
time.sleep(1)

driver.close()#關閉瀏覽器