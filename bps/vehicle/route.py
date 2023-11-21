from flask import Blueprint, render_template
from .controller import VehicleController

vehicle = Blueprint(
    'vehicle', __name__, static_folder='static', template_folder='templates',
    url_prefix='/vehicle'
)

@vehicle.get('/create/')
def create():
    return render_template('vehicleForm.html')

@vehicle.get('/<vehicle_id>')
def index(vehicle_id):
    return render_template('vehicleForm.html')

@vehicle.get('/api/')
def vehicleList():
    return VehicleController().get()

@vehicle.get('/api/detail/<vehicle_id>')
def vehicleDetail(vehicle_id):
    return VehicleController().getSingleVehicle(vehicle_id)

@vehicle.post('/api/update')
def vehicleUpdate():
    return VehicleController().updateVehicle()

@vehicle.delete('/api/')
def vehicleDelete():
    return VehicleController().deleteVehicle()

@vehicle.post('/api/create')
def vehicleCreate():
    return VehicleController().createVehicle()
