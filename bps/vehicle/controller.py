from flask import abort, request
from .model import Vehicle


class VehicleController:
    def __init__(self):
        self.model = Vehicle()

    def get(self):
        data = self.model.get()
        if not data:
            return {'message': 'no data found!'}, 404
        return {'data': data}

    def getSingleVehicle(self, vehicle_id):
        data = self.model.getSingleVehicle(vehicle_id)
        if not data:
            return {'message': 'no data found!'}, 404
        return {'data': data}

    def updateVehicle(self):
        data = self.model.updateVehicle(request.json)
        return {'data': data}

    def deleteVehicle(self):
        data = self.model.deleteVehicle(request.json)
        return {'data': data}

    def createVehicle(self):
        data = self.model.createVehicle(request.json)
        return {'data': data}
