from flask import g

import mysql.connector


def init_db():
    print('Initializing db connection...')
    g.db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="password",
        database="plm"
    )


def get_db():
    if 'db' not in g:
        init_db()

    return g.db
