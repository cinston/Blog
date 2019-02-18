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

class User(UserMixin, db.Model):
    """
    User model class to create users.
    Args:
        db.Model - connects our class to the database.
    """
    __tablename__ = 'users'