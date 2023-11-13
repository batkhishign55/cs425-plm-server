from flask import Blueprint, render_template

from protect import protect

from .controller import PaymentController

payment = Blueprint(
    'payment', __name__, static_folder='static', template_folder='templates',
    url_prefix='/pay'
)


@payment.before_request
@protect
def login_required():
    pass


@payment.get('/api/')
def lotList():
    return PaymentController().get()
