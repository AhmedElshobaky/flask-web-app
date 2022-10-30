from datetime import datetime
from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(64), index = True, unique = True)
    email = db.Column(db.String(120), index = True, unique = True)
    password_hash = db.Column(db.String(128))
    
    
    posts = db.relationship('Post', backref='auther', lazy='dynamic')
    
    # repr function shows how objects of this class are printed
    def __repr__(self):
        return '<User {}>'.format(self.username)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key =True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index = True, default = datetime.utcnow)
    
    # Note that when passing db model to db.relatoinship 
    # we pass the name of class even if it had capital letters
    # passing db model to foreignkey should be with database table 
    # name which is all small and has '_' if it is more than one word
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post {}>'.format(self.body)