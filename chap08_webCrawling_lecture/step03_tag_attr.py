'''
tag 속성과 내용 가져오기
- element : tag + 속성 + 내용
ex) <a href="www.naver.com">네이버 </a>
a : tag
href : 속성(attribute)
네이버 : 내용(content)
'''

from bs4 import BeautifulSoup

# 1. local file 가져오기
file = open("../data/html02.html", encoding='utf-8')
src = file.read()

# 2. html 파싱
html = BeautifulSoup(src, 'html.parser')
print(html)

# 3. a 태그 엘리머트 가져오기
links = html.find_all('a') # list
print(links)

# 4. a 태그 -> 속성(href(5), target(1))
urls = []
for link in links :
    print(link.string) # 내용 : 네이버
    atts = link.attrs # dict
    print(atts) # 속성 : {'href': 'www.naver.com'}
    # {'href': 'http://www.naver.com', 'target': '_blank'}
    #print(atts['href']) # value
    urls.append(atts['href']) # value
    try :
        print(atts['target']) #  '_blank'
    except Exception as e :
        print('예외 발생 :', e)

print(urls) # ['www.naver.com', 'http://www.naver.com', 'http://www.naver.com', 'www.duam.net', 'http://www.duam.net']
print(len(urls)) # 5

# 문) urls -> 정상 url -> new_urls
import re # findall, match, sub

#['http://www.naver.com', 'http://www.naver.com','http://www.duam.net']
new_urls = []
print('findall 사용 예')
for url in urls :
    tmp = re.findall('^http://', url) # 접두어 메타문자 이용
    if tmp : # 일치된 경우
        new_urls.append(url)
print(new_urls)

new_urls.clear() # list 원소 제거

print('match 사용 예')
for url in urls :
    tmp = re.match('^http://', url)
    if tmp :
        new_urls.append(url)
print(new_urls)
