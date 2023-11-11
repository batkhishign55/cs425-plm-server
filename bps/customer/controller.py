from flask import abort, request
from .model import Customer


class CustController:
    def __init__(self):
        self.model=Customer()

    def get(self):
        data = self.model.get()
        if not data:
            abort(404)
        return {'status': True, 'data': data, 'message': ''}

    def getSingleCustomer(self, cust_id):
        data = self.model.getSingleCustomer(cust_id)
        if not data:
            abort(404)
        return {'status': True, 'data': data, 'message': ''}

    def updateCust(self):
        try:
            print(request.json)
            data = self.model.updateCust(request.json)
        except Exception as e:
            abort(500, str(e))
        return {'status': True, 'data': data, 'message': ''}

    def deleteCust(self):
        try:
            data = self.model.deleteCust(request.json)
        except Exception as e:
            abort(500, str(e))
        return {'status': True, 'data': data, 'message': ''}
    
    def createCust(self):
        try:
            data = self.model.createCust(request.json)
        except Exception as e:
            print(str(e))
            abort(500, str(e))
        return {'status': True, 'data': data, 'message': ''}
