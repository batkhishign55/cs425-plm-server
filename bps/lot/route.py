from flask import Blueprint, render_template, session

from protect import adminProtect, protect
from .controller import LotController

lot = Blueprint(
    'lot', __name__, static_folder='static', template_folder='templates',
    url_prefix='/lot'
)


@lot.before_request
@protect
def login_required():
    pass


@lot.get('/')
def create():
    return render_template('lotForm.html', type=session["object"]["type"])


@lot.get('/<lot_id>')
def index(lot_id):
    return render_template('lotForm.html', type=session["object"]["type"])


@lot.get('/api/')
def lotList():
    return LotController().get()


@lot.get('/api/all')
def lotAll():
    return LotController().getAll()


@lot.get('/api/detail/<lot_id>')
def lotDetail(lot_id):
    return LotController().getSingleLot(lot_id)


@lot.post('/api/update')
def lotUpdate():
    return LotController().updateLot()


@lot.delete('/api/')
def lotDelete():
    return LotController().deleteLot()


@lot.post('/api/create')
def lotCreate():
    return LotController().createLot()


@lot.get('/api/spot')
def lotSpot():
    return LotController().getSpot()
