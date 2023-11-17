from .model import Payment


class PaymentController:
    def __init__(self):
        self.model = Payment()

    def get(self):
        data = self.model.get()
        if not data:
            return {'message': 'no data found!'}, 404
        return {'data': data}

    def analytics(self):
        data = self.model.analytics()
        if not data:
            return {'message': 'no data found!'}, 404
        return {'data': data}
