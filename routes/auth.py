from flask import Blueprint, render_template

auth = Blueprint("auth", __name__, url_prefix="/auth")

@auth.route('/login')
def login_view():
    return render_template("pages/auth/login.html")

@auth.route('/register')
def register_view():
    return render_template("pages/auth/register.html")