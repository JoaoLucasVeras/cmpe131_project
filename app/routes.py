from app import myapp_obj
from flask import render_template, redirect, flash
from app.forms import LoginForm

@myapp_obj.route("/")
def home():
    return render_template('base.html')

@myapp_obj.route("/admin")
def admin():
    return "Administration Page!"

@myapp_obj.route("/login", methods=['POST', 'GET'])
def login():
    current_form = LoginForm()
    #taking input from user and doing something with it
    if(current_form.validate_on_submit()):
        flash('quick way to debug')
        print(current_form.username.data, current_form.password.data)    
        return redirect('/')
    if(current_form.username.data == "" or current_form.password.data == ""):
        flash("error")

    a = 1
    name = "ricardo"
    return render_template('login.html', name = name, a=a, form=current_form)
