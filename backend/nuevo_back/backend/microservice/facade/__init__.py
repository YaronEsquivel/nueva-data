# application/facade/__init__.py
from flask import Blueprint

user_facade_blueprint = Blueprint('user_facade', __name__)

from microservice.facade.user_facade import *