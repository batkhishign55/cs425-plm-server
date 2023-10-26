import json
import pathlib
from flask import g

from db import get_db

class Reservation:
    def __init__(self):
        self.db = get_db()
    
    def get(self):
        mycursor = self.db.cursor()
        mycursor.execute("SELECT * FROM reservation;")
        res = mycursor.fetchall()
        print(res)
        return res

    def getSingleReservation(self, id):
        reservation=self.collections.get('reservation')
        for reserve in reservation:
            if str(reserve.get('id'))==id: 
                return reserve
        return {}
