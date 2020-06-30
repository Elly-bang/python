'''
<작업 순서>
1.index 페이지 작성-> 동 입력
2.flask server에서 동(파라미터 ) 받기
3. db연동  -> 주소 조회
4. 조회 결과 -> result페이지 출력
'''


import os
os.getcwd()
os.chdir(r'C:\ITWILL\3_Pythin-I\workspace\chap10_Flask\myFlask')
os.getcwd()

from flask import Flask, render_template, request #app생성 , html 호출

app = Flask(__name__) #object - > app object

#함수 장식자
@app.route('/') #기본 url 요청 -> 함수 호출
def index():
    return render_template("/app03/index.html") #'/search'

@app.route('/search', methods =['POST','GET'])
def search() :
    if request.method == 'POST' :
        dong = request.form['dong'] #동
        print('dong=', dong)

        import pymysql
        config = {
            'host': '127.0.0.1',
            'user': 'scott',
            'password': 'tiger',
            'database': 'work',
            'port': 3306,
            'charset': 'utf8',
            'use_unicode': True}

        try:
            # 1. db 연동 객체
            conn = pymysql.connect(**config)
            # 2. cursor 객체 : sql문
            cursor = conn.cursor()


            # 4. 레코드 조회
            sql = "select * from zipcode_tab"
            cursor.execute(sql)
            data = cursor.fetchall()
            #print('data :', data)
            if data:  # True : 검색
                sql = f"select * from zipcode_tab where dong like '%{dong}%'"
                cursor.execute(sql)
                data2 = cursor.fetchall()
                if data2 :
                    for row in data2 :
                        print("[%s]    %s   %s   %s  %s"%row)

                    print('검색된 레코드 수:', len(data2))

                    size=len(data2)
                else :
                    print('검색된 레코드 없음')
                    size = 0


        except Exception as e:
            print('db 연동 오류 :', e)
            conn.rollback()
        finally:
            cursor.close()
            conn.close()

    return render_template("/app03/result.html", dong=dong, data=data2, size=size)

#프로그램 시작점
if __name__ == "__main__":
    app.run() #app실행

