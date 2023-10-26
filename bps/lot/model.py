
from db import get_db


class Lot:
    def __init__(self):
        self.db = get_db()

    def get(self):
        mycursor = self.db.cursor()
        mycursor.execute("""SELECT * FROM parking_lot""")
        return mycursor.fetchall()

    def getSingleLot(self, lot_id):
        mycursor = self.db.cursor()
        mycursor.execute(
            """SELECT * FROM parking_lot WHERE lot_id=%s""", (lot_id,))
        return mycursor.fetchone()

    def updateLot(self, dict):
        mycursor = self.db.cursor()
        mycursor.execute(
            """UPDATE parking_lot
                    SET lot_name=%s, location=%s, total_spots=%s, available_spots=%s, emp_id=%s
                WHERE lot_id=%s""", (dict['name'], dict['location'], dict['totalSpots'], dict['availableSpots'], dict['employee'], dict['lotId'],))
        self.db.commit()
        return mycursor.rowcount

    def deleteLot(self, dict):
        mycursor = self.db.cursor()
        mycursor.execute(
            """DELETE FROM parking_lot
                WHERE lot_id=%s""", ( dict['lotId'],))
        self.db.commit()
        return mycursor.rowcount
