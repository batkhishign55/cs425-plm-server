from flask import abort, request
from .model import Lot


class LotController:
    def __init__(self):
        self.model = Lot()

    def get(self):
        data = self.model.get()
        if not data:
            abort(404)
        return {'status': True, 'data': data, 'message': ''}

    def getSingleLot(self, lot_id):
        data = self.model.getSingleLot(lot_id)
        if not data:
            abort(404)
        return {'status': True, 'data': data, 'message': ''}

    def updateLot(self):
        try:
            data = self.model.updateLot(request.json)
        except Exception as e:
            print(str(e))
            abort(500, str(e))
        return {'status': True, 'data': data, 'message': ''}

    def deleteLot(self):
        try:
            data = self.model.deleteLot(request.json)
        except Exception as e:
            print(str(e))
            abort(500, str(e))
        return {'status': True, 'data': data, 'message': ''}

    def createLot(self):
        try:
            data = self.model.createLot(request.json)
        except Exception as e:
            print(str(e))
            abort(500, str(e))
        return {'status': True, 'data': data, 'message': ''}
