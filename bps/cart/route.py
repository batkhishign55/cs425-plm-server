from flask import Blueprint, render_template
from .controller import CartController

cart=Blueprint(
    'cart', __name__, static_folder='static', template_folder='templates',
    url_prefix='/cart'
    )

@cart.get('/')
def index():
    return render_template( 'cart.html')

@cart.get('/api/')
def listOfCartItems():
    return CartController().getCart()

@cart.get('/api/total-items')
def totalOfCartItems():
    return CartController().getTotalItemsInCart()

@cart.post('/api/')
def addNewDataToCart():
    return CartController().addNewItemToCart()

@cart.delete('/api/')
def removeItemFromCart():
    return CartController().removeItemFromCart()