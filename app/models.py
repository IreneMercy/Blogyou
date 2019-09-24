from . import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime


class User(UserMixin,db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(255), nullable=False, unique=True)
    email = db.Column(db.String(255),nullable=True,unique=True)
    password = db.Column(db.String(255), nullable=False)
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String(255))
    blogs = db.relationship('Blog', backref='blogyou',lazy=True)
    comment = db.relationship('Comments', backref='commenting',lazy=True)


    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def set_password(self,password):
        password_hash = generate_password_hash(password)
        self.password = password_hash

    def check_password(self,password):
        return check_password_hash(self.password,password)

    def __repr__(self):
        return "User: %s"%str(self.username)


@login_manager.user_loader
def user_loader(user_id):
    return User.query.get(user_id)


class Blog(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(100),nullable=False)
    date_posted = db.Column(db.DateTime,nullable=False,default=datetime.utcnow)
    blog = db.Column(db.Text,nullable=False)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'),nullable=False)
    comment_it = db.relationship('Comments', backref='user_comment',lazy=True)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


    def __repr__(self):
        return f"Blog('{self.title}', '{self.date_posted}')"




class Comments(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    comment = db.Column(db.String(255),nullable=False)
    date_posted = db.Column(db.DateTime,nullable=False,default=datetime.utcnow)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    blog_id = db.Column(db.Integer,db.ForeignKey('blog.id'))

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


    def __repr__(self):
        return f"Comments('{self.comment}', '{self.date_posted}')"

class Subscribe(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    email = db.Column(db.String(100))
    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
    def __repr__(self):
        return f"Comments('{self.email}')"


class Quotes:
    def __init__(self,author,quote,permalink):
        self.author = author
        self.quote = quote
        self.permalink = permalink
