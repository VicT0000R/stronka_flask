import os 
class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///users.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'po co najebanemu piękne miasto nocą?'
    PERMANENT_SESSION_LIFETIME = 180  # w minutach


