from flask import Flask, render_template, session,jsonify, request, abort

from bps.auth.route import authbp
from bps.lot.route import lot
from bps.user.route import user
from bps.customer.route import cust
from bps.Reservation.route import reservation
from bps.Payment.route import payment
from bps.log.route import log
from bps.vehicle.route import vehicle

from db import init_db,get_db
from protect import adminProtect, protect, userProtect

app = Flask(__name__)

app.register_blueprint(user)
app.register_blueprint(lot)
app.register_blueprint(cust)
app.register_blueprint(reservation)
app.register_blueprint(payment)
app.register_blueprint(authbp)
app.register_blueprint(vehicle)


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


@app.get('/home')
@userProtect
def home():
    return render_template('user_home.html', type=session["object"]["type"])


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


@app.route('/api/search_suggestions')
def search_suggestions():
    search_value = request.args.get('source')

    db = get_db()
    cursor = db.cursor(dictionary=True)

    try:
        # Use parameterized query to prevent SQL injection
        query = (
            "SELECT DISTINCT location, zipcode FROM parking_lot "
            "WHERE location LIKE %(search_value)s OR zipcode LIKE %(search_value)s"
        )
        cursor.execute(query, {'search_value': f"%{search_value}%"})
        suggestions = cursor.fetchall()

        # Extract location and zipcode from the query result
        suggestions = [f"{entry['location']}, {entry['zipcode']}" for entry in suggestions]
    except Exception as e:
        print(f"Error: {e}")
        abort(500)
    finally:
        cursor.close()
        db.close()

    return jsonify(suggestions=suggestions)


@app.route('/api/search_lots')
def search_lots():
    source = request.args.get('source')

    db = get_db()
    cursor = db.cursor(dictionary=True)

    # Assuming you have a 'parking_lots' table in your database
    query = (
        "SELECT lot_id, lot_name, location, total_spots, available_spots "
        "FROM parking_lot WHERE location LIKE %s OR zipcode LIKE %s ORDER BY lot_id"
    )
    cursor.execute(query, (f"%{source}%", f"%{source}%"))
    parking_lots_data = cursor.fetchall()

    cursor.close()

    return jsonify(parking_lots=parking_lots_data)
    
if __name__ == '__main__':
    app.run(debug=True, port=8887)
