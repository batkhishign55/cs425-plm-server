
from db import get_db
from protect import getUserId


class Vehicle:
    def __init__(self):
        self.db = get_db()

    def get(self):
        mycursor = self.db.cursor()
        mycursor.execute(
            """SELECT * FROM vehicle where cust_id=%s""", (getUserId(),))

        return mycursor.fetchall()

    def getSingleVehicle(self, vehicle_id):
        mycursor = self.db.cursor()
        mycursor.execute(
            """SELECT * FROM vehicle WHERE vehicle_id=%s""", (vehicle_id,))
        return mycursor.fetchone()

    def updateVehicle(self, dict):
        mycursor = self.db.cursor()
        mycursor.execute(
            """UPDATE vehicle
                    SET plate_number=%s, vehicle_type=%s
                WHERE vehicle_id=%s""", (dict['plateNumber'], dict['type'], dict['vehicleId'],))
        self.db.commit()
        return mycursor.rowcount

    def deleteVehicle(self, dict):
        mycursor = self.db.cursor()
        mycursor.execute(
            """DELETE FROM vehicle
                WHERE vehicle_id=%s""", (dict['vehicleId'],))
        self.db.commit()
        return mycursor.rowcount

    def createVehicle(self, dict):
        mycursor = self.db.cursor()

        mycursor.execute("""SELECT MAX(vehicle_id) FROM vehicle""")
        vehicle_id = mycursor.fetchone()[0]
        vehicle_id += 1

        mycursor.execute(
            """INSERT INTO vehicle
                    (vehicle_id, cust_id,plate_number, vehicle_type)
                VALUES
                    (%s, %s, %s, %s)""", (vehicle_id, getUserId(), dict['plateNumber'], dict['type']))
        self.db.commit()
        return mycursor.rowcount
