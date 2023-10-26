from flask import Blueprint, render_template

from .controller import ReservationController

reservation = Blueprint(
    'reservation', __name__, static_folder='static', template_folder='templates',
    url_prefix='/res'
)


@reservation.get('/api/')
def reservationList():
    return ReservationController().get()
