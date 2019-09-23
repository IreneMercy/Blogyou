from flask import render_template, request, redirect, url_for
from . import main
from app.models import User
from flask_login import login_user,login_required, logout_user


@main.route('/')
@login_required
def home():
    title = "YUBlog"
    return render_template('index.html', title=title)
