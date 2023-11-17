
from flask import redirect, session


def adminProtect(func):
    def wrap(*args, **kwargs):
        print(session)
        if "object" not in session:
            return redirect("/")
        if session["object"]["type"] != "admin":
            return {"message": "not authorized"}, 401
        return func(*args, **kwargs)
    wrap.__name__ = func.__name__

    return wrap


def userProtect(func):
    def wrap(*args, **kwargs):
        print(session)
        if "object" not in session:
            return redirect("/")
        if session["object"]["type"] != "user":
            return {"message": "not authorized"}, 401
        return func(*args, **kwargs)
    wrap.__name__ = func.__name__

    return wrap


def protect(func):
    def wrap(*args, **kwargs):
        print(session)
        if "object" not in session:
            return redirect("/")
        return func(*args, **kwargs)
    wrap.__name__ = func.__name__

    return wrap

def getType():
    return session['object']['type']

def getUserId():
    return session['object']['user_id']

def getAdminId():
    return session['object']['emp_id']