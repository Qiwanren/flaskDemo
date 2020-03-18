# coding:utf-8

from app.auth import auth
from flask import jsonify
import json

dept_data = [
    {
        'name': '部门1',
        'id': 12345
    },
    {
        'name': '部门2',
        'id': 12346
    }
]

@auth.route('/<int:id>', methods=['GET', ])
def get(id):
    for dept in dept_data:
        if int(dept['id']) == id:
            return jsonify(status='success', dept=dept)

    return jsonify(status='failed', msg='dept not found')


@auth.route('/auths', methods=['GET', ])
def get_depts():
    data = {
        'status': 'success',
        'auths': dept_data
    }
    return json.dumps(data, ensure_ascii=False, indent=1)
