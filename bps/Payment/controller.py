from .model import Payment

class PaymentController:
    def __init__(self):
        self.model=Payment()

    def get(self):
        data=self.model.get()
        if not data:
            return {'status':False, 'data':data, 'message':'Data is not found'}
        return {'status':True, 'data':data, 'message':''} 
