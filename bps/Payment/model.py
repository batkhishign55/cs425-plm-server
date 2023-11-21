
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
            mycursor.execute(
                """SELECT * FROM payment where cust_id=%s""", (getUserId(),))
        res = mycursor.fetchall()
        return res

    def getSinglePayment(self, id):
        # to-do have to fix this, shouldn't query all data and filter
        payments = self.collections.get('payment')
        for payment in payments:
            if str(payment.get('id')) == id:
                return payment
        return {}

    def analytics(self):
        mycursor = self.db.cursor()

        mycursor.execute("""SELECT cust_id, pmt_mode,sum(pmt_amt) FROM payment
                            GROUP BY cust_id, pmt_mode
                            with ROLLUP
                            ORDER BY cust_id, pmt_mode;""")
        res = mycursor.fetchall()
        return res

    def create_pmt(self, dict):
        mycursor = self.db.cursor()

        try:
            mycursor.execute("""SELECT MAX(pmt_id) FROM payment""")
            pmt_id = mycursor.fetchone()[0]
            pmt_id += 1
            mycursor.execute(
                """INSERT INTO payment
                    (pmt_id, log_id, cust_id, pmt_mode, pmt_amt, pmt_status)
                VALUES
                    (%s, %s, %s, %s, %s, %s)""", (pmt_id, dict['logId'], getUserId(), dict['pmtMode'], dict['pmtAmt'], "success",))
            self.db.commit()
        except Exception as e:
            self.db.rollback()
            raise e
        return mycursor.rowcount
