'''
    클라이언트가 서버에게 데이터를 보내는 방법
    - 방법 : method(GET, POST, PUT, ...) 
        -> http 프로토콜(통신규약, 서로 데이터를 주고받는 약속)에서 정의
        http는 헤더(고정크기)를 먼저 전송, 바드(가변크기)를 나중에 전송
        GET 방식은 헤더만 전송 -> 고정 크기만 전송 : 전송량의 최대치가 정해져있음
            http 헤더만 알면 패킷(전송 데이터)을 가로채서 데이터를 해킹할 수 있음
        POST 방식은 헤더(바디의 크기가 세팅되어 있음) 전송 -> 바디 전송 : 대량 전송 가능
            구조를 모르기 때문에 보안에 상대적으로 우수, 암호화 가능
    - 방식
        - form 전송 : <form> 태그 사용
        - ajax 전송 : 백그라운드로 서버와 통신
        - websocket : 웹소켓을 열어서 통신
        - 동적파라미터 : get의 헤더를 활용. url에 데이터를 넣어서 보내는 방식

    - 동적파라미터
        - http 헤더의 주소 정보를 활용

'''
from flask import Flask, render_template, jsonify, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello world"

# 동적 파라미터, 문자열 타입으로 전송
# 용량은 헤더 사이즈, 주소크기를 초과할 수 없다
# 파라미터는 함수 인자를 통해서 함수 내부로 진입
@app.route('/news/<news_id>')
def news(news_id):
    return "전달된 데이터 [ %s ]" % news_id

# 1개 이상도 전달 가능?
@app.route('/<news_id>/news2/<news_author>')
def news2(news_id, news_author):
    return "전달된 데이터 [ %s, %s ]" % (news_id, news_author)

# 타입 제한(int, float, path) 가능?
# int, float
@app.route('/news3/<int:news_id>')
def news3(news_id):
    return "전달된 데이터 [ %d ]" % news_id

# path
# 전달값을 무한대로 늘려주는 옵션
@app.route('/news4/<path:news_id>')
def news4(news_id):
    # 정보를 구분해서 여러개로 전달 가능(가변적)
    return "전달된 데이터 [ %s ]" % news_id

if __name__ == "__main__":
    app.run(debug=True)