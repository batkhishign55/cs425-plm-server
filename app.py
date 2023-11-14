from werkzeug.exceptions import HTTPException
from flask import Flask, abort, redirect, render_template, request, session, url_for

from bps.auth.route import authbp
from bps.lot.route import lot
from bps.user.route import user
from bps.customer.route import cust
from bps.Reservation.route import reservation
from bps.Payment.route import payment
from bps.log.route import log

from db import init_db
from protect import protect

app = Flask(__name__)

app.register_blueprint(user)
app.register_blueprint(lot)
app.register_blueprint(cust)
app.register_blueprint(reservation)
app.register_blueprint(payment)
app.register_blueprint(authbp)


with app.app_context():
    init_db()


@app.errorhandler(Exception)
def catch_server_errors(e: Exception):
        print(e)
        return {'message': str(e)}, 500


@app.get('/')
@protect
def index():
    return render_template('index.html')


@app.get('/lot')
def lots():
    return render_template('lots.html')


@app.get('/cust')
@protect
def cust():
    return render_template('customer.html')


@app.get('/res')
@protect
def reservation():
    return render_template('reservation.html')


@app.get('/pay')
@protect
def payment():
    return render_template('payment.html')


@app.get('/log')
@protect
def log():
    return render_template('logs.html')


app.secret_key = 'some secret key'


@app.get('/log')
def logs():
    return render_template('logs.html')

@app.get('/usersignup')
def usersignup():
    return render_template('usersignup.html')

@app.get('/userlogin')
def userlogin():
    return render_template('userlogin.html')

@app.get('/admin')
def admin():
    return render_template('admin.html')

if __name__ == '__main__':
    app.run(debug=True, port=8887)
