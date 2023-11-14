from flask import Blueprint, render_template

from protect import adminProtect

from .controller import UserController

user = Blueprint(
    'user', __name__, static_folder='static', template_folder='templates',
    url_prefix='/user'
)


@user.before_request
@adminProtect
def login_required():
    pass


@user.get('/')
def index():
    return render_template('user.html')


@user.get('/api/detail')
def detailUser():
    return UserController().getUser()
