from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="plm"
)


@app.get('/')
def index():
    return render_template('store.html')


mycursor = db.cursor()
mycursor.execute("SELECT * FROM parking_log;")
myresult = mycursor.fetchall()

for x in myresult:
    print(x)


# app.register_blueprint(user)
# app.register_blueprint(cart)
# app.register_blueprint(product)

if __name__ == '__main__':
    app.run(debug=True, port=8887)
