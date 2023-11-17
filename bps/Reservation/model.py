
from db import get_db
from protect import getAdminId, getType, getUserId


class Reservation:
    def __init__(self):
        self.db = get_db()

    def get(self):
        mycursor = self.db.cursor()

        if getType() == 'admin':
            mycursor.execute("""SELECT * FROM reservation r
                                JOIN parking_spot s on r.spot_id = s.spot_id
                                JOIN parking_lot l on s.lot_id = l.lot_id
                             where l.emp_id=%s""", (getAdminId(),))
        else:
            mycursor.execute("""SELECT * FROM reservation where cust_id=%s""", (getUserId(),))
            
        res = mycursor.fetchall()
        return res

    def getSingleReservation(self, id):
        # to-do have to fix this, shouldn't query all data and filter
        reservation = self.collections.get('reservation')
        for reserve in reservation:
            if str(reserve.get('id')) == id:
                return reserve
        return {}
