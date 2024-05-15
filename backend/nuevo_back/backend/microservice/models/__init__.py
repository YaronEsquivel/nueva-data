# application/models/__init__.py
from flask import Blueprint

user_model_blueprint = Blueprint('user_model', __name__)

from microservice.models.user import *