from flask import Blueprint

from protect import protect

from .controller import ReservationController

reservation = Blueprint(
    'reservation', __name__, static_folder='static', template_folder='templates',
    url_prefix='/res'
)


@reservation.before_request
@protect
def login_required():
    pass


@reservation.get('/api/')
def reservationList():
    return ReservationController().get()


@reservation.post('/api/create')
def resCreate():
    return ReservationController().createRes()
