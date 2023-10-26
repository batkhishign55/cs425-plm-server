import json
import pathlib
from flask import g

from db import get_db


class Lot:
    def __init__(self):
        self.db = get_db()

    def get(self):
        mycursor = self.db.cursor()
        mycursor.execute("""SELECT * FROM parking_lot""")
        return mycursor.fetchall()

    def getSingleLot(self, lot_id):
        mycursor = self.db.cursor()
        mycursor.execute(
            """SELECT * FROM parking_lot where lot_id=%s""", (lot_id,))
        return mycursor.fetchone()
