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


# Modify the search_suggestions route to include suggestions for lot_name
@app.route('/api/search_suggestions')
def search_suggestions():
    search_value = request.args.get('source')

    db = get_db()
    cursor = db.cursor(dictionary=True)

    # Query your database to get suggestions based on the input
    # Adjust the query based on your database schema and requirements
    query = (
        "SELECT DISTINCT location, zipcode, lot_name FROM parking_lot "
        "WHERE location LIKE %s OR zipcode LIKE %s OR lot_name LIKE %s"
    )
    cursor.execute(query, (f"%{search_value}%", f"%{search_value}%", f"%{search_value}%"))
    suggestions_data = cursor.fetchall()

    # Extract distinct suggestions for location, zipcode, and lot_name
    locations = set(item['location'] for item in suggestions_data if item['location'])
    zipcodes = set(item['zipcode'] for item in suggestions_data if item['zipcode'])
    lot_names = set(item['lot_name'] for item in suggestions_data if item['lot_name'])
    suggestions = list(locations | zipcodes | lot_names)

    cursor.close()
    db.close()

    return jsonify(suggestions=suggestions)



# Modify the search_lots route to search by location, zipcode, and lot_name
@app.route('/api/search_lots')
def search_lots():
    source = request.args.get('source')

    db = get_db()
    cursor = db.cursor(dictionary=True)

    # Assuming you have a 'parking_lots' table in your database
    query = (
        "SELECT lot_id, lot_name, location, total_spots, available_spots "
        "FROM parking_lot WHERE "
        "location LIKE %s OR zipcode LIKE %s OR lot_name LIKE %s ORDER BY lot_id"
    )
    cursor.execute(query, (f"%{source}%", f"%{source}%", f"%{source}%"))
    parking_lots_data = cursor.fetchall()

    cursor.close()

    return jsonify(parking_lots=parking_lots_data)


    
if __name__ == '__main__':
    app.run(debug=True, port=8887)
