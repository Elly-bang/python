'''
원격 서버의  웹 수집
'''

from bs4 import BeautifulSoup # source -> html 파싱
import urllib.request as res # 별칭 : 원격 서버 파일 요청

url = "http://www.naver.com/index.html"

# 1. 원격 서버 url 요청
req = res.urlopen(url) # 요청 -> 응답
print(req) # object info
data = req.read() # source
print(data) # <!doctype html> -> source

# 2. source(문자열) -> html 형식 : html 파싱
src = data.decode('utf-8') # 디코딩 -> 소스
html = BeautifulSoup(src, 'html.parser') # source -> html
print(html)

# 3. Tag 내용 가져오기
link = html.find('a') # <a href='url'>내용 </a>
print(link)
'''
element : <시작태그  속성명='값'> 내용 </종료태그>
'''
print('a 태그 내용 :', link.string) # 태그 내용 추출
# a 태그 내용 : 연합뉴스 바로가기




