from .model import Reservation

class ReservationController:
    def __init__(self):
        self.model=Reservation()

    def get(self):
        data=self.model.get()
        if not data:
            return {'status':False, 'data':data, 'message':'Data is not found'}
        return {'status':True, 'data':data, 'message':''} 
