
#db연결 객체 생성 함수
def db_conn():
  import pymysql
    config = {
        'host': '127.0.0.1',
        'user': 'scott',
        'password': 'tiger',
        'database': 'work',
        'port': 3306,
        'charset': 'utf8',
        'use_unicode': True}

    # db 연결 객체 생성
    conn = pymysql.connect(**config)
    # SQL 실행 객체 생성
    cursor = conn.cursor()
    return conn, cursor

from flask import Flask, render_template, request #app생성 , html 호출

app = Flask(__name__) #object - > app object

#함수 장식자
@app.route('/') #기본 url 요청 -> 함수 호출
def index():
    return render_template("/app05/main.html")


@app.route('/docForm')
def dorForm():
    return render_template("/app05/docForm.html")

@app.route('/docPro', methods= ['GET','POST'])
def dorPro():
    if request.method =='POST':
        doc_id =int(request.form['id'])
        major = request.form['major']
        conn, cursor = db_conn()

        sql = f"""select*from dortors where doc_id={doc_id}
        and major_treat = '{major}'"""

        cursor.execute(sql)
        row= cursor.fetchone()

        if row: #로그인 성공 601 내과
            #print('login 성공')
            sql = f"""select d.doc_id,t.pat_id, TREAT_CONTENTS, TREAD_DATE
            from doctors d inner join treatment t 
            on d.doc_id = t.doc_id and d.doc_id = {doc_id}"""

            cursor.execute(sql)
            data=cursor.fetchall()

            if data:
                for row in data:
                    print(row)
                size = len(data)
            else:
                size = 0

            return render_template("/app05/docPro.html", dataset = data)

        else:
           return render_template(".app05/error.html", info='id 또는 진료과목 확인')

@app.route('/nurseForm', methods= ['GET','POST'])
def nurseForm():
    return render_template("/app05/error.html")

@app.route("/nursePro")
def nursePro():
    #파라미터 아이디 받기 -> 아이디 유무 파악 -> 있으면, 간호사 join환자
    #있으면, 간호사 join 환자 nursePro.html
    #없으면, error.html
    ''''
    < th > 담당 간호사 ID < / th >
    < th > 담당 의사 ID < / th >
    < th > 환자이름 < / th >
    < th > 환자 전화번호 < / th >
    '''
    pass
'''
@app.route('/select', methods=['GET','POST']) #기본 url 요청 -> 함수 호출
def select():
    if request.method == 'GET' :
        menu = int(request.args.get('menu'))
        # name = request.args.get('menu')
        print('menu : ', menu)

    if menu == 1 :#전체 레코드 조회
        data = select_func()
        size = len(data)
        return render_template("/app04/select.html", data=data, size=size)

    if menu == 2 :#레코드 추가
        return render_template("/app04/insert_form.html")

    if menu == 3 : # 레코드 수정
      return render_template("/app04/update_form.html")

#1. delete_form(code) -> get -> flask server(파라미터) -> delete
    if menu == 4 : # 레코드 삭제
       return render_template("/app04/delete_form.html")

@app.route("/insert", methods = ['GET', 'POST'])
def insert():
    try:
        if request.method == 'POST' :
            code = int(request.form['code'])
            name = request.form['name']
            su = int(request.form['su'])
            dan = int(request.form['dan'])

        conn, cursor =  db_conn()
        sql = f"insert into goods values({code},'{name}',{su},{dan})"
        cursor.execute(sql)  # 레코드 추가
        conn.commit()
        cursor.close(); conn.close()

        #레코드 조회
        data = select_func()
        size =len(data)
        print('data:', data)
        return render_template("/app04/select.html", data=data, size=size)
    except Exception as e :
        return render_template("/app04/error.html", error_info=e)

@app.route("/update", methods=['GET', 'POST'])
def update():
     try:
         if request.method == 'POST':
             code = int(request.form['code'])
             #name = int(request.form['name'])
             su = int(request.form['su'])
             dan = int(request.form['dan'])

         #레코드 수정
         conn, cursor = db_conn()
         sql = f"update goods set su={su}, dan={dan} where code={code}"
         cursor.execute(sql)  # 레코드 추가
         conn.commit()
         cursor.close(); conn.close()

         # 레코드 조회
         data = select_func()
         size = len(data)
         return render_template("/app04/select.html", data=data, size=size)
     except Exception as e:
         return render_template("/app04/error.html", error_info=e)

@app.route("/delete", methods=['GET', 'POST'])
def delete():
         try:
             if request.method == 'GET':
                 code = int(request.args.get['code'])
                 # name = int(request.form['name'])

             # 레코드 수정
             conn, cursor = db_conn()
             sql = f"delete from goods where code={code}"
             cursor.execute(sql)  # 레코드 추가
             conn.commit()
             cursor.close();
             conn.close()

             # 레코드 조회
             data = select_func()
             size = len(data)
             return render_template("/app04/select.html", data=data, size=size)
         except Exception as e:
             return render_template("/app04/error.html", error_info=e)
'''
#프로그램 시작점
if __name__ == "__main__":
    app.run(): #app실행

