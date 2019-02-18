import os

class Config:
    """
    General configuration parent class
    """
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://winston:zagadat@localhost/blog'
    UPLOADED_PHOTOS_DEST = 'app/static'