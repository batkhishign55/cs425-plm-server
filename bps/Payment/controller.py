from flask import request

from bps.log.model import log
from .model import Payment


class PaymentController:
    def __init__(self):
        self.model = Payment()

    def get(self):
        data = self.model.get()
        if not data:
            return {'message': 'no data found!'}, 404
        return {'data': data}

    def make_pmt(self):
        data = self.model.create_pmt(request.json)
        log_model = log()
        log_model.updateCheckout(request.json['logId'])
        return {'data': data}

    def analytics(self):
        data = self.model.analytics()
        if not data:
            return {'message': 'no data found!'}, 404
        return {'data': data}
