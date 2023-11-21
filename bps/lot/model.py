
from db import get_db
from protect import getAdminId


class Lot:
    def __init__(self):
        self.db = get_db()

    def getAll(self):
        mycursor = self.db.cursor()
        mycursor.execute(
            """SELECT pl.*
                    FROM parking_lot pl""")
        return mycursor.fetchall()

    def get(self):
        mycursor = self.db.cursor()
        mycursor.execute(
            """SELECT pl.*, e.first_name, e.last_name
                    FROM parking_lot pl
                LEFT JOIN employee e on e.emp_id=pl.emp_id
                where pl.emp_id=%s """, (getAdminId(),))
        return mycursor.fetchall()

    def getSingleLot(self, lot_id):
        mycursor = self.db.cursor()
        mycursor.execute(
            """SELECT * FROM parking_lot WHERE lot_id=%s""", (lot_id,))
        return mycursor.fetchone()

    def updateLot(self, dict):
        mycursor = self.db.cursor()
        try:
            mycursor.execute(
                """UPDATE parking_lot
                        SET lot_name=%s, location=%s, total_spots=%s, available_spots=%s
                    WHERE lot_id=%s""", (dict['name'], dict['location'], dict['totalSpots'], dict['availableSpots'], dict['lotId'],))
            self.db.commit()
        except Exception as e:
            self.db.rollback()
            raise e
        return mycursor.rowcount

    def deleteLot(self, dict):
        mycursor = self.db.cursor()
        mycursor.execute(
            """DELETE FROM parking_lot
                WHERE lot_id=%s""", (dict['lotId'],))
        self.db.commit()
        return mycursor.rowcount

    def createLot(self, dict):
        mycursor = self.db.cursor()

        mycursor.execute("""SELECT MAX(lot_id) FROM parking_lot""")

        lot_id = mycursor.fetchone()[0]
        lot_id += 1

        mycursor.execute(
            """INSERT INTO parking_lot
                    (lot_id, lot_name, location, total_spots, available_spots, emp_id)
                VALUES
                    (%s, %s, %s, %s, %s, %s)""", (lot_id, dict['name'], dict['location'], dict['totalSpots'], dict['availableSpots'], getAdminId(),))
        self.db.commit()
        return mycursor.rowcount

    def getSpot(self, lotId):
        mycursor = self.db.cursor()
        mycursor.execute(
            """SELECT * from parking_spot
                where lot_id=%s and status="available" """, (lotId,))
        return mycursor.fetchall()
