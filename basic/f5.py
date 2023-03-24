'''
- POST 방식으로 데이터 전송하기
    - 클라이언트 (Json, Xml, Text, Form(키=값&키=값...), Form-encode, Graphql, Binary)
        - form 전송 (화면 깜빡임 -> 화면 전환)
            - Form(키=값&키=값...), Form-encode 형식
            <form action="http://127.0.0.1:5000/link" method="post" >
                <input name="name" value="hello"/>
                <input name="age" value="100"/>
                <input type="submit" value="전송"/>
            </form>
        - ajax (jQuery로 표현, 화면 유지)
            - Json, Xml, Text, Form(키=값&키=값...), Form-encode, Graphql, Binary 형식
            $.get({
                url: "http://127.0.0.1:5000/link",
                data: "name=hello&age=100",
                success: (res)=>{},
                error: (res)=>{}
            })
    
    - 서버
        - post 방식 데이터 추출
            name = request.form.get('name')
            age = request.form.get('age')

- /link 로 요청하는 방식은 다양할 수 있다. 단, 사이트 설계 상 1가지로만 정의되어 있다면
    다른 방식의 접근은 모두 비정상적인 접근이다(웹크롤링, 스크래핑, 해킹 등이 대상)
        이런 접근을 필터링할 것인지가 보안의 기본사항
'''
from flask import Flask, render_template, jsonify, request, redirect, url_for
from d4 import login_db

app = Flask(__name__)

# @app.route() -> 기본적으로 GET 방식
# 메소드 추가는 methods=['POST', ..]
@app.route('/login', methods=['GET', 'POST'])
def login():
    # method별 분기
    if request.method == 'GET':
        return render_template('login.html')   
    else: # request.method == 'POST'
        # 1. 로그인 정보 획득
        user_id = request.form.get('uid')
        user_pw = request.form.get('upw') # 암호는 차후에 암호화해야함(관리자도 볼 수 없음)
        print(user_id, user_pw)
        # 2. 회원 여부를 쿼리
        result = login_db(user_id, user_pw)
        # 3. 회원이면
        if result:
            # 3-1. 세션 생성, 기타 필요한 조치 수행
            # 3-2. 서비스 메인 화면으로 이동
            return
        # 4. 회원이 아니면
        else:
            # 4-1. 적당한 메세지 후 다시 로그인 유도
            # render_template(): jinja2 템플릿 엔진 사용
            return render_template('error.html', msg='로그인 실패')
        # return redirect('https://www.naver.com') # 요청을 다른 url로 포워딩

if __name__ == "__main__":
    app.run(debug=True)