
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
            mycursor.execute(
                """SELECT * FROM reservation where cust_id=%s""", (getUserId(),))

        res = mycursor.fetchall()
        return res

    def getSingleReservation(self, id):
        # to-do have to fix this, shouldn't query all data and filter
        reservation = self.collections.get('reservation')
        for reserve in reservation:
            if str(reserve.get('id')) == id:
                return reserve
        return {}

    def createRes(self, dict):
        mycursor = self.db.cursor(buffered=True)

        mycursor.execute("""SELECT spot_id FROM parking_spot where lot_id=%s""", (dict['lotId'],))

        spot_id = mycursor.fetchone()[0]

        mycursor.execute("""SELECT MAX(res_id) FROM reservation""")

        res_id = mycursor.fetchone()[0]
        res_id += 1

        print(spot_id, res_id)

        mycursor.execute(
            """INSERT INTO reservation
                    (res_id, cust_id, spot_id, checkin_time, checkout_time, status)
                VALUES
                    (%s, %s, %s, %s, %s, %s)""", (res_id, getUserId(), spot_id, dict['startTime'], dict['endTime'], "new",))
        self.db.commit()
        return mycursor.rowcount
