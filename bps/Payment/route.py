from flask import Blueprint

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
def paymentList():
    return PaymentController().get()


@payment.post('/api/make')
def makePmt():
    return PaymentController().make_pmt()


@payment.get('/api/analytics/')
def analytics():
    return PaymentController().analytics()
