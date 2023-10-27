import json
import pathlib
from flask import g

from db import get_db


class log:
    def __init__(self):
        self.db = get_db()

    def get(self):
        mycursor = self.db.cursor()
        mycursor.execute("""SELECT * FROM parking_log_view""")
        return mycursor.fetchall()

    def getSinglelog(self, log_id):
        mycursor = self.db.cursor()
        mycursor.execute(
            """SELECT * FROM parking_log where log_id=%s""", (log_id,))
        return mycursor.fetchone()
