from app import myapp_obj
from flask import render_template

@myapp_obj.route("/")
def hello():
    name = "ricardo"
    return render_template('hello.html', names = name)

@myapp_obj.route("/admin")
def admin():
    return "Administration Page!"

@myapp_obj.route("/login")
def login():
    return render_template('login.html')
