from flask import Blueprint, render_template
from .controller import AuthController

authbp = Blueprint(
    'auth', __name__, static_folder='static', template_folder='templates',
    url_prefix='/auth'
)


@authbp.get('/')
def login():
    return render_template('login.html')


@authbp.post('/login')
def loginPost():
    return AuthController().login()


@authbp.post('/logout')
def logoutPost():
    return AuthController().logout()
