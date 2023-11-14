

from flask import redirect, session, url_for


def protect(func):
    def wrap(*args, **kwargs):
        print(session)
        # if "email" not in session:
        #     return redirect(url_for("auth.login"))
        return func(*args, **kwargs)
    wrap.__name__ = func.__name__

    return wrap
