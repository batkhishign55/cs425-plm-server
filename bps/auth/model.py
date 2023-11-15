from db import get_db


class Auth:
    def __init__(self):
        self.db = get_db()

    def getEmployee(self, username):
        mycursor = self.db.cursor()
        mycursor.execute(
            """SELECT * from employee WHERE user_name=%s""", (username,))
        return mycursor.fetchone()

    def getUser(self, username):
        mycursor = self.db.cursor()
        mycursor.execute(
            """SELECT * from customer WHERE user_name=%s""", (username,))
        return mycursor.fetchone()