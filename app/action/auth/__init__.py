# coding:utf-8
from flask import Blueprint

auth = Blueprint('auth', __name__,)

from app.action.auth import views