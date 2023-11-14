from flask import abort, request
from .model import Vehicle


class VehicleController:
    def __init__(self):
        self.model = Vehicle()

    def get(self):
        data = self.model.get()
        if not data:
            abort(404)
        return {'status': True, 'data': data, 'message': ''}

    def getSingleVehicle(self, vehicle_id):
        data = self.model.getSingleVehicle(vehicle_id)
        if not data:
            abort(404)
        return {'status': True, 'data': data, 'message': ''}

    def updateVehicle(self):
        try:
            data = self.model.updateVehicle(request.json)
        except Exception as e:
            print(str(e))
            abort(500, str(e))
        return {'status': True, 'data': data, 'message': ''}

    def deleteVehicle(self):
        try:
            data = self.model.deleteVehicle(request.json)
        except Exception as e:
            print(str(e))
            abort(500, str(e))
        return {'status': True, 'data': data, 'message': ''}

    def createVehicle(self):
        try:
            data = self.model.createVehicle(request.json)
        except Exception as e:
            print(str(e))
            abort(500, str(e))
        return {'status': True, 'data': data, 'message': ''}
