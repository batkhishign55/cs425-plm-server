from flask import Flask, render_template
from bps.lot.route import lot
from bps.user.route import user
from bps.customer.route import cust
from bps.Reservation.route import reservation
from bps.Payment.route import payment


from db import init_db

app = Flask(__name__)

app.register_blueprint(user)
app.register_blueprint(lot)
app.register_blueprint(cust)
app.register_blueprint(reservation)
app.register_blueprint(payment)


with app.app_context():
    init_db()

@app.get('/')
def index():
    return render_template('lots.html')

@app.get('/cust')
def cust():
    return render_template('customer.html')

@app.get('/res')
def reservation():
    return render_template('reservation.html')

@app.get('/pay')
def payment():
    return render_template('payment.html')

if __name__ == '__main__':
    app.run(debug=True, port=8887)
