from flask import Blueprint, render_template

from protect import adminProtect
from .controller import LotController

lot = Blueprint(
    'lot', __name__, static_folder='static', template_folder='templates',
    url_prefix='/lot'
)

@lot.before_request
@adminProtect
def login_required():
    pass


@lot.get('/')
def create():
    return render_template('lotForm.html')


@lot.get('/<lot_id>')
def index(lot_id):
    return render_template('lotForm.html')


@lot.get('/api/')
def lotList():
    return LotController().get()


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
