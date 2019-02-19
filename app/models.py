from . import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    """
    Function that retrieves a user
    """
    return User.query.get(int(user_id))
class Quote:

   def __init__(self,id,author,quote):
       self.id =id
       self.author = author
       self.quote = quote

         

class User(UserMixin, db.Model):
    """
    User model class to create users.
    Args:
        db.Model - connects our class to the database.
    """
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key = True)
    firstname =db.Column(db.String(255))
    lastname =db.Column(db.String(255))
    username = db.Column(db.String(255),index =True)
    email = db.Column(db.String(255), unique = True, index = True)
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    pass_secure = db.Column(db.String(255))

    blogs = db.relationship('Blog', backref = 'user', lazy = 'dynamic')
    comments = db.relationship('Comment', backref = 'user', lazy = 'dynamic')

    @property
    def password(self):
        """
        Method that raises an error when a user tries to access the passwords.
        """
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        """
        Method that generates hashes for passwords.
        """
        self.pass_secure = generate_password_hash(password)

    def verify_password(self, password):
        """
        Method that checks if the password hashes are the same.
        """
        return check_password_hash(self.pass_secure, password)

    def get_blogs(self):
        """
        Method that gets all blogs for a particular user
        """
        user = User.query.filter_by(id = self.id).first()
        return user.blogs

    def __repr__(self):
        """
        Method used for debugging the database.
        """
        return f'User {self.username}'

class Blog(db.Model):
    """
    Blog model class to create blogs.
    Args:
        db.Model - connects our class to the database.
    """
    __tablename__ = 'blogs'

    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(255))
    description = db.Column(db.String(700))
    category = db.Column(db.String)
    posted = db.Column(db.DateTime, default=datetime.utcnow)
    upvotes = db.Column(db.Integer)
    downvotes = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    comments = db.relationship('Comment', backref = 'blog', lazy = 'dynamic')

    def save_blog(self):
        """
        Method that saves a blog to the database
        """
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_blogs(cls,category):
        blogs = Blog.query.filter_by(category=category).all()
        return blogs

    @classmethod
    def get_blog(cls,id):
        blog = Blog.query.filter_by(id=id).first()

        return blog

    @classmethod
    def count_blogs(cls,uname):
        user = User.query.filter_by(username=uname).first()
        blogs = Blog.query.filter_by(user_id=user.id).all()

        blogs_count = 0
        for blog in blogs:
            blogs_count += 1

        return blogs_count

    def get_comments(self):
        """
        Method that retrieves a blog's comments.
        """
        blog = Blog.query.filter_by(id = self.id).first()
        comments = Comment.query.filter_by(pitch_id = blog.id).all()
        return comments

class Comment(db.Model):
    """
    Comment model class to create comments.
    Args:
        db.Model - connects our class to the database.
    """
    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key = True)
    content = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    blog_id = db.Column(db.Integer, db.ForeignKey('blogs.id'))

    def save_comment(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        """
        Method used for debugging the database.
        """
        return f'User {self.content}'