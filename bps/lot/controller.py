from flask import request
from .model import Lot


class LotController:
    def __init__(self):
        self.model = Lot()

    def get(self):
        data = self.model.get()
        if not data:
            return {'message': 'no data found!'}, 404
        return {'data': data}

    def getAll(self):
        data = self.model.getAll()
        if not data:
            return {'message': 'no data found!'}, 404
        return {'data': data}

    def getSingleLot(self, lot_id):
        data = self.model.getSingleLot(lot_id)
        if not data:
            return {'message': 'no data found!'}, 404
        return {'data': data}

    def updateLot(self):
        data = self.model.updateLot(request.json)
        return {'data': data}

    def deleteLot(self):
        data = self.model.deleteLot(request.json)
        return {'data': data}

    def createLot(self):
        data = self.model.createLot(request.json)
        return {'data': data}

    def getSpot(self):
        data = self.model.getSpot(request.args.get('lotId'))
        if not data:
            return {'message': 'no data found!'}, 404
        return {'data': data}
