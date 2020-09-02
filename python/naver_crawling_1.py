from bs4 import BeautifulSoup
from selenium import webdriver
import urllib.request

driver = webdriver.Chrome('chromedriver_win32\\chromedriver.exe')
driver.get("https://datalab.naver.com/keyword/realtimeList.naver?where=main")
html=driver.page_source
soup = BeautifulSoup(html, "html.parser")

def getkeyword():
    keywords=soup.select("span.item_title")
    #print(keywords)
    index=1
    for key in keywords:
        data = str(index)+". "+key.get_text()
        print(data)
        index+=1

getkeyword()
