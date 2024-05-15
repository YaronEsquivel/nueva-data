# application/services/__init__.py
from flask import Blueprint

user_service_blueprint = Blueprint('user_service', __name__)

from microservice.services.user_service import *