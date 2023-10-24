from flask import Flask, render_template
from bps.cart.route import cart
from bps.lot.route import lot
from bps.user.route import user
from bps.product.route import product
from db import init_db

app = Flask(__name__)

app.register_blueprint(user)
app.register_blueprint(cart)
app.register_blueprint(product)
app.register_blueprint(lot)

with app.app_context():
    init_db()

@app.get('/')
def index():
    return render_template('lots.html')


if __name__ == '__main__':
    app.run(debug=True, port=8887)
