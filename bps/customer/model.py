import json
import pathlib
from flask import g

from db import get_db

class Customer:
    def __init__(self):
        self.db = get_db()
    
    def get(self):
        mycursor = self.db.cursor()
        mycursor.execute("SELECT * FROM customer;")
        res = mycursor.fetchall()
        print(res)
        return res

    def getSingleCustomer(self, id):
        customers=self.collections.get('customer')
        for cust in customers:
            if str(cust.get('id'))==id: 
                return cust
        return {}
