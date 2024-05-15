# application/repositories/__init__.py
from flask import Blueprint

user_repository_blueprint = Blueprint('user_repository', __name__)

from microservice.repositories.user_repository import *