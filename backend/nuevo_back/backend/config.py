# config.py
import os
from dotenv import load_dotenv

def config_dotenv():
    dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
    print('dotenv_path', dotenv_path)
    if os.path.exists(dotenv_path):
        load_dotenv(dotenv_path)

class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    ENV = "development"
    DEBUG = True

class QualityConfig(Config):
    ENV = "quality"
    DEBUG = True

class ProductionConfig(Config):
    ENV = "production"
    DEBUG = False
