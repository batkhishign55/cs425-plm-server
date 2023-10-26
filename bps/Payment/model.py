import json
import pathlib
from flask import g

from db import get_db

class Payment:
    def __init__(self):
        self.db = get_db()
    
    def get(self):
        mycursor = self.db.cursor()
        mycursor.execute("SELECT * FROM payment;")
        return mycursor.fetchall()

    def getSinglePayment(self, id):
        payments=self.collections.get('payment')
        for payment in payments:
            if str(payment.get('id'))==id: 
                return payment
        return {}
