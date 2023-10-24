from flask import Blueprint, render_template
from .controller import UserController

user=Blueprint(
    'user', __name__, static_folder='static', template_folder='templates',
    url_prefix='/user'
    )

@user.get('/')
def index():
    return render_template('user.html')

@user.get('/api/detail')
def detailUser():
    return UserController().getUser()