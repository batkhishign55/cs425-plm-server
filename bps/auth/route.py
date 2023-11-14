from flask import Blueprint, render_template

from protect import adminProtect, userProtect

from .controller import AuthController

authbp = Blueprint(
    'auth', __name__, static_folder='static', template_folder='templates',
    url_prefix='/auth'
)


@authbp.post('/admin/login')
def adminLogin():
    return AuthController().adminLogin()


@authbp.post('/admin/logout')
@adminProtect
def adminLogout():
    return AuthController().adminLogout()


@authbp.post('/user/login')
def userLogin():
    return AuthController().userLogin()


@authbp.post('/user/logout')
@userProtect
def userLogout():
    return AuthController().userLogout()