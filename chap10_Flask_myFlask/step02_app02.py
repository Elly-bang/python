'''
python 객체 (list, dict) -> 템플릿으로 보내기

JinJa2템플릿 표현식
{{object}}: 단일 객체 출력
{% for 변수 in 열거형 객체 %}: 열거형 객체 출력

flask; 웹 어플을 만드는 frame work
'''

import os
os.getcwd()
os.chdir(r'C:\ITWILL\3_Pythin-I\workspace\chap10_Flask\myFlask')
os.getcwd()

from flask import Flask
app=Flask(__name__)

@app.route('/')
def index():
    return render_template("/app02/index.html")

@app.route('temp01')
def temp01():
    uname = "홍길동" #단일객체
    goodList= ["딸기","포도","사과"] #열거형 객체
    return render_template("/app02/temp01_page.html", name=uname, glist=goodList)

@app.route('/temp02/<uname>')
def temp02(uname):
    return render_template("/app02/temp02_page.html",name=uname)

if__name__ == "__main__"
 app.run()



