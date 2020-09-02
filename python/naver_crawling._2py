from bs4 import BeautifulSoup
import requests

json = requests.get('https://www.naver.com/srchrank?frm=main').json()

ranks = json.get("data")
#print(ranks)

for key in ranks:
    rank = key.get("rank")
    keyword = key.get("keyword")
    print(rank, keyword)
