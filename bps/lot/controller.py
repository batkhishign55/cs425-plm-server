from .model import Lot


class LotController:
    def __init__(self):
        self.model = Lot()

    def get(self):
        data = self.model.get()
        if not data:
            return {'status': False, 'data': data, 'message': 'Data is not found'}
        return {'status': True, 'data': data, 'message': ''}

    def getSingleLot(self, lot_id):
        data = self.model.getSingleLot(lot_id)
        if not data:
            return {'status': False, 'data': data, 'message': 'Data is not found'}
        return {'status': True, 'data': data, 'message': ''}
