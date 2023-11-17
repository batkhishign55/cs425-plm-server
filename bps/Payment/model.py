
from db import get_db
from protect import getAdminId, getType, getUserId


class Payment:
    def __init__(self):
        self.db = get_db()

    def get(self):
        mycursor = self.db.cursor()

        if getType() == 'admin':
            mycursor.execute("""SELECT * FROM payment p
                             JOIN parking_log lg on lg.log_id = p.log_id
                             JOIN parking_spot s on s.spot_id = lg.spot_id
                             JOIN parking_lot l on l.lot_id = s.lot_id
                             where l.emp_id=%s""", (getAdminId(),))
        else:
            mycursor.execute("""SELECT * FROM payment where cust_id=%s""", (getUserId(),))
        res = mycursor.fetchall()
        return res

    def getSinglePayment(self, id):
        # to-do have to fix this, shouldn't query all data and filter
        payments = self.collections.get('payment')
        for payment in payments:
            if str(payment.get('id')) == id:
                return payment
        return {}
