from flask import Flask, render_template, session,jsonify, request, abort, session

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


@app.get('/home')
@userProtect
def home():
    return render_template('user_home.html', type=session["object"]["type"])

@app.get('/park')
@userProtect
def park():
    return render_template('park_vehicle.html', type=session["object"]["type"])

@app.get('/exit')
@userProtect
def exit():
    # Retrieve the values from session storage
    selected_vehicle_type = session.get('selectedVehicleType', 'None')
    selected_spot_type = session.get('selectedSpotType', 'None')

    # Pass the values to the template
    return render_template('exit_vehicle.html', type=session["object"]["type"],selected_vehicle_type=selected_vehicle_type, selected_spot_type=selected_spot_type)



@app.get('/analytics')
@adminProtect
def analytics():
    return render_template('analytics.html')


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


#Modify the search_suggestions route to include suggestions for lot_name
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




@app.route('/park', methods=['POST'])
@protect  # You may want to protect this route based on user roles
def park_vehicle():
    try:
        # Retrieve form data
        vehicle_type = request.form.get('vehicle_type')
        parking_lot = request.form.get('parking_lot')  # Update with the actual name of the field
        spot_type = request.form.get('spot_type')

        # Perform actions to park the vehicle, update the database, etc.

        # Return a success response
        return jsonify({'status': 'success', 'message': 'Vehicle parked successfully'})
    except Exception as e:
        # Handle errors
        return jsonify({'status': 'error', 'message': str(e)}), 500

@app.route('/exit', methods=['POST'])
@userProtect
def exit_vehicle():
    try:
        # Retrieve the values from the form data
        selected_vehicle_type = request.form.get('selected_vehicle_type')
        selected_spot_type = request.form.get('selected_spot_type')

        # Perform any additional actions needed with the selected values

        # Return a success response
        return jsonify({'status': 'success', 'message': 'Vehicle exited successfully'})
    except Exception as e:
        # Handle errors
        return jsonify({'status': 'error', 'message': str(e)}), 500
    
    
    
if __name__ == '__main__':
    app.run(debug=True, port=8887)
