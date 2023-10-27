
from db import get_db

class Customer:
    def __init__(self):
        self.db = get_db()
    
    def get(self):
        mycursor = self.db.cursor()
        mycursor.execute("""SELECT * FROM customer;""")
        # res = mycursor.fetchall()
        # print(res)
        # return res
        return mycursor.fetchall()

    def getSingleCustomer(self, cust_id):
        # customers=self.collections.get('customer')
        # for cust in customers:
        #     if str(cust.get('id'))==id: 
        #         return cust
        # return {}
        mycursor = self.db.cursor()
        mycursor.execute(
            """SELECT * FROM customer where cust_id=%s""", (cust_id,))
        return mycursor.fetchone()
    
    def updateCust(self, dict):
        mycursor=self.db.cursor()
        print(dict)
        mycursor.execute(
            """UPDATE customer
                    SET first_name=%s, last_name=%s, email=%s, phone_number=%s, address=%s,user_name=%s, password=%s
                WHERE cust_id=%s""", (dict['first_name'],dict['last_name'],dict['email'],dict['phone_number'], dict['address'], dict['username'], dict['password'],dict['custId']))
        self.db.commit()
        #print(dict)
        return mycursor.rowcount

    def deleteCust(self, dict):
        mycursor = self.db.cursor()
        print(dict)
        mycursor.execute(
            """DELETE FROM customer
                WHERE cust_id=%s""", ( dict['custId'],))
        self.db.commit()
        return mycursor.rowcount

    def createCust(self, dict):
        print(dict)
        mycursor = self.db.cursor()

        mycursor.execute("""SELECT MAX(cust_id) FROM customer""")

        cust_id = mycursor.fetchone()[0]
        cust_id += 1

        mycursor.execute(
            """INSERT INTO customer
                    (cust_id, first_name, last_name, email, phone_number, address,user_name, password)
                VALUES
                    (%s, %s, %s, %s, %s, %s, %s, %s)""", (cust_id,dict['first_name'],dict['last_name'],dict['email'],dict['phone_number'], dict['address'], dict['username'], dict['password'],))
        self.db.commit()
        return mycursor.rowcount