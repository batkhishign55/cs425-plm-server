from flask import request
from .model import Customer


class CustController:
    def __init__(self):
        self.model = Customer()

    def get(self):
        data = self.model.get()
        if not data:
            return {'message': "no data found!"}, 404
        return {'data': data}

    def getSingleCustomer(self, cust_id):
        data = self.model.getSingleCustomer(cust_id)
        if not data:
            return {'message': "no data found!"}, 404
        return {'data': data}

    def updateCust(self):
        data = self.model.updateCust(request.json)
        return {'data': data}

    def deleteCust(self):
        data = self.model.deleteCust(request.json)
        return {'data': data}

    def createCust(self):
        data = self.model.createCust(request.json)
        return {'data': data}

    def allUsers(self):
        data = self.model.allUsers()
        if not data:
            return {'message': "no data found!"}, 404
        return {'data': data}
