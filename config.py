import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'my-secret-key')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'https://github.com/Zachariarian/actaria.git/')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY', 'my-jwt-secret-key')
