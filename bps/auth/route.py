from flask import Blueprint, render_template, session

from protect import adminProtect, userProtect

from .controller import AuthController

authbp = Blueprint(
    'auth', __name__, static_folder='static', template_folder='templates',
    url_prefix='/auth'
)


@authbp.post('/admin/login')
def adminLogin():
    return AuthController().adminLogin()


@authbp.post('/logout')
def logout():
    return AuthController().logout()


@authbp.get('/admin/check')
def adminCheck():
    if "object" not in session:
        return {"message": "not authorized"}, 401
    if session["object"]["type"] != "admin":
        return {"message": "not authorized"}, 401
    return "has session", 200


@authbp.post('/user/login')
def userLogin():
    return AuthController().userLogin()


@authbp.get('/user/check')
def userCheck():
    if "object" not in session:
        return {"message": "not authorized"}, 401
    if session["object"]["type"] != "user":
        return {"message": "not authorized"}, 401
    return "has session", 200