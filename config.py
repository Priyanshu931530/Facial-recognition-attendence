import os


class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI', 'sqlite:////tmp/test.db')
    SECRET_KEY = 'your_secret_key'


class DevelopmentConfig(Config):
    DEBUG = True
