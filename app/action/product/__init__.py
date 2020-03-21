# coding:utf-8
from flask import Blueprint

product = Blueprint('product', __name__,)

from app.action.product import prouductManage
