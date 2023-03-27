from flask import render_template, request, url_for
from service.controllers import auth_bp as auth

@auth.route("/")
def home():
    # url_for("별칭.함수명") -> url 리턴
    print(url_for("auth_bp.login"))
    return render_template("auth/home.html")

@auth.route("/login")
def login():
    return render_template("auth/login.html")

@auth.route("/logout")
def logout():
    return render_template("auth/logout.html")

@auth.route("/signup")
def signup():
    return render_template("auth/signup.html")

@auth.route("/delete")
def delete():
    return render_template("auth/delete.html")