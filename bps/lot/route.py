from flask import Blueprint, render_template
from .controller import LotController

lot = Blueprint(
    'lot', __name__, static_folder='static', template_folder='templates',
    url_prefix='/lot'
)


@lot.get('/api/')
def lotList():
    return LotController().get()
