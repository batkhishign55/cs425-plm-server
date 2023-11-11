from werkzeug.exceptions import HTTPException
from flask import Flask, abort, redirect, render_template, request, session, url_for
from bps.auth.route import authbp
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
app.register_blueprint(authbp)


with app.app_context():
    init_db()


@app.errorhandler(Exception)
def catch_server_errors(e: Exception):
        print(e)
        return {'message': str(e)}, 500


def login_required(func):
    def secure_function(*args, **kwargs):
        print(session)
        if "email" not in session:
            return redirect(url_for("auth.login"))
        return func(*args, **kwargs)

    return secure_function


@app.get('/')
@login_required
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


app.secret_key = 'some secret key'


if __name__ == '__main__':
    app.run(debug=True, port=8887)
