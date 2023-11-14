from flask import g

import mysql.connector
from flask import current_app

def init_db(app):
    print('Initializing db connection...')
    app.config['DB'] = mysql.connector.connect(
        host="localhost",
        user="root",
        password="password",
        database="plm"
    )

def get_db():
    db = current_app.config.get('DB', None)
    if db is None:
        init_db(current_app)

    return db

def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()

def init_app(app):
    app.teardown_appcontext(close_db)
