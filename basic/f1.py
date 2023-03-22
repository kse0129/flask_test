from flask import Flask, render_template, jsonify, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello world"

if __name__ == "__main__":
    # 웹 상의 기본 포트: http -> 80: 생략 가능
    # 나중에 웹서버(apache, nginx)와 연동
    app.run(debug=True, host="0.0.0.0", port=5000)