from flask import Blueprint, render_template
from .controller import PaymentController

payment = Blueprint(
    'payment', __name__, static_folder='static', template_folder='templates',
    url_prefix='/pay'
)


@payment.get('/api/')
def lotList():
    return PaymentController().get()
