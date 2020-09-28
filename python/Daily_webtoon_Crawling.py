from bs4 import BeautifulSoup
import urllib.request

html = urllib.request.urlopen("https://comic.naver.com/webtoon/weekday.nhn")
soup = BeautifulSoup(html.read(),"html.parser") #웹 페이지 파싱
html.close() #닫기

def getkeyword():
    daily_list=soup.findAll('div',{'class':'col_inner'})
    week=['월요웹툰', '화요웹툰', '수요웹툰', '목요웹툰', '금요웹툰', '토요웹툰', '일요웹툰']
    
    for day in range(len(daily_list)):
        print("["+week[day]+"]")
        titles=daily_list[day].findAll('a', {'class': 'title'})
        titles_txt = [t.text for t in titles]
        
        index=1
        for i in titles:
            data = str(index)+". "+i.get_text()
            print(data)
            index+=1
        print("\n\n=======================\n\n")

getkeyword()
