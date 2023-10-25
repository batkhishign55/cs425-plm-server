from flask import Blueprint, render_template
from .controller import LotController

lot = Blueprint(
    'lot', __name__, static_folder='static', template_folder='templates',
    url_prefix='/lot'
)


@lot.get('/<lot_id>')
def index(lot_id):
    return render_template('lot.html')

@lot.get('/api/')
def lotList():
    return LotController().get()

@lot.get('/api/detail/<lot_id>')
def lotDetail(lot_id):
    return LotController().getSingleLot(lot_id)
