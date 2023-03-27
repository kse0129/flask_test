from flask import render_template, request, url_for
from service.controllers import auth_bp as auth

@auth.route("/")
def home():
    # url_for("별칭.함수명") -> url 리턴
    print(url_for("auth_bp.login"))
    return render_template("home.html")

@auth.route("/login")
def login():
    return render_template("login.html")

@auth.route("/logout")
def logout():
    return render_template("logout.html")

@auth.route("/signup")
def signup():
    return render_template("signup.html")

@auth.route("/delete")
def delete():
    return render_template("delete.html")