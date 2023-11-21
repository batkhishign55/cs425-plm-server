from flask import Flask, render_template, session, jsonify, request, abort, session

from bps.auth.route import authbp
from bps.lot.route import lot
from bps.user.route import user
from bps.customer.route import cust
from bps.Reservation.route import reservation
from bps.Payment.route import payment
from bps.log.route import log
from bps.vehicle.route import vehicle

from db import init_db, get_db
from protect import adminProtect, protect, userProtect

app = Flask(__name__)

app.register_blueprint(user)
app.register_blueprint(lot)
app.register_blueprint(cust)
app.register_blueprint(reservation)
app.register_blueprint(payment)
app.register_blueprint(authbp)
app.register_blueprint(vehicle)
app.register_blueprint(log)


with app.app_context():
    init_db()


@app.errorhandler(Exception)
def catch_server_errors(e: Exception):
    print(e)
    return {'message': str(e)}, 500


@app.get('/')
def index():
    return render_template('index.html')


@app.get('/lot')
@protect
def lots():
    return render_template('lots.html', type=session["object"]["type"])


@app.get('/cust')
@adminProtect
def cust():
    return render_template('customer.html', type=session["object"]["type"])


@app.get('/res')
@protect
def reservation():
    return render_template('reservation.html', type=session["object"]["type"])


@app.get('/pay')
@protect
def payment():
    return render_template('payment.html', type=session["object"]["type"])


@app.get('/log')
@protect
def log():
    return render_template('logs.html', type=session["object"]["type"])


@app.get('/vehicle')
@userProtect
def vehicle():
    return render_template('vehicle.html', type=session["object"]["type"])

@app.get('/user_profile')
@userProtect
def user_profile():
    return render_template('user_profile.html')

@app.get('/admin_profile')
@adminProtect
def admin_profile():
    return render_template('admin_profile.html')

@app.get('/home')
@userProtect
def home():
    return render_template('user_home.html', type=session["object"]["type"])


@app.get('/analytics')
@adminProtect
def analytics():
    return render_template('analytics.html', type=session["object"]["type"])


@app.get('/allusers')
@adminProtect
def allUsers():
    return render_template('all_users.html', type=session["object"]["type"])


app.secret_key = 'some secret key'


@app.get('/log')
def logs():
    return render_template('logs.html', type=session["object"]["type"])


@app.get('/usersignup')
def usersignup():
    return render_template('usersignup.html')


@app.get('/userlogin')
def userlogin():
    return render_template('userlogin.html')


@app.get('/adminlogin')
def admin():
    return render_template('admin_login.html')


if __name__ == '__main__':
    app.run(debug=True, port=8887)
