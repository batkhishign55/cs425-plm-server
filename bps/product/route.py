from flask import Blueprint, render_template
from .controller import ProductController

product=Blueprint(
    'product', __name__, static_folder='static', template_folder='templates',
    url_prefix='/product'
    )

@product.get('/<productId>')
def index(productId):
    return render_template('product.html')

@product.get('/api/')
def productList():
    return ProductController().get()

@product.get('/api/detail/<productId>')
def certainProduct(productId):
    return ProductController().getSingleProduct(productId)