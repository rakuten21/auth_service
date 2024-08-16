import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'authentication_service')
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = ''
    MYSQL_DB = 'auth_db'

    