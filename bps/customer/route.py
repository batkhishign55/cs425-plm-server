from flask import Blueprint, render_template, session

from protect import adminProtect
from .controller import CustController

cust = Blueprint(
    'cust', __name__, static_folder='static', template_folder='templates',
    url_prefix='/cust'
)


@cust.before_request
@adminProtect
def login_required():
    pass


@cust.get('/<cust_id>')
def form(cust_id):
    return render_template('customerForm.html', type=session["object"]["type"])


@cust.get('/create/')
def index():
    return render_template('customerForm.html', type=session["object"]["type"])


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


@cust.post('/api/create')
def custCreate():
    return CustController().createCust()


@cust.get('/api/allusers/')
def analytics():
    return CustController().allUsers()
