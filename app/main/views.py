from flask import render_template, request, redirect, url_for
from . import main
from app.models import User,Blog, Comments, Quotes, Subscribe
from flask_login import login_user,login_required, logout_user,current_user
import requests
from .. import mail
from ..email import mail_message
from flask_mail import Message


response = requests.get('http://quotes.stormconsultancy.co.uk/random.json')
quotes = response.json()
author = quotes.get('author')
quote = quotes.get('quote')
permalink = quotes.get('permalink')
quoty = Quotes(author,quote,permalink)


@main.route('/')
def home():
    title = "YUBlog"
    blogs = Blog.query.all()
    comment = Comments.query.all()
    quote = quoty
    print(quotes)
    return render_template('index.html', title=title,blogs=blogs,comment=comment, quote=quote)

@main.route('/blogs', methods=['POST','GET'])
@login_required
def blogs():

    if request.method == 'POST':
        form = request.form
        title = form.get('title')
        blog = form.get('blog')
        if title==None or blog==None:
            error = "All fields are required"
            return render_template('create_blog.html', error=error)
        blog = Blog(title=title,blog=blog, user_id=current_user.id)
        blog.save()
        
        return redirect(url_for('main.home'))
    return render_template('create_blog.html')


@main.route("/blogs/<int:blog_id>", methods=['GET', 'POST'])
@login_required
def update_post(blog_id):
   post = Blog.query.all()
   print('------..........', post)

   # if post.blogyou != current_user:
   #     abort(403)
   #     form = request.form
   #     post.title = form.get('title')
   #     post.blog = form.get('blog')
   #     # if post.title==None or post.blog==None:
   #     #     error = "All fields are required"
   #     #     return render_template('create_blog.html', error=error)
   #     db.session.commit()
   #     flash('Your post has been updated!', 'success')
   #     return redirect(url_for('main.home'))
   # # elif request.method == 'GET':
   #     form.get('title') = post.title
   #     form.get('blog') = post.blog
   return render_template('create_blog.html', title='Update Post')

@main.route('/delete/<int:comment_id>')
@login_required
def delete(comment_id):
    comm = Comments.query.get(comment_id)
    comm.delete()
    return redirect(url_for('main.home'))


@main.route('/del/<int:blog_id>', methods=['POST','GET'])
@login_required
def del_blog(blog_id):
    blog = Blog.query.get(blog_id)
    blog.delete()
    return redirect(url_for('main.home'))


@main.route('/comment/<int:blog_id>', methods=['GET','POST'])
def comment(blog_id):
    if request.method == 'POST':
        comment = request.form.get('comment')
        blog = Blog.query.filter_by(id=blog_id).first()
        comment = Comments(comment=comment,blog_id=blog.id)
        comment.save()
        return redirect(url_for('main.home',blog=blog))
    return render_template('index.html')

@main.route('/subscribe', methods=['GET','POST'])
def subscribe():
    if request.method == "POST":
        form = request.form
        email = form.get("email")
        if email==None:
            error = "Enter your email required"
            return render_template('index.html', error=error)
        user = Subscribe(email=email)
        user.save()
        users = Subscribe.query.all()
        for user in users:
            mail_message("Hello", "email/subscribe",user.email,user=user)
        return redirect(url_for("main.home"))
    return render_template('index.html')
