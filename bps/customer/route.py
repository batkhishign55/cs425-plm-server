from flask import Blueprint, render_template
from .controller import CustController

cust = Blueprint(
    'cust', __name__, static_folder='static', template_folder='templates',
    url_prefix='/cust'
)


@cust.get('/<cust_id>')
def index(cust_id):
    return render_template('customerForm.html')

@cust.get('/api/')
def custList():
    return CustController().get()

@cust.get('/api/detail/<cust_id>')
def custDetail(cust_id):
    return CustController().getSingleCustomer(cust_id)

@cust.post('/api/update')
def custUpdate():
    return CustController().updateCust()

@cust.delete('/api/')
def custDelete():
    return CustController().deleteCust()