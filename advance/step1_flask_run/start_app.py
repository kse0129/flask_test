# 사용자가 정의한 엔트리포인트
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "hello custom"