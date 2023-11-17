
from db import get_db
from protect import getAdminId, getType, getUserId


class log:
    def __init__(self):
        self.db = get_db()

    def get(self):
        mycursor = self.db.cursor()

        if getType() == 'admin':
            mycursor.execute("""SELECT * FROM parking_log_view pv
                             JOIN parking_spot s on s.spot_id = pv.spot_id
                             JOIN parking_lot l on l.lot_id = s.lot_id
                             where l.emp_id=%s""", (getAdminId(),))
        else:
            mycursor.execute("""SELECT * FROM parking_log_view where cust_id=%s""", (getUserId(),))
            
        return mycursor.fetchall()

    def getSinglelog(self, log_id):
        mycursor = self.db.cursor()
        mycursor.execute(
            """SELECT * FROM parking_log where log_id=%s""", (log_id,))
        return mycursor.fetchone()
