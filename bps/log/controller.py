from flask import request
from .model import log


class logController:
    def __init__(self):
        self.model = log()

    def get(self):
        data = self.model.get()
        if not data:
            return {'message': 'no data found!'}, 404
        return {'data': data}

    def getParking(self):
        data = self.model.getParking()
        if not data:
            return {'message': 'no data found!'}, 404
        return {'data': data}

    def getSinglelog(self, log_id):
        data = self.model.getSinglelog(log_id)
        if not data:
            return {'message': 'no data found!'}, 404
        return {'data': data}

    def createLog(self):
        data = self.model.createLog(request.json)
        return {'data': data}
