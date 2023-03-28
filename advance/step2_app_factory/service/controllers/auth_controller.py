from flask import render_template, request, url_for, current_app, jsonify
from service.controllers import auth_bp as auth
# 시간 정보 획득, 시간차 계산
from datetime import datetime, timedelta
import jwt

@auth.route("/")
def home():
    # url_for("별칭.함수명") -> url 리턴
    print(url_for("auth_bp.login"))
    return render_template("home.html")


@auth.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    else:
        # jwt 관련 체크 -> 정상(200), 오류(401: 권한 없음)
        # 1. uid, upw 획득
        uid = request.form.get('uid')
        upw = request.form.get('upw')
        # 2. uid, upw로 회원이 존재하는지 체크 -> 원래 DB, 임시로 값 비교
        if uid == 'guest' and upw == '1234':
            # 3. 회원이면 토큰 생성 (규격, 만료시간, 암호 알고리즘 지정, ...)
            payload = {
                # 저장할 정보는 고객 정보 기반으로 자유롭게 구성
                'id': uid,
                # 만료시간
                # 24시간 후에 토큰이 만료되는 것으로 설정
                'exp':  datetime.utcnow() + timedelta(seconds=60*60*24)
            }
            # 토큰 발급(시크릿키, 해시 알고리즘("HS256"), 데이터(payload) 필요)
            SECRET_KEY = current_app.config.get('SECRET_KEY')
            token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')

            # 4. 응답 전문 구성
        return jsonify({'code': 1, 'token': token})

@auth.route("/logout")
def logout():
    return render_template("logout.html")

@auth.route("/signup")
def signup():
    return render_template("signup.html")

@auth.route("/delete")
def delete():
    return render_template("delete.html")