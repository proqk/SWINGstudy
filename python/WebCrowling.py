from bs4 import BeautifulSoup
import urllib.request

html = urllib.request.urlopen("http://www.swu.ac.kr/www/swuniversity.html")
result = BeautifulSoup(html.read(), "html.parser")
search = result.findAll("a") #a태그 찾기
print("*** 서울여자대학교 학과 및 홈페이지 정보 ***\n")
print("학과 \t\t\t 홈페이지\n")

for s in search:
	if s.text == "공동기기실" or s.text == "자율전공학부" or "교육원" in s.text or "대학원" in s.text :
		continue
	else:
		html2 = urllib.request.urlopen("http://www.swu.ac.kr" + s["href"])#각 과들의 전공페이지 요청
		result2 = BeautifulSoup(page.read(), "html.parser")
		search2 = result2.find("a", { "class","btn btn_xl btn_blue_gray" })#학과 홈페이지 본문에서 태그 추출

		if search2 is None:
			print(s.text + "\t\t홈페이지가 존재하지 않음")
		elif 'bacha' in search2['href']:
			print(s.text + "\t\t홈페이지가 존재하지 않음")
		else:
			print(s.text + "\t\t" + pageUrl["href"])
